import folium

# Centro en Puerto Rico
mapa = folium.Map(location=[18.2208, -66.5901], zoom_start=9)

# Ejemplo propiedades
propiedades = [
    {"nombre": "Condado Property", "lat": 18.4655, "lon": -66.1057},
    {"nombre": "Dorado Property", "lat": 18.4588, "lon": -66.2677},
]

for prop in propiedades:
    folium.Marker(
        location=[prop["lat"], prop["lon"]],
        popup=prop["nombre"],
        icon=folium.Icon(color="blue", icon="home")
    ).add_to(mapa)

mapa.save("mapa_las_brisas.html")

print("Mapa generado correctamente.")
