# Importing required function
from object_creator import func_to_create_object

# Importing the required libraries
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
# Creating the numpy array of 2D or 3D shape
object_to_plot=func_to_create_object(1000,-100,100,True)


def noise_addition(array_to_distort:np.ndarray)->np.ndarray: 

  # Extracting the shape of the array that we need to distort
  rqd_shape=array_to_distort.shape

  # Creating some noise :) 
  noise=np.random.normal(1,10,rqd_shape)

  # Adding the noise in the parent array
  distored_array=array_to_distort+noise

  # scaling the array for further distorting it
  scaling=np.array([1.2,0.75,15]) 

# Adding the scaling in the distorted array
  distored_array=distored_array*scaling

  return distored_array


def plot_graph(points:np.ndarray)->None:
  """
  This function will plot the 2D or 3D array

  args:
    2D or 3D array will be passed as an argument to this function

  """
  # If the number of columns is not 2 or 3 then value error will be raised
  if points.shape[1] not in [2,3]:
    raise ValueError(" The numpy array has to be of shape 2D or 3D ")
  
  # If 2 columns are available then a 2D graph will be created
  elif points.shape[1]==2: 
    fig=px.scatter(
      x=points[:,0], # Adding X axis coordinates
      y=points[:,1],  # Adding Y axis coordinates
      )
    
    # Updating the traces
    fig.update_traces(
      marker=dict(opacity=0.5,colorscale='Viridis',size=5,color=points[:,0])
    )

    # Updating the layout
    fig.update_layout(title='2D Plot',scene=dict(xaxis_title='X_Axis',yaxis_title='Y_Axis'))
    fig.show()

  # If 3 columns are available then a 3D graph will be created
  elif points.shape[1]==3: 
    # Calling the figure method
    fig=go.Figure()

    # Mapping the graphs as per the requirement
    fig.add_trace(go.Scatter3d(
        x=points[:,0], # Adding X axis coordinates
        y=points[:,1], # Adding Y axis coordinates
        z=points[:,2], # Adding Z axis coordinates
        mode='markers',
        marker=dict(color=points[:,2],opacity=0.5,colorscale='Viridis',size=5) # Changing the marker dimensions
        ))

    #Updating the layout
    fig.update_layout(title='3D Plot',scene=dict(xaxis_title='X_Axis',yaxis_title='Y_Axis',zaxis_title='Z_Axis')) # Adding labels to the graph
    fig.show()

# Distorting & scaling the object to be plotted
object_to_plot=noise_addition(object_to_plot)

# Plotting the graph
plot_graph(object_to_plot)
