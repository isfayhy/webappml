import streamlit as st

st.set_page_config(page_title="Formulaire", page_icon="📝")



nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
age = st.number_input("Âge", min_value=0, max_value=100, value=18)
niveau_etude = st.selectbox("Niveau d’étude", ["Sans diplôme", "BAC", "BAC+2", "BAC+5", "BAC+8"])

if st.button("Soumettre"):
    if age < 18:
        st.success("Vous êtes mineur.")
    else:
        st.success("Vous êtes majeur.")
