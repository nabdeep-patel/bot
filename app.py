import streamlit as st

# Define a function to handle the chat messages
def chat():
    st.title("Streamlit Chat App")
    st.markdown("Welcome to the chat app! Feel free to start a conversation.")
    
    # Create a text input for user messages
    user_input = st.text_input("You:", "")

    # Create a button to send the message
    if st.button("Send"):
        # Display the user's message
        st.write("You:", user_input)

        # You can add your own logic here to generate responses
        # For simplicity, let's just echo the user's message as the response
        st.write("Bot:", user_input)

# Run the chat function
if __name__ == "__main__":
    chat()
