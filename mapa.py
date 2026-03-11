import folium
from folium.plugins import MarkerCluster

# Crear mapa profesional BLANCO
mapa = folium.Map(
    location=[18.2208, -66.5901],
    zoom_start=9,
    tiles="CartoDB positron"
)

# Crear mapa profesional OSCURO
# mapa = folium.Map(
#     location=[18.2208, -66.5901],
#     zoom_start=9,
#     tiles="CartoDB dark_matter"
# )

# Agregar cluster (importante si tendrás muchas propiedades)
marker_cluster = MarkerCluster().add_to(mapa)

# Propiedades mejoradas
propiedades = [
    {
        "nombre": "Paseo Caribe",
        "localizacion": "Condado, PR",
        "lat": 18.462101073029388,
        "lon": -66.0855394647402,
        "descripcion": "Paseo Caribe is a dream come true with a blend of retail, restaurants,"
        " personal services, and workspaces.  Paseo Caribe offers shared office spaces with short "
        "and long-term leasing available (hourly or monthly). These state-of-the-art shared office"
        " spaces range from 165 sq. ft. to 500 sq. ft. and are conceptualized to promote collaboration"
        " and the flow of ideas, while still helping maintain privacy. This oceanfront oasis for "
        "entertainment, shopping, and workspaces is an ideal hub for people to dream. Paseo Caribe "
        "is a 120,000 sq ft vibrant space to socialize, connect, and inspire you with its stunning"
        " oceanfront views. Steps away from 475 residential units, 250 hotel rooms, and hundreds "
        "of restaurants, retails, and attractions all around Condado, Isla Verde, and the hot spots"
        " of San Juan.",
        "imagen": "https://static.wixstatic.com/media/c9ce2e_f78f0edf0b424fc8ae3457cb3750a6a3~mv2.jpg/v1/crop/x_0,y_0,w_1977,h_1600/fill/w_700,h_566,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/PaseoCaribe5_LOW.jpg",
        "link": "https://images.search.yahoo.com/search/images;_ylt=AwrFGRAFcKhpPgIAQn1XNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3Nj?p=PASEO+CARIBE&fr=mcafee"
    },
    {
        "nombre": "Dorado Property",
        "localizacion": "Dorado, PR",
        "lat": 18.4588,
        "lon": -66.2677,
        "descripcion": "Casa moderna con piscina y acceso privado.",
        "imagen": "https://via.placeholder.com/250",
        "link": "https://lasbrisasproperty.com/property2"
    }
]

for prop in propiedades:

    html_popup = f"""
    <div style="width:250px">
        <h3>{prop['nombre']}</h3>
        <h4>{prop['localizacion']}</h4>
        <img src="{prop['imagen']}" width="100%" style="border-radius:8px;">
        <p>{prop['descripcion']}</p>
        <a href="{prop['link']}" target="_blank" 
           style="background-color:#0d6efd;
                  color:white;
                  padding:6px 10px;
                  text-decoration:none;
                  border-radius:5px;">
           Ver Propiedad
        </a>
    </div>
    """

    iframe = folium.IFrame(html=html_popup, width=270, height=350)
    popup = folium.Popup(iframe, max_width=300)

    folium.Marker(
        location=[prop["lat"], prop["lon"]],
        popup=popup,
        icon=folium.Icon(color="blue", icon="home", prefix="fa")
    ).add_to(marker_cluster)

mapa.save("mapa_las_brisas.html")

print("Mapa profesional generado correctamente.")