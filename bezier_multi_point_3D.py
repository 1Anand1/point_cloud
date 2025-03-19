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
  t_list=np.linspace(0,1,100)

  x_terms=[((1-t)**(n-i)*t**i*comb(n,i)*x_points[i] for i in range(n+1)) for t in t_list]


  return x_terms

# Defining a function to create a Bezier Curve
# def bezier_curve(t):
#   term=comb(n,i)

# x**3+3*x**2*y+3*x*y**2+y**3
print(bezier_curve(rand_points))