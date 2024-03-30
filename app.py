import google.generativeai as genai
import streamlit as st
from google.generativeai.v1.types.text import GenerateTextRequest, TextPrompt  # Add import statements for GenerateTextRequest and TextPrompt

st.title("Hello User")

def chat_with_gemini(prompt):
    # Initialize GenerateTextRequest object
    request = GenerateTextRequest(
        prompt=TextPrompt(text=prompt),
        max_tokens=2048,  # Adjust token limit as needed
    )
    client = genai.Client(api_key=st.secrets["genainp"])  # Assuming "genainp" is your secret key name
    try:
        # Send request to Gemini and get response
        response = client.text.generate_text(request=request)
        return response.text
    except Exception as e:
        return f"Error: {e}"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.echo():
        if message["role"] == "user":
            st.markdown(f"**User:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**Assistant:** {message['content']}")

if prompt := st.text_input("Talk to Gemini"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chat_with_gemini(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
