import streamlit as st
from personas import PERSONAS
from requestai import get_response

# Configuration de la page Streamlit
st.set_page_config(page_title="Dead Talks (API)", page_icon="💀")

# Interface Streamlit
st.title("💀 Dead Talks (via Mistral API) 💬")
st.subheader("Discute avec une personnalité disparue grâce à l'IA")

persona_name = st.selectbox("Choisis une personnalité :", list(PERSONAS.keys()))
user_question = st.text_input("Pose ta question 👇")

send_button = st.button("Envoyer")

# Check if the user has submitted the form and the required fields are filled
if send_button and not user_question:
    st.warning("Pose une question à la personnalité !")
elif send_button and user_question:

    with st.spinner("L'IA réfléchit..."):
        response = get_response(persona_name, user_question)
        if response:
            # Display the response from the AI
            st.markdown(f"💬 **{persona_name}** : {response}")
