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
    nombre = nombre.split("-")[0]

    # Limpiar espacios
    nombre = nombre.strip()

    # Reemplazar espacios por _
    nombre = nombre.replace(" ", "_")

    # Eliminar caracteres raros (opcional pero recomendado)
    nombre = re.sub(r'[^A-Za-z0-9_]', '', nombre)

    return nombre

# Obtener imágenes
BASE_URL = "https://genesisperez19.github.io/las-brisas-interactive-map"


def get_images(nombre):
    folder_name = format_folder_name(nombre)
    path = f"images/{folder_name}/property_images"
    
    if not os.path.exists(path):
        return []

    images = sorted(os.listdir(path))
    
    return [
        f"{BASE_URL}/{path}/{img}"
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