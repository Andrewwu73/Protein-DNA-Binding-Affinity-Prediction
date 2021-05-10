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

dataset = '../Datasets/Protein-DNA Complex/ProNIT_filtered.csv'
column_names = ['entry', 'sequence', 'sequence_wild1', 'pronit_t', 'p_h',
                'd_g_wild', 'stoichiometry']

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
    dna = features['sequence_wild1'][int(i)]
    protein = features['sequence'][int(i)]
    d_g = features['d_g_wild'][int(i)]
    if(type(dna)==str and type(protein)==str and protein[0]!='(' and type(d_g)==str):
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
            protein_sequences.append(list(protein.upper().rstrip().ljust(496, '_')[:496]))
            dna_sequences.append(list(dna.upper().rstrip().ljust(500, ' ')[:500]))
        except:
          print(d_g)
          
  dna_sequences = enc_dna.fit_transform(dna_sequences).reshape(-1, dna_len, 4, 1).astype('float32')
  protein_sequences = enc.fit_transform(protein_sequences).reshape(-1, protein_len, 21, 1).astype('float32')
  latent_protein = tf.concat(protein_encoder.encode(protein_sequences), axis=1)
  latent_dna = tf.concat(dna_encoder.encode(dna_sequences), axis=1)
  return tf.concat([latent_protein, latent_dna], axis=1), tf.convert_to_tensor(d_gs)
train_data, train_labels = process_data(train_features, True)
test_data, test_labels = process_data(test_features, False)

def build_and_compile_model():
  model = keras.Sequential([
      layers.Dense(128, activation=None),
      layers.LeakyReLU(),
      layers.Dense(64, activation=None),
      layers.LeakyReLU(),
      layers.Dense(64, activation=None),
      layers.LeakyReLU(),
      layers.Dense(1)
  ])

  model.compile(loss='MeanAbsoluteError',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

def plot_data(data):
  plt.hist(data.numpy(), 20)
  plt.show()

plot_data(train_labels)
def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.ylim([0, 30])
  plt.xlabel('Epoch')
  plt.ylabel('Mean Absolute Error for dG kcal/mol')
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
binding_model = build_and_compile_model()
history = binding_model.fit(train_data, train_labels, validation_split=0.2, verbose=1, epochs=400)
plot_loss(history)
plot_test_results(binding_model)

#TEST MSE = 7.91 for Leaky 3 layer Raw
#TEST MSE = 15.586 for Leaky 3 Layer Normalized 15%
#TEST MAE = 2.1669 for Leaky 3 Layer Normalized 15%
print("TEST SET ERROR")
print(binding_model.evaluate(test_data, test_labels))
