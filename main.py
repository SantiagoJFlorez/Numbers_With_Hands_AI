#Librerias
import streamlit as st
from tensorflow import keras
import os
from os import remove
import numpy as np
from PIL import Image

#funciones
@st.cache
def use_image(imagen_file):
    
    img=np.asarray(Image.open(imagen_file))
    im= Image.fromarray(np.uint8(img))
    size=(64,64)
    im1=im.resize(size)
    img2=np.asarray(im1)
    return img2

@st.cache
def load_image(imagen_file):
    img1=Image.open(imagen_file)
    return img1

#Título
st.write("""
# Predicción del número de dedos en manos 
""")

#Subida del archivo
imagen_file = st.file_uploader('Omite el error. Sube aquí la imagen ',type='jpg')
if imagen_file is not None:
    st.write(type(imagen_file))
    file_details={"Nombre":imagen_file.name,
    "Tipo":imagen_file.type,"Tamaño":imagen_file.size}
    
    st.image(load_image(imagen_file),width=250,height=250)

#Subida del modelo entrenado
model = keras.models.load_model('Power.h5')

#Proceso de la imagen 
new1=use_image(imagen_file)

new=np.array([new1,new1])

st.write('Espera, estamos procesando...')

#Predicción del modelo
y_pred=model.predict(new)

filtro = y_pred[0].max()
target= y_pred[0] ==filtro


for i in range(len(target)):
  if target[i] ==1:
    num= i

#Entregable
st.write('es el número '+str(num))
