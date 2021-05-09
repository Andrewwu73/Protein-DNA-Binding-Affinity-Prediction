import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

'''
Sourced from Tensorflow's tutorial on Variational Autoencoders.
'''

class CVAE(tf.keras.Model):
  """Convolutional variational autoencoder."""

  def __init__(self, latent_dim, shape_of_input, reg_coeff, dropout_rate):
    super(CVAE, self).__init__()
    #print(shape_of_input)
    self.latent_dim = latent_dim
    self.regularizer = tf.keras.regularizers.l2(l2=reg_coeff)
    self.encoder = tf.keras.Sequential(
        [
            tf.keras.layers.InputLayer(input_shape=shape_of_input),
            tf.keras.layers.Conv2D(
                filters=32, kernel_size=(4,1), strides=1, activation='relu', kernel_regularizer=self.regularizer),
            tf.keras.layers.MaxPool2D(
                pool_size=(2, 2), strides=2, padding='valid'),
            tf.keras.layers.Conv2D(
                filters=64, kernel_size=(4,1), strides=1, activation='relu', kernel_regularizer=self.regularizer),
            tf.keras.layers.MaxPool2D(
                pool_size=(2, 1), strides=1, padding='valid'),
            tf.keras.layers.Flatten(),

            tf.keras.layers.Dense(124, kernel_regularizer=self.regularizer),

            tf.keras.layers.Dropout(dropout_rate),
            # No activation
            tf.keras.layers.Dense(latent_dim + latent_dim, kernel_regularizer=self.regularizer),
        ]
    )

    self.decoder = tf.keras.Sequential(
        [
            tf.keras.layers.InputLayer(input_shape=(latent_dim,)),
            tf.keras.layers.Dropout(dropout_rate),
            tf.keras.layers.Dense(units=shape_of_input[0]*shape_of_input[1], activation=tf.nn.relu),
            tf.keras.layers.Reshape(target_shape=(shape_of_input[0], shape_of_input[1],1)),
            # tf.keras.layers.UpSampling2D(size=(2, 1)),
            tf.keras.layers.Conv2DTranspose(
                filters=64, kernel_size=(4,1), strides=1, padding='same',
                activation='relu',kernel_regularizer=self.regularizer),
            # tf.keras.layers.UpSampling2D(size=(2, 2)),
            tf.keras.layers.Conv2DTranspose(
                filters=32, kernel_size=(4,1), strides=1, padding='same',
                activation='relu', kernel_regularizer=self.regularizer),
            # No activation
            tf.keras.layers.Conv2DTranspose(
                filters=1, kernel_size=1, strides=1, padding='same'),
        ]
    )

  @tf.function
  def sample(self, eps=None):
    if eps is None:
      eps = tf.random.normal(shape=(100, self.latent_dim))
    return self.decode(eps, apply_sigmoid=True)

  def encode(self, x):
    return self.encode(x)

  def reparameterize(self, mean, logvar):
    eps = tf.random.normal(shape=mean.shape)
    return eps * tf.exp(logvar * .5) + mean

  def decode(self, z, apply_sigmoid=False):
    logits = self.decoder(z)
    if apply_sigmoid:
      probs = tf.sigmoid(logits)
      return probs
    return logits
