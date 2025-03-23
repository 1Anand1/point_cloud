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

  # Extracting the points
  x_points=points[:,0]
  y_points=points[:,1]
  z_points=points[:,2]

  # Checking the number of fixed points on the Bezier curve 
  n=len(points)-1 # This is the degree of the curve 
  t_list=np.linspace(0,1,points_on_bezier)

  x=[sum((comb(n,i))*((1-t)**(n-i))*(t**i)*x_points[i] for i in range(n+1)) for t in t_list]
  y=[sum((comb(n,i))*((1-t)**(n-i))*(t**i)*y_points[i] for i in range(n+1)) for t in t_list]
  z=[sum((comb(n,i))*((1-t)**(n-i))*(t**i)*z_points[i] for i in range(n+1)) for t in t_list]
  

  return np.array(x)


print(bezier_curve(rand_points,10))