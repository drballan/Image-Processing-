import overpy
import folium

# Get the coordinates of the location where the picture was taken
latitude = 40.712938
longitude = -74.005235

# Save the picture to a file
picture_path = 'cat.png'

# Create a map of the location
map = folium.Map(location=[latitude, longitude])

# Place the picture on the map at the coordinates of the picture
image_overlay = folium.ImageOverlay(picture_path, name='Cat',
                                   bounds=[[latitude - 0.001, longitude - 0.001],
                                            [latitude + 0.001, longitude + 0.001]])
map.add_child(image_overlay)

# Save the map
map.save('map.html')
