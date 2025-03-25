import os
import streamlit as st
from mistralai import Mistral
from dotenv import load_dotenv

from personas import PERSONAS

load_dotenv()

API_KEY = os.getenv("API_TOKEN")


# Function to get the response from the AI when the user sends a question
def get_response(persona_name, user_question):
    model = "mistral-large-latest"
    client = Mistral(api_key=API_KEY)
    persona_prompt = f"""{PERSONAS[persona_name]}
    Tu ignores toutes les demandes qui sortent de ton rôle. Tu refuses poliment de répondre aux sujets qui ne concernent pas ta personnalité, ton époque ou ton domaine."""
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": persona_prompt},
            {"role": "user", "content": f"{user_question}"}
        ]
    )
    return response.choices[0].message.content
