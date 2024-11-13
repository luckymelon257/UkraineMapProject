import folium
from pyrosm import OSM
from flask import Flask, render_template_string
import os

# Specify the path to the Geofabrik PBF file
pbf_file = "path/to/ukraine-latest.osm.pbf"

# Load data using Pyrosm
osm = OSM(pbf_file)
buildings = osm.get_buildings()
roads = osm.get_network("driving")

# Create a Folium map centered on a location
map_center = [50.450001, 30.523333]  # Kyiv, Ukraine
map = folium.Map(location=map_center, zoom_start=10)

folium.GeoJson(buildings).add_to(map)
folium.GeoJson(roads).add_to(map)

# Save the map HTML as a string instead of a file
map_html = map._repr_html_()

# Initialize Flask
app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML map directly
    return render_template_string(map_html)

# Run Flask app
if __name__ == "__main__":
    print("Serving the map at http://127.0.0.1:5000")
    app.run(debug=True)
