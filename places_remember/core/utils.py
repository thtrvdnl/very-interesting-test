import folium

def add_map() -> folium.Map:
    map = folium.Map(
        width=800,
        height=500,
        location=[56.8519, 60.6122],
        tiles='Stamen Terrain',
        zoom_start=13
    )
    map.add_child(folium.ClickForMarker(popup='Waypoint'))
    return map._repr_html_()