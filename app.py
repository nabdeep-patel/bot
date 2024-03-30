import google.generativeai as genai
import streamlit as st

st.title("Hello User")

def chat_with_gemini(prompt):
  # Initialize GenerateTextRequest object
  request = GenerateTextRequest(
      prompt=TextPrompt(text=prompt),
      max_characters=2048,

      
def chat_with_gemini(prompt):
  # Initialize GenerateTextRequest object
  request = GenerateTextRequest(
      prompt=TextPrompt(text=prompt),
      max_characters=2048,  # Adjust character limit as needed
  )
  client = genai.Client(api_key=st.secrets["genainp"])
  try:
    # Send request to Gemini and get response
    response = client.text.generate_text(request=request)
    return response.text
  except Exception as e:
    return f"Error: {e}"
      
if "messages" not in st.session_state:
  st.session_state["messages"] = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("Talk to Gemini"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  response = chat_with_gemini(prompt)
  st.session_state.messages.append({"role": "assistant", "content": response})
  with st.chat_message("assistant"):
    st.markdown(response)
