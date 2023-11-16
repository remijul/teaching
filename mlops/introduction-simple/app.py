import streamlit as st
#import tensorflow as tf
#import numpy as np
#from tensorflow.keras.applications.inception_v3 import InceptionV3
#from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
#from tensorflow.keras.preprocessing import image

# Charger le modèle InceptionV3 pré-entrainé
#model = InceptionV3(weights='imagenet')

# Titre de l'application
st.title("Reconnaissance d'images de chiens ou de chats")

# Widget de téléchargement d'image
uploaded_file = st.file_uploader("Choisissez une image...", type="jpg")

if uploaded_file is not None:
    # # Charger l'image depuis l'uploader
    # img = image.load_img(uploaded_file, target_size=(299, 299))

    # # Prétraitement de l'image
    # img_array = image.img_to_array(img)
    # img_array = np.expand_dims(img_array, axis=0)
    # img_array = preprocess_input(img_array)

    # # Prédiction
    # predictions = model.predict(img_array)

    # # Décodage des prédictions
    # decoded_predictions = decode_predictions(predictions, top=1)[0]

    # # Affichage des résultats
    # st.image(img, caption="Image chargée", use_column_width=True)
    st.write(f"Prédiction : ... ")
    st.write(f"Confiance : ... ")
