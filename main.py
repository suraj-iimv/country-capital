import streamlit as st
from openai import OpenAI

# Initialize client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["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"]  # store key securely
)

# App UI
st.title("🌍 Country → Capital Finder")

country = st.text_input("Enter a country name:")

if st.button("Get Capital") and country:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                {
                    "role": "user",
                    "content": f"What is the capital of {country}? Give only the capital name."
                }
            ]
        )

        capital = response.choices[0].message.content
        st.success(f"Capital: {capital}")

    except Exception as e:
        st.error(f"Error: {e}")
