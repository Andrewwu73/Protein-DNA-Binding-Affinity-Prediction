import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

# TO CHANGE
dataset = '../Datasets/Protein-DNA Complex/ProNIT_filtered.csv'
column_names = ['entry', 'sequence', 'sequence_wild1', 'pronit_t', 'p_h',
                'd_g_wild', 'stoichiometry']

raw_dataset = pd.read_csv(dataset, names=column_names,
                          sep=',', skipinitialspace=True)

train_dataset = raw_dataset.sample(frac=0.8, random_state=0)
test_dataset = raw_dataset.drop(train_dataset.index)
#sns.pairplot(train_dataset[['MPG', 'Cylinders', 'Displacement', 'Weight']], diag_kind='kde') ?

train_features = train_dataset.copy()
test_features = test_dataset.copy()
# CHANGE OT BINDING AFFINTIY
train_labels = train_features.pop('d_g_wild')
test_labels = test_features.pop('d_g_wild')

def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model
    
