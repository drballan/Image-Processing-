import overpy
import folium

# Get the coordinates of the location where the picture was taken
latitude = 40.712938
longitude = -74.005235

# Create a map of the location
map = folium.Map(location=[latitude, longitude])

# Place a marker on the map at the coordinates of the picture
marker = folium.Marker([latitude, longitude], popup='This is where the picture was taken!')
map.add_child(marker)

# Save the map
map.save('map.html')
