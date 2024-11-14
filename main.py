import geopandas as gpd
import folium

# Load the GeoJSON data directly from the URL
geo_df = gpd.read_file('http://geo.rv.ua/api-user/geojson/9118925304098502.json')

# Initialize a Folium map centered on Ukraine (approximate coordinates for Kyiv)
m = folium.Map(location=[48.3794, 31.1656], zoom_start=6)

# Optional: Add a layer control to toggle layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file and display it
m.save("ukraine_map.html")
print("Map saved as 'ukraine_map.html'")
