# Importing the required libraries
import numpy as np

# Defining a function to create a 2D or 3D numpy array of X,Y,Z Coordinates
def func_to_create_object(n:int,low_range:int,high_range:int,z=True)->np.array:
  """
  This is the function that creates a numpy array of shape (n,2) or (n,3)

  args :
    n parameter --> Number of data points
    low_range parameter --> Tells about the lower range in which the numbers will be distributed
    high_range parameter --> Tells about the higher range in which the numbers will be distributed
    z parameter --> If this parameter is True then a 3D array will be created, if False then it will create a 2D array

  returns :
    It returns a 2D or 3D array 
  
  """

  # Making a sorted numpy array of x
  x_range=np.sort(np.random.uniform(low_range,high_range,n))
  y_range=x_range**2 # Making y a square of x array

  # If z is set True then z array will be created
  if z==True:
    z_range=x_range**3 # Making z a cube of x array
    rqd_array=np.stack((x_range,y_range,z_range),axis=1) # Stacking the x , y & z arrays
  else:
    rqd_array=np.stack((x_range,y_range),axis=1) # Stacking the x & y arrays only

  return rqd_array
