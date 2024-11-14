import geopandas as gpd
import folium
import webbrowser
import os
import tempfile

# Load the GeoJSON data directly from the URL
geo_df = gpd.read_file('http://geo.rv.ua/api-user/geojson/9118925304098502.json')

# Initialize a Folium map centered on Ukraine (approximate coordinates for Kyiv)
m = folium.Map(location=[48.3794, 31.1656], zoom_start=6)

# Optional: Add a layer control to toggle layers
folium.LayerControl().add_to(m)

# Save the map temporarily in a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
    tmpfile.write(m._repr_html_().encode())
    tmpfile.close()

    # Open the map in the default web browser
    webbrowser.open(f'file://{tmpfile.name}')
    
    print(f"Map is now open in your browser: {tmpfile.name}")
