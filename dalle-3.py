import streamlit as st
from openai import OpenAI


st.title("Intégration Dall-E 3")
OpenAIKEY = st.sidebar.text_input("Entrez votre clé API")
st.write(OpenAIKEY)
prompt = st.text_input("Entrez un texte pour générer une image")

def prompt_dall_e():
    client = OpenAI(api_key=OpenAIKEY)

    try:
        response = client.images.generate(
            model="dall-e-3", 
            prompt=prompt,
            #size="512x512",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption="Votre image a été générée")
    except Exception as e:
        st.error(f"Erreur lors de la génération de l'image: {e}")
if st.button("Générer"):
    prompt_dall_e()