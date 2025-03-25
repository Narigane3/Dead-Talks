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
    other_personas = [p for p in PERSONAS if p != persona_name]
    other_names = ", ".join(other_personas)

    persona_prompt = f"""{PERSONAS[persona_name]}

    Tu ignores toute question qui ne concerne pas ta personne. Si l'utilisateur te parle d'un autre personnage comme {other_names}, tu refuses poliment et tu lui rappelles que tu es uniquement {persona_name}.

    Ne réponds que si la question est pertinente pour toi."""
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": persona_prompt},
            {"role": "user", "content": f"{user_question}"}
        ]
    )
    return response.choices[0].message.content
