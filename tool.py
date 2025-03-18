import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Access variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def check():

    client = OpenAI()

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