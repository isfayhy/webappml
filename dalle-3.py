import streamlit as st
from openai import OpenAI


st.title('Intégration OpenAI ')




# Testez ici plusieurs variation du prompte

APIKEY = st.text_input("Entre ta clé API :")

client = OpenAI(api_key=APIKEY)

prompt = st.text_input("Entre ton texte :") 



if st.button("Générer"):
    image = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
    )  
    image_url = image['data'][0]['url']
    st.image(image_url)

