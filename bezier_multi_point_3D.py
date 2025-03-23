# Importing the required libraries
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from math import comb

# Generating some random 3D points
rand_points=np.random.randint(10,200,(20,3))

# Defining a function to create a Bezier Curve
def bezier_curve(points:np.ndarray,points_on_bezier:int)->None:
  """
  This function is used to generate a Bezier Curve in 3D for multiple control points

  *args:
    points: The control and the fixed points for the Bezier curve are to be specified
    points_on_bezier : The points on the curve which will created by the binomial equation are to be specified

  returns:
    None (Produces a graph for the Bezier curve)
  """



  x_points=points[:,0]
  y_points=points[:,1]
  z_points=points[:,2]

  n=len(points)
  t_list=np.linspace(0,1,points_on_bezier)



  return x_terms

# Defining a function to create a Bezier Curve
# def bezier_curve(t):
#   term=comb(n,i)

# x**3+3*x**2*y+3*x*y**2+y**3
print(bezier_curve(rand_points))