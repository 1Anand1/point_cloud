# Importing required libraries
import numpy as np
import plotly.graph_objects as go

# Generating points and direction
np.random.seed(42)
random_point=np.random.randint(1,5,(1,3))
direction=np.random.randint(1,3,(1,3))

# Range in which the points are to be spread for the given line
range_of_points=np.linspace(-10,10,10)
range_of_points=range_of_points[:,np.newaxis]


# Making the line
line_through_points=(random_point)+(direction*range_of_points)

# Plotting the graph
fig=go.Figure()

fig.add_traces(go.Scatter3d(x=line_through_points[:,0],
                            y=line_through_points[:,1],
                            z=line_through_points[:,2],
                            mode='lines',
                            name='Line'))

fig.add_traces(go.Scatter3d(x=random_point[:,0],
                            y=random_point[:,1],
                            z=random_point[:,2],
                            mode='markers',
                            marker=dict(color='red',size=5),
                            name='Point'))
fig.show()