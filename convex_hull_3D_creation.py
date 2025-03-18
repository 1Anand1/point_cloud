# Importing the required libraries
import numpy as np

import plotly.graph_objects as go
from scipy.spatial import ConvexHull

# Making a 3D numpy array
# np.random.seed(42) # Uncomment it if the same points are to be plotted everytime
rand_int=np.random.randint(0,50,(100,3))

# Making a hull object
hull=ConvexHull(rand_int)

# Plotting the graph of the points
scatter=go.Scatter3d(x=rand_int[:,0],
                     y=rand_int[:,1],
                     z=rand_int[:,2],
                     mode='markers',
                     marker=dict(color='red',size=3))

# Initializing empty list for capturing boundry faces
hull_faces=[]

# Adding the boundry faces in hull faces list
for simplex in hull.simplices:
  hull_faces.append(go.Mesh3d(x=rand_int[simplex,0],
                              y=rand_int[simplex,1],
                              z=rand_int[simplex,2],
                              color='green',
                              opacity=1))



# Converting the scatter in a list and then adding hull faces with scatter & then plotting the 3D graph
fig=go.Figure([scatter]+hull_faces)
fig.show()