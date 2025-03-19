# Importing the required libraries
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from math import comb

# Generating some random 3D points
rand_points=np.random.randint(10,200,(20,3))

# Defining a function to create a Bezier Curve
def bezier_curve(points:np.ndarray)->None:
  x_points=points[:,0]
  y_points=points[:,1]
  z_points=points[:,2]

  n=len(points)
  t=np.linspace(0,1,100)
  x=[(comb(n,i) for i in range(points.shape[0]+1))]

  return x

print(bezier_curve(rand_points))