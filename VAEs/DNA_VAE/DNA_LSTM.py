# lstm autoencoder reconstruct and predict sequence
from numpy import array
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import RepeatVector
from tensorflow.keras.layers import TimeDistributed
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from TF_VAE_DNA import CVAE
import datetime as time
from generate_dna_onehot import obtainDNAData

class DNA_LSTM():
    def __init__(self, latent_dim=64, reg_coeff=0.00001, dropout_rate=0.001):
        l2 = tf.keras.regularizers.l2(l2=reg_coeff)
        self.model = Sequential()
        self.model.add(LSTM(latent_dim, activation='tanh', input_shape=(500,4), kernel_regularizer=l2))
        self.model.add(RepeatVector(n_in))
        self.model.add(LSTM(latent_dim, activation='tanh', return_sequences=True, dropout=dropout_rate, kernel_regularizer=l2))
        self.model.add(TimeDistributed(Dense(4)))
        self.model.compile(optimizer='adam', loss="mse", metrics=['accuracy'])


    def train(self, epochs=30):

        history = self.model.fit(seq_in, seq_in, epochs=epochs, verbose=2, validation_split=0.2)

        encoder_model = Model(inputs=self.model.inputs, outputs=self.model.layers[0].output)

        '''
        print(yhat.shape)
        print(yhat[:,:,:])
        print('-----')
        print(model.summary())
        '''

        encoder_model.save_weights('dna_lstm_encoder')
        self.model.save_weights('dna_lstm_full_model')

    def predict(self, directory, dataset):

        self.model.load_weights(directory)
        yhat = self.model.predict(dataset, verbose=2)

        return yhat

    def get_accuracies(self, directory, dataset):
        num = 1000
        samples = dataset[0:num]

        ret = self.predict(directory, dataset)
        accuracies = []
        gc = []
        for i, j in zip(range(num - 1), range(1, num)):
            arr1 = tf.math.argmax(ret[i:j], axis = 2)
            arr2 = tf.math.argmax(samples[i:j], axis = 2)
            errors = 0
            gc_content = 0
            for bp1, bp2 in zip(tf.reshape(arr1, [-1]), tf.reshape(arr2, [-1])):
                if bp1 != bp2:
                    errors += 1
                if (bp2 == 0 or bp2 == 3):
                    gc_content += 1
            accuracies.append(1 - errors/500)
            gc.append(gc_content/500)

        import matplotlib.pyplot as plt
        plt.scatter(gc, accuracies)
        plt.show()

dataset_directory = "../../Datasets/FinalDatasets/5SpeciesDNA.csv"
dna_dataset_obtainer = obtainDNAData(dataset_directory)
train_dataset, test_dataset = dna_dataset_obtainer.obtainData()
seq_in = tf.cast(tf.convert_to_tensor(train_dataset), dtype=tf.float32)
test_dataset = tf.cast(tf.convert_to_tensor(test_dataset), dtype=tf.float32)

n_in = 500
lstm = DNA_LSTM(64,0.00001, 0.001)
lstm.get_accuracies('dna_lstm_full_model', test_dataset)
