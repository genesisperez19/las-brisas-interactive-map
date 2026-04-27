# # import folium
# # from folium.plugins import MarkerCluster

# # # Crear mapa profesional BLANCO
# # mapa = folium.Map(
# #     location=[18.2208, -66.5901],
# #     zoom_start=9,
# #     tiles="CartoDB positron"
# # )

# # # Crear mapa profesional OSCURO
# # # mapa = folium.Map(
# # #     location=[18.2208, -66.5901],
# # #     zoom_start=9,
# # #     tiles="CartoDB dark_matter"
# # # )

# # # Agregar cluster (importante si tendrás muchas propiedades)
# # marker_cluster = MarkerCluster().add_to(mapa)

# # propiedades = read_excel("properties.xlsx")

# # # Propiedades mejoradas
# # propiedades = [
# #     {
# #         "nombre": "Paseo Caribe",
# #         "localizacion": "Condado, PR",
# #         "lat": 18.462101073029388,
# #         "lon": -66.0855394647402,
# #         "descripcion": "Paseo Caribe is a dream come true with a blend of retail, restaurants,"
# #         " personal services, and workspaces.  Paseo Caribe offers shared office spaces with short "
# #         "and long-term leasing available (hourly or monthly). These state-of-the-art shared office"
# #         " spaces range from 165 sq. ft. to 500 sq. ft. and are conceptualized to promote collaboration"
# #         " and the flow of ideas, while still helping maintain privacy. This oceanfront oasis for "
# #         "entertainment, shopping, and workspaces is an ideal hub for people to dream. Paseo Caribe "
# #         "is a 120,000 sq ft vibrant space to socialize, connect, and inspire you with its stunning"
# #         " oceanfront views. Steps away from 475 residential units, 250 hotel rooms, and hundreds "
# #         "of restaurants, retails, and attractions all around Condado, Isla Verde, and the hot spots"
# #         " of San Juan.",
# #         "imagen": "https://static.wixstatic.com/media/c9ce2e_f78f0edf0b424fc8ae3457cb3750a6a3~mv2.jpg/v1/crop/x_0,y_0,w_1977,h_1600/fill/w_700,h_566,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/PaseoCaribe5_LOW.jpg",
# #         "link": "https://images.search.yahoo.com/search/images;_ylt=AwrFGRAFcKhpPgIAQn1XNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3Nj?p=PASEO+CARIBE&fr=mcafee"
# #     },
# #     {
# #         "nombre": "Dorado Property",
# #         "localizacion": "Dorado, PR",
# #         "lat": 18.4588,
# #         "lon": -66.2677,
# #         "descripcion": "Casa moderna con piscina y acceso privado.",
# #         "imagen": "https://via.placeholder.com/250",
# #         "link": "https://lasbrisasproperty.com/property2"
# #     }
# # ]

# # for prop in propiedades:

# #     html_popup = f"""
# #     <div style="width:250px">
# #         <h3>{prop['nombre']}</h3>
# #         <h4>{prop['localizacion']}</h4>
# #         <img src="{prop['imagen']}" width="100%" style="border-radius:8px;">
# #         <p>{prop['descripcion']}</p>
# #         <a href="{prop['link']}" target="_blank" 
# #            style="background-color:#0d6efd;
# #                   color:white;
# #                   padding:6px 10px;
# #                   text-decoration:none;
# #                   border-radius:5px;">
# #            Ver Propiedad
# #         </a>
# #     </div>
# #     """

# #     iframe = folium.IFrame(html=html_popup, width=270, height=350)
# #     popup = folium.Popup(iframe, max_width=300)

# #     folium.Marker(
# #         location=[prop["lat"], prop["lon"]],
# #         popup=popup,
# #         icon=folium.Icon(color="blue", icon="home", prefix="fa")
# #     ).add_to(marker_cluster)

# # mapa.save("mapa_las_brisas.html")

# # print("Mapa profesional generado correctamente.")

# import folium
# from folium.plugins import MarkerCluster

# # Crear mapa profesional BLANCO
# mapa = folium.Map(
#     location=[18.2208, -66.5901],
#     zoom_start=9,
#     tiles="CartoDB positron"
# )

# # Crear mapa profesional OSCURO
# # mapa = folium.Map(
# #     location=[18.2208, -66.5901],
# #     zoom_start=9,
# #     tiles="CartoDB dark_matter"
# # )

# # Agregar cluster (importante si tendrás muchas propiedades)
# marker_cluster = MarkerCluster().add_to(mapa)

# propiedades = read_excel("properties.xlsx")

# # Propiedades mejoradas
# propiedades = [
#     {
#         "nombre": "Paseo Caribe",
#         "localizacion": "Condado, PR",
#         "lat": 18.462101073029388,
#         "lon": -66.0855394647402,
#         "descripcion": "Paseo Caribe is a dream come true with a blend of retail, restaurants,"
#         " personal services, and workspaces.  Paseo Caribe offers shared office spaces with short "
#         "and long-term leasing available (hourly or monthly). These state-of-the-art shared office"
#         " spaces range from 165 sq. ft. to 500 sq. ft. and are conceptualized to promote collaboration"
#         " and the flow of ideas, while still helping maintain privacy. This oceanfront oasis for "
#         "entertainment, shopping, and workspaces is an ideal hub for people to dream. Paseo Caribe "
#         "is a 120,000 sq ft vibrant space to socialize, connect, and inspire you with its stunning"
#         " oceanfront views. Steps away from 475 residential units, 250 hotel rooms, and hundreds "
#         "of restaurants, retails, and attractions all around Condado, Isla Verde, and the hot spots"
#         " of San Juan.",
#         "imagen": "https://static.wixstatic.com/media/c9ce2e_f78f0edf0b424fc8ae3457cb3750a6a3~mv2.jpg/v1/crop/x_0,y_0,w_1977,h_1600/fill/w_700,h_566,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/PaseoCaribe5_LOW.jpg",
#         "link": "https://images.search.yahoo.com/search/images;_ylt=AwrFGRAFcKhpPgIAQn1XNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3Nj?p=PASEO+CARIBE&fr=mcafee"
#     },
#     {
#         "nombre": "Dorado Property",
#         "localizacion": "Dorado, PR",
#         "lat": 18.4588,
#         "lon": -66.2677,
#         "descripcion": "Casa moderna con piscina y acceso privado.",
#         "imagen": "https://via.placeholder.com/250",
#         "link": "https://lasbrisasproperty.com/property2"
#     }
# ]

# for prop in propiedades:

#     html_popup = f"""
#     <div style="width:250px">
#         <h3>{prop['nombre']}</h3>
#         <h4>{prop['localizacion']}</h4>
#         <img src="{prop['imagen']}" width="100%" style="border-radius:8px;">
#         <p>{prop['descripcion']}</p>
#         <a href="{prop['link']}" target="_blank" 
#            style="background-color:#0d6efd;
#                   color:white;
#                   padding:6px 10px;
#                   text-decoration:none;
#                   border-radius:5px;">
#            Ver Propiedad
#         </a>
#     </div>
#     """

#     iframe = folium.IFrame(html=html_popup, width=270, height=350)
#     popup = folium.Popup(iframe, max_width=300)

#     folium.Marker(
#         location=[prop["lat"], prop["lon"]],
#         popup=popup,
#         icon=folium.Icon(color="blue", icon="home", prefix="fa")
#     ).add_to(marker_cluster)

# mapa.save("mapa_las_brisas.html")

# print("Mapa profesional generado correctamente.")

import folium
from folium.plugins import MarkerCluster
import pandas as pd
import os

# Leer Excel
df = pd.read_excel("properties.xlsx")

# Crear mapa
mapa = folium.Map(
    location=[18.2208, -66.5901],
    zoom_start=9,
    tiles="CartoDB positron"
)

marker_cluster = MarkerCluster().add_to(mapa)

# Formatear nombre de carpeta
import re

def format_folder_name(nombre):
    # Cortar en "/"
    nombre = nombre.split("/")[0]

    # Limpiar espacios
    nombre = nombre.strip()

    # Reemplazar espacios por _
    nombre = nombre.replace(" ", "_")

    # Eliminar caracteres raros (opcional pero recomendado)
    nombre = re.sub(r'[^A-Za-z0-9_]', '', nombre)

    return nombre

# Obtener imágenes
def get_images(nombre):
    folder_name = format_folder_name(nombre)
    path = f"images/{folder_name}/property_images"
    
    if not os.path.exists(path):
        return []

    images = sorted(os.listdir(path))
    
    return [
        f"{path}/{img}"
        for img in images
        if img.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]


for _, prop in df.iterrows():

    nombre = prop["property"]
    localizacion = f"{prop['city']}, {prop['state']}"

    images = get_images(nombre)

    # Slideshow
    if images:
        imgs_html = "".join([
            f'<img src="{img}" class="slide" style="width:100%; display:none; border-radius:8px;">'
            for img in images
        ])

        slideshow = f"""
        <div class="slideshow">
            {imgs_html}
        </div>

        <script>
        var slides = document.currentScript.previousElementSibling.querySelectorAll('.slide');
        let index = 0;
        function showSlides() {{
            slides.forEach(s => s.style.display = "none");
            slides[index].style.display = "block";
            index = (index + 1) % slides.length;
            setTimeout(showSlides, 1500);
        }}
        showSlides();
        </script>
        """
    else:
        slideshow = "<p>No images available</p>"

    # Info extra (opcional)
    extra_info = f"""
    <p><strong>Category:</strong> {prop['category']}</p>
    <p><strong>Sq Ft:</strong> {prop['sq_ft']}</p>
    <p><strong>Available:</strong> {prop['available_space']}</p>
    <p><strong>Type:</strong> {prop['sale_lease']}</p>
    <p><strong>Cost:</strong> ${prop['cost']}</p>
    """

    html_popup = f"""
    <div style="width:250px">
        <h3>{nombre}</h3>
        <h4>{localizacion}</h4>
        {slideshow}
        <p>{prop['description']}</p>
        {extra_info}
    </div>
    """

    iframe = folium.IFrame(html=html_popup, width=270, height=400)
    popup = folium.Popup(iframe, max_width=300)

    folium.Marker(
        location=[prop["lat"], prop["lon"]],
        popup=popup,
        icon=folium.Icon(color="blue", icon="home", prefix="fa")
    ).add_to(marker_cluster)

mapa.save("mapa_las_brisas.html")

print("Mapa generado con Excel + slideshow correctamente.")