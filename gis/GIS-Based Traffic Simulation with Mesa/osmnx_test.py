import osmnx as ox
import shapely
import os

# Print osmnx and shapely versions
print(f"osmnx version: {ox.__version__}\nshapely version: {shapely.__version__}")
print(f"Full Python build information: {os.popen('python -V').read()}")

# Bounding box coordinates for Bangalore
north, south, east, west = (
    12.976,
    12.961,
    77.599,
    77.579,
)  # Adjusted coordinates for Bangalore

# Update bounding box to follow the new order (left, bottom, right, top)
# GeoPandas >= 2.0 is required!
bbox = (77.579, 12.961, 77.599, 12.976)  # west, south, east, north

G = ox.graph_from_bbox(bbox, network_type="drive")
