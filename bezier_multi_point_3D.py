import numpy as np
import plotly.graph_objects as go
from math import comb
random_points=np.random.randint(0,10,(4,3))
def bezier_curve(points:np.array,control_points:int)->None:
  """
  This function is used to generate a Bezier Curve in 3D for multiple control points

  *args:
    points: The control and the fixed points for the Bezier curve are to be specified
    points_on_bezier : The points on the curve which will created by the binomial equation are to be specified

  returns:
    None (Produces a graph for the Bezier curve)
  """
  # Extracting the coordinates of the points 
  x_points=points[:,0]
  y_points=points[:,1]
  z_points=points[:,2]

  # Creating the control points
  t_list=np.linspace(0,1,control_points)

  # Checking length of the points array & getting the degree of the curve
  n=len(points) - 1

  # Making Bernstein Basis
  berstenian_basis=np.array([(comb(n,i))*((1-t_list)**(n-i)*(t_list**i)) for i in range(n+1)]) # Here I did n+1 because the number of points is degree of curve + 1
  
  # Getting the curve points
  x_curve=np.dot(berstenian_basis.T , x_points)
  y_curve=np.dot(berstenian_basis.T , y_points)
  z_curve=np.dot(berstenian_basis.T , z_points)

  # Plotting the curve
  fig=go.Figure()
  fig.add_trace(go.Scatter3d(x=x_curve,y=y_curve,z=z_curve,mode='lines',name='Bezier Curve'))
  fig.add_trace(go.Scatter3d(x=x_points,y=y_points,z=z_points,mode='markers',name='Control Points',marker=dict(size=5,color='red')))
  fig.show()

bezier_curve(random_points,9999)