# Importing Libraries
import numpy as np
import plotly.graph_objects as go 
import matplotlib.pyplot as plt

# Creating a random 3 points -> 2 fixed and 1 control point
rqd_points=np.random.randint(0,100,(3,2))

# Extracting the points p1 & p3 --> fixed & p2 is control point
p1=rqd_points[0]
p2=rqd_points[1]
p3=rqd_points[2]

def bezier_curve(pt1:np.ndarray,pt2:np.ndarray,pt3:np.ndarray)->tuple[np.ndarray]:

  """
  This function will plot a 2D Bezier curve

  *args:
    2 Fixed points --> P1 & P3 , 1 control point --> P2 

  returns:
    Tuple of the numpy arrays that are to be plotted
  """

  # Different values of t are stored in a list
  list_t=np.linspace(0,1,100)

  # Plotting x & y coordinates of the Bezier curve for different values of t
  x=[(1-t)**2*pt1[0]+2*(1-t)*t*pt2[0]+t**2*pt3[0] for t in list_t]
  y=[(1-t)**2*pt1[1]+2*(1-t)*t*pt2[1]+t**2*pt3[1] for t in list_t]

  return x,y

# Calling the function & then performing tuple unpacking
X,Y=bezier_curve(p1,p2,p3)

# Plotting the graph
plt.plot(X,Y,color='green') # Plotting a Bezier curve 
plt.scatter(x=rqd_points[:,0],y=rqd_points[:,1],color='red') # Plotting the fixed points & the control point
plt.show()