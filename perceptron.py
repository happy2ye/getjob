import numpy as np
# w - weight, b - bias, w&b can be any combination to achieve the gate logic, here is 0.5 and 0.2
def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  temp = np.sum(w*x) + b
  if temp <= 0:
    return 0
  else:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  temp = np.sum(w*x) + b
  if temp <= 0:
    return 0
  else:
    return 1
 
def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  temp = np.sum(w*x) + b
  if temp <= 0:
    return 0
  else:
    return 1

def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y

