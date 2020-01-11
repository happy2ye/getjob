import numpy as np
import matplotlib.pylab as plt

# x is sum of b + w1x1 + w2x2. Therefore, x returns the sum of signals, and this value decide whether neuron be actived

def stepFunction(x):
  y = x > 0
  return y.astype(np.int)

def sigmoid(x):
  return 1 / (1 +np.exp(-x))

def relu(x):
  return np.maximum(0, x)

