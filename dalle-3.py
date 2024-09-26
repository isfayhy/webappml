import streamlit as st
from openai import OpenAI


st.title('Intégration OpenAI ')




OpenAIKEY = st.text_input("Entre ta clé API :")


prompt = st.text_input("Entre ton texte :") 



def generer() :
    client = OpenAI(api_key=OpenAIKEY)
    
    image = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="512x512",
        quality="standard",
        n=1,
    )  
    
    image_url = image['data'][0]['url']
    st.image(image_url)

if st.button("Générer"):
    generer()