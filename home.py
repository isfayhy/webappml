import streamlit as st
st.set_page_config(page_title="WebApp", page_icon=":sunglasses:")

st.title("Mon formulaire")


st.video("https://www.youtube.com/watch?v=4ch1oHamkv8")
st.video("https://www.youtube.com/watch?v=ld-f9b3OSTg")

if st.button("Première vidéo"):
    st.success("Première vidéo choisie !")

if st.button("Deuxieme vidéo"):
    st.success("Deuxième vidéo choisie !")

