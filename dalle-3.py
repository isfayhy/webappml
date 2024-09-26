import streamlit as st
import openai

# Configuration de l'API
openai.api_key = "Sk-6uxlenvrwsRO0NlIgqhrg2B-AvWNwVlPV8MgbU-QSHT3BlbkFJSc_Lmu6ZS06yDsSmP4kvVEd42Ds95-CXp726oavJMA"

# Interface Streamlit
st.title('Intégration OpenAI dans Streamlit')

user_input = st.text_input("Entre ton texte :")

if st.button("Générer"):
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=user_input, 
        max_tokens=50
    )
    st.write(response.choices[0].text.strip())
