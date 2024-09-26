import streamlit as st
from openai import OpenAI


st.title('Intégration OpenAI ')




OpenAIKEY = st.text_input("Entre ta clé API :")


prompt = st.text_input("Entre ton texte :") 



if st.button("Générer"):
    client = OpenAI(api_key=OpenAIKEY)

    image = client.images.generate(
    prompt=prompt,
    n=1,
    size="512x512"
    )  
    image_url = image['data'][0]['url']
    st.image(image_url)

