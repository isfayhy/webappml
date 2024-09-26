import streamlit as st
st.set_page_config(page_title="WebApp", page_icon=":sunglasses:")

st.title("Mon formulaire")


st.video("https://www.youtube.com/watch?v=4ch1oHamkv8")
if st.button("Choisir"):
    st.success("Première vidéo choisie !")

st.video("https://www.youtube.com/watch?v=ld-f9b3OSTg")

if st.button("Choisir"):
    st.success("Deuxième vidéo choisie !")

