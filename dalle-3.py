import streamlit as st
from openai import OpenAI


st.title('Intégration OpenAI ')




APIKEY = st.text_input("Entre ta clé API :")


prompt = st.text_input("Entre ton texte :") 



if st.button("Générer"):
    client = OpenAI(api_key=APIKEY)
    image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    n=1,
    size="512x512"
    )  
    image_url = image['data'][0]['url']
    st.image(image_url)

