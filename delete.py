import numpy as np

x = 1
y = 10
ar = np.linspace(x, y, 9)
print(ar)

def tttt(a, b):
  z = (a+b)/2
  return round(z, 4)
res = tttt(x, y)
print(res)
