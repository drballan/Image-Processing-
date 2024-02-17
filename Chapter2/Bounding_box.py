import overpy


# Get all the roads in a bounding box
bbox = [40.7127837, -74.0059413, 40.7130811, -74.0044444]
query = overpy.Overpass(bbox=bbox, highway='road')
response = query.get_response()


# Iterate over the roads
for road in response.ways:
    print(road.id)
