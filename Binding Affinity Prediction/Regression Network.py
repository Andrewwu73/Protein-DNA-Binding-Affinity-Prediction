import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import csv
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
from sklearn.preprocessing import OneHotEncoder
from TF_VAE_PROTEIN import CVAE as protein_vae
from TF_VAE_DNA import CVAE as dna_vae
import operator
import random
protein_len = 496
dna_len = 500
amino_acids = np.array(['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
        'Q', 'R', 'S', 'T', 'V', 'W', 'Y', '_'], dtype='<U1')
nucleic_acids = np.array(['A', 'C', 'T', 'G'], dtype='<U1')
enc = OneHotEncoder(categories = [amino_acids for i in range(protein_len)],
                    sparse = False, 
                    handle_unknown='ignore')
enc_dna = OneHotEncoder(categories = [nucleic_acids for i in range(dna_len)],
                        sparse= False,
                        handle_unknown='ignore')

protein_encoder = protein_vae(40, (496, 21, 1), 0.0001, 0.5)
protein_encoder.load_weights("../VAEs/Protein_VAE/Protein_VAE")

dna_encoder = dna_vae(64, (500, 4, 1), 0.00005, 0.001)
dna_encoder.load_weights("../VAEs/DNA_VAE/dna_model")

dataset = '../Datasets/Protein-DNA Complex/ProNIT_Final.csv'
column_names = ['protein_sequence', 'dna_sequence', 'd_g_wild', 'entry']


raw_dataset = pd.read_csv(dataset, names=column_names,
                          sep=',', skipinitialspace=True)

train_dataset = raw_dataset.sample(frac=0.8, random_state=0)
test_dataset = raw_dataset.drop(train_dataset.index)

train_features = train_dataset.copy()
test_features = test_dataset.copy()
def process_data(features, normalize = True):
  dna_sequences = []
  protein_sequences = []
  d_gs = []
  for i in features['entry'].keys():
    dna = features['dna_sequence'][int(i)]
    protein = features['protein_sequence'][int(i)]
    d_g = features['d_g_wild'][int(i)]
    if(type(dna)==str and type(protein)==str and protein[0]!='(' and type(d_g)==str):
        protein = list(protein.upper().rstrip().ljust(496, '_')[:496])
        dna = list(dna.upper().rstrip().ljust(500, ' ')[:500])
        d_g_v = d_g.split(' ')
        if(len(d_g_v)>=3):
          d_g_v = d_g_v[1]
        else:
          d_g_v = d_g_v[0]
        try:
          allowed = True
          if(normalize and float(d_g_v)>-14 and float(d_g_v) < -4):
            allowed = (random.random() < 0.15)
          if(allowed):
            d_gs.append(float(d_g_v))
            protein_sequences.append(protein)
            dna_sequences.append(dna)
        except:
          print(d_g)
  dna_sequences = enc_dna.fit_transform(dna_sequences).reshape(-1, dna_len, 4, 1).astype('float32')
  protein_sequences = enc.fit_transform(protein_sequences).reshape(-1, protein_len, 21, 1).astype('float32')
  latent_protein = tf.concat(protein_encoder.encode(protein_sequences), axis=1)
  latent_dna = tf.concat(dna_encoder.encode(dna_sequences), axis=1)
  return tf.concat([latent_protein, latent_dna], axis=1), tf.convert_to_tensor(d_gs)
train_data, train_labels = process_data(train_features, True)
test_data, test_labels = process_data(test_features, False)

def build_and_compile_model(arch='leaky', loss='MeanSquaredError'):

  if(arch=='leaky'):
    model = keras.Sequential([
        layers.Dense(128, activation=None),
        layers.LeakyReLU(),
        layers.Dense(64, activation=None),
        layers.LeakyReLU(),
        layers.Dropout(0.2),
        layers.Dense(64, activation=None),
        layers.LeakyReLU(),
        layers.Dense(1)
    ])
  elif(arch=='2'):
    model = keras.Sequential([
      layers.Dense(128, activation='relu'),
      layers.Dropout(0.2),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
    ])
  elif(arch=='3'):
    model = keras.Sequential([
      layers.Dense(128, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dropout(0.2),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
    ])
  else:
    model = keras.Sequential([
      layers.Dense(1)
    ])
  

  
  model.compile(loss=loss,
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

def plot_data(data):
  plt.xlabel('Binding Affinity in kcal/mol')
  plt.ylabel('Number of Protein-DNA Pairs in Binding Affinity Range')
  plt.hist(data.numpy(), 20)
  plt.show()

#plot_data(train_labels)
def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.ylim([0, 30])
  plt.xlabel('Epoch')
  plt.ylabel('Mean Squared Error for dG kcal/mol')
  plt.legend()
  plt.grid(True)
  plt.show()

def plot_test_results(model):
  test_predictions = model.predict(test_data).flatten()
  a = plt.axes(aspect='equal')
  plt.scatter(test_labels, test_predictions)
  plt.xlabel("True Affinities [kcal/mol]")
  plt.ylabel("Predicted Affinities [kcal/mol]")
  lims = [-50, 0]
  plt.xlim(lims)
  plt.ylim(lims)
  plt.plot(lims, lims)
  plt.show()

def plot_rank_correlation(model):
  test_predictions = list(model.predict(test_data).flatten())
  indices = [i for i in range(len(test_data))]
  correct_labels = test_labels.numpy().tolist()
  predicted = dict(zip(indices, test_predictions))
  predictions_sorted_by_correct_labels = [k for k,v in sorted(zip(test_predictions, correct_labels), key = operator.itemgetter(1))]
  # the rank i correct label was given predicted value predictions_***_[i]
  indices_sorted_by_predictions = [k for k,v in sorted(zip(indices, test_predictions), key = operator.itemgetter(1))]
  # the prediction with rank i originally had index indices_***_[i]
  rank_correlation_permutation = [i for i in range(len(test_data))]
  for rank in indices:
    original_index = indices_sorted_by_predictions[rank]
    for i in range(len(predictions_sorted_by_correct_labels)):
      if(test_predictions[original_index]==predictions_sorted_by_correct_labels[i]):
        rank_correlation_permutation[i] = rank
        predictions_sorted_by_correct_labels[i] = 0
        break
  a = plt.axes(aspect='equal')
  plt.scatter(indices, rank_correlation_permutation)
  plt.xlabel("Rank of true Binding Affinity Value")
  plt.ylabel("Rank of predicted Binding Affinity Value")
  lims = [0, len(test_data)]
  plt.xlim(lims)
  plt.ylim(lims)
  plt.plot(lims, lims)
  plt.show()

def outlier_correctness(model, cutoff):
  #We define an outlier as those with values < cutoff kcal/mol.
  #In this method, we compute two values:
  #Precision: Fraction of predicted outliers that are indeed outliers
  #Recall: Fraction of outliers that were successfully predicted.
  test_predictions = list(model.predict(test_data).flatten())
  correct_labels = test_labels.numpy().tolist()
  true_positives = 0
  false_negatives = 0
  false_positives = 0
  for i in range(len(test_predictions)):
    if(test_predictions[i]<cutoff):
      #predicted positive
      if(correct_labels[i]<=cutoff):
        true_positives += 1
      else:
        false_positives += 1
    else:
      if(correct_labels[i]<cutoff):
        false_negatives +=1
  #Return a precision, recall pair
  if(true_positives == 0):
    precision = 0
    recall = 0
  else:
    precision =true_positives/(true_positives+false_positives)
    recall = true_positives/(true_positives+false_negatives)
  return precision, recall


losses = ['MeanSquaredError', 'MeanAbsoluteError']
archs = ['leaky', '3', '2', 'linear']
'''
Final Error Results:
Raw Dataset
- Leaky 3 Layer
  - MAE: 1.7602
  - MSE: 6.8598
- 3 Layer NN
  - MSE: 7.126
  - MAE: 2.380
- 2 Layer NN
  - MSE: 6.9515
  - MAE: 1.882
- Linear Baseline
  - MAE: 1.934
  - MSE: 11.913

Normalized Dataset
- Leaky 3 Layer
  - MSE: 12.23
  - MAE: 2.268
- 3 Layer NN
  - MSE: 17.2416
  - MAE: 2.274
- 2 Layer NN
  - MSE: 14.1737
  - MAE: 2.359
- Linear MSE:
  - MSE: 15.735
  - MAE: 2.238
'''
#for arch in archs:
#  for l in losses:
binding_model = build_and_compile_model('leaky', 'mse')
history = binding_model.fit(train_data, train_labels, validation_split=0.2, verbose=0, epochs=100)
precision, recall = outlier_correctness(binding_model, -20)
print("Precision: " + str(precision))
print("Recall: "+str(recall))
#print("Error for: "+arch + " "+l)
#print(binding_model.evaluate(test_data, test_labels))
#plot_loss(history)
#plot_test_results(binding_model)
#plot_rank_correlation(binding_model)
#TEST MSE = 7.91 for Leaky 3 layer Raw
#TEST MSE = 15.586 for Leaky 3 Layer Normalized 15%
#TEST MAE = 2.1669 for Leaky 3 Layer Normalized 15%

