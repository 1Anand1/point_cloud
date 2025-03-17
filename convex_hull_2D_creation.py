import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Generating random points
# np.random.seed(42) # This comment can be activated if we want different random points everytime
random_points=np.random.rand(20,2) # Creating 100 random points

def convex_2d_hull(points:np.ndarray)->None:

  """
  This function is used to create a convex hull --> More importantly the boundry points will be identified

  *args:
    a 2D numpy array has to be passed in

  returns:
    None , but plots the graph of the 2D points along with convex hull boundry points & a line passing through them.
  """

  # Defining the coordinates to plot
  X=points[:,0]
  Y=points[:,1]

  # Initialising the Convex Hull Object
  hull=ConvexHull(points)

  # Now plotting the graph
  plt.scatter(x=X,y=Y)

  # Plotting the convex hull
  for simplex in hull.simplices:
    plt.plot(points[simplex,0],points[simplex,1],'-r',linewidth=1)

  # Mapping other aesthetic requirements for the graph
  plt.legend()
  plt.title('2D Scatter Plot with Convex Hull')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.tight_layout()
  plt.show()

# Calling the function to plot the 2D points and the convex hull boundry points
convex_2d_hull(random_points)