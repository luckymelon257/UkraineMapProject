import plotly.express as px
import geopandas as gpd
import osmnx as ox

# Retrieve the boundaries for Ukraine
ukraine = ox.geocode_to_gdf('Ukraine')

# Create a Plotly map with enhanced UI
fig = px.choropleth_mapbox(
    ukraine,
    geojson=ukraine.geometry,
    locations=ukraine.index,
    color_discrete_sequence=["#0077b6"],  # Custom color for Ukraine
    mapbox_style="carto-positron",        # Cleaner style for better UI
    center={"lat": 48.3794, "lon": 31.1656},
    zoom=5,
    opacity=0.1,                           # Adjust transparency for a softer look
)

# Update layout for focused UI
fig.update_layout(
    title="Interactive Map of Ukraine",
    mapbox={"center": {"lat": 48.3794, "lon": 31.1656}, "zoom": 5},
    margin={"r":0, "t":0, "l":0, "b":0},  # Remove margins for full-screen map
    showlegend=False,                     # Remove legend for a cleaner look
)

fig.show()
