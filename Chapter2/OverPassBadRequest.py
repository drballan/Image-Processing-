import overpy


# Create an Overpass API object
api = overpy.Overpass()


# Define the bounding box coordinates
bbox = [54.6710, -5.9382, 54.6556, -5.8922]


# Define the query to retrieve data within the bounding box
query = f"""
    node({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
    out;
"""


# Query the data within the bounding box
result = api.query(query)


# Iterate over the nodes
for node in result.nodes:
    print(node.id)


# Get the name of a node
if result.nodes:
    node = result.nodes[0]
    name = node.tags.get('name', 'N/A')
    print(name)
