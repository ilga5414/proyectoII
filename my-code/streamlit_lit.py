import pandas as pd
import src.manage_data as dat
import streamlit as st
from PIL import Image
import plotly.express as px 

Image = Image.open("../imagenes/signos-xra-streamlit.jpg")

st.image(Image)


st.write("""
Quiero que todos los no solteros descubrais aqui la compatibilidad de los signos de vuestra relación.
Los solteros, os invito a que os registreis en Meetic!""")