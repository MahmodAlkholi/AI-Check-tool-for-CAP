import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Access variables
#load_dotenv(dotenv_path="/run/media/storm/local1/PEX company/crewai/chick updates tool/.env")
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

if not load_dotenv():
    print("Warning: .env file not found or could not be loaded.")

# Fetch API key
#api_key = os.getenv("OPENAI_API_KEY")
api_key = st.secrets["OPENAI_API_KEY"]


def check():

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-search-preview",
        web_search_options={
            "search_context_size": "low",
        },
        messages=[{
            "role": "user",
            "content": "notify me of updates on CAP guidelines",
        }],
    )

    st.write(completion.choices[0].message.content)


st.header("notify us of updates on CAP guidelines to modify our templates")

btn = st.button("CLICK TO CHICK")
if btn:
    check()
