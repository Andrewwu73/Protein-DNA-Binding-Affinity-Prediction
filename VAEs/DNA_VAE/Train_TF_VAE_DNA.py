import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from TF_VAE_DNA import CVAE
import datetime as time
from generate_dna_onehot import obtainDNAData
import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)

'''
Sourced from Tensorflow's tutorial on VAEs.
'''
optimizer = tf.keras.optimizers.Adam(1e-3)
def log_normal_pdf(sample, mean, logvar, raxis=1):
  log2pi = tf.math.log(2. * np.pi)
  return tf.reduce_sum(
      -.5 * ((sample - mean) ** 2. * tf.exp(-logvar) + logvar + log2pi),
      axis=raxis)


def compute_loss(model, x):
  mean, logvar = model.encode(x)
  z = model.reparameterize(mean, logvar)
  x_logit = model.decode(z)
  cross_ent = tf.nn.sigmoid_cross_entropy_with_logits(logits=x_logit, labels=x)  #Try alternate loss functions, maybe interesting ones that penalize large mutations rather than small mutations
  logpx_z = -tf.reduce_sum(cross_ent, axis=[1, 2, 3])
  logpz = log_normal_pdf(z, 0., 0.)
  logqz_x = log_normal_pdf(z, mean, logvar)
  return -tf.reduce_mean(logpx_z + logpz - logqz_x)


@tf.function
def train_step(model, x, optimizer):
  """Executes one training step and returns the loss.

  This function computes the loss and gradients, and uses the latter to
  update the model's parameters.
  """
  with tf.GradientTape() as tape:
    loss = compute_loss(model, x)
  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))

# dataset_directory = "../../Datasets/Protein-DNA Complex/DNADataset.csv"
dataset_directory = "../../Datasets/FinalDatasets/5SpeciesDNA.csv"
dna_dataset_obtainer = obtainDNAData(dataset_directory)
# train_dataset, test_dataset = dna_dataset_obtainer.obtainData()
# train_dataset = tf.cast(tf.convert_to_tensor(train_dataset), dtype=tf.float32)
# test_dataset = tf.cast(tf.convert_to_tensor(test_dataset), dtype=tf.float32)

# print(train_dataset[0].shape)
# print(train_dataset.shape)
# print(test_dataset.shape)

# train_dataset = tf.expand_dims(train_dataset, axis=3)
# test_dataset = tf.expand_dims(test_dataset, axis=3)

# print(train_dataset[-20])
# print(train_dataset[-19])

# train_dataset = []#TODO 100x4 for one hot encoding of DNA sequence, pad 0s to make sure have space for longest DNA sequence
# shape_of_input = tf.expand_dims(train_dataset[0], axis=2)
# shape_of_input = tf.expand_dims(shape_of_input, axis=3)
# shape_of_input = train_dataset[0].shape
# print(shape_of_input)
def train(epochs = 50, latent_dim=32, reg_coeff = 0.0001, dropout_rate = 0):
    model = CVAE(latent_dim, shape_of_input, reg_coeff, dropout_rate)
    for epoch in range(1, epochs + 1):
      start_time = time.datetime.now()
      for train_x in train_dataset:
        # shape_of_inputx = tf.expand_dims(train_x, axis=2)
        shape_of_inputx = tf.expand_dims(train_x, axis=0)
        train_step(model, shape_of_inputx, optimizer)
      end_time = time.datetime.now()

      loss = tf.keras.metrics.Mean()
      for test_x in test_dataset:
        # shape_of_inputtest = tf.expand_dims(test_x, axis=2)
        shape_of_inputtest = tf.expand_dims(test_x, axis=0)
        loss(compute_loss(model, shape_of_inputtest))
      elbo = -loss.result()
      # display.clear_output(wait=False)
      print('Epoch: {}, Test set ELBO: {}, time elapse for current epoch: {}'
            .format(epoch, elbo, end_time - start_time))
    model.save_weights('dna_model_updated')
    return model

# hypers = {"latent_dim": [16, 32, 64, 128], "reg_coeff": [0.0001, 0.00001, 0.00005], "dropout_rate": [0.01, 0.001, 0.0001]}
# for l in range(3):
#     for r in range(3):
#         for d in range(3):
#             print("\n\nNew Epoch:\n\n")
#             latent = hypers["latent_dim"][l]
#             reg = hypers["reg_coeff"][r]
#             drop = hypers["dropout_rate"][d]
#             print('Latent Dimension: {}, Reg Coeff: {}, Dropout Rate: {}'
#                   .format(latent, reg, drop))
# trained = train(latent_dim=64, reg_coeff=0.00005, dropout_rate=0.001)
# model = CVAE(64, (500, 4, 1), 0.00005, 0.001)
# model.load_weights("dna_model")
model = CVAE(64, (500, 4, 1), 0.00005, 0.001)
model.load_weights("dna_model")
# # list = model.layers
# # print(list[-1].weights)
# print("This is the first sample")
# sample = test_dataset[20]
# shape_of_inputx = tf.expand_dims(sample, axis=2)
# shape_of_inputx = tf.expand_dims(shape_of_inputx, axis=0)
# encoded = model.encode(shape_of_inputx)
# decoded = model.decode(encoded[0])
# print(sample)
# print(decoded[0:2])
# print("This is the second sample")
# sample = test_dataset[40]
# shape_of_inputx = tf.expand_dims(sample, axis=2)
# shape_of_inputx = tf.expand_dims(shape_of_inputx, axis=0)
# encoded = model.encode(shape_of_inputx)
# decoded = model.decode(encoded[0])
# print(sample)
# print(decoded[0:2])
# decoded = tf.reshape(decoded, [-1])
# print(decoded.shape)
# print(encoded.shape)
# print(tf.argmax(decoded, axis=2))
# print(decoded.numpy)
# print(sample)

lengths, test_dataset = dna_dataset_obtainer.getSequenceLengthData()
test_dataset = tf.cast(tf.convert_to_tensor(test_dataset), dtype=tf.float32)
test_dataset = tf.expand_dims(test_dataset, axis=3)

print(len(lengths))
print(len(test_dataset))

num = 1000
samples = test_dataset[0:num]
lat = model.encode(samples)
ret = model.decode(lat)
#print(tf.math.argmax(ret[0:1], axis = 2))
#print(tf.math.argmax(samples[0:1], axis = 2))
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
