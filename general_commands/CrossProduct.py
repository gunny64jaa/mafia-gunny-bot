import numpy as np
def cross(t):
  x,y=[i for i in t.split('x')]
  x=[float(i) for i in x.split(',')]
  y=[float(i) for i in y.split(',')]
  return (np.cross(x, y))