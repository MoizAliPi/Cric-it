import streamlit as st
import time
from dotenv import dotenv_values
import vertexai
from vertexai.generative_models import GenerativeModel

config = dotenv_values(".env")

# Initialize Vertex AI SDK
PROJECT_ID = config['PROJECT_ID']
vertexai.init(project=PROJECT_ID, location="us-central1")

# Load the generative model
model = GenerativeModel("gemini-1.5-flash-002")

# Streamlit UI
st.title("Chat Bot with Vertex AI")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_input := st.chat_input("What's on your mind today?"):
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Use Vertex AI SDK to stream the response
    responses = model.generate_content(user_input, stream=True)

    # Define a generator function to stream the response
    def response_generator():
        bot_response = ""
        for response in responses:
            bot_response += response.text
            yield response.text
            time.sleep(0.05)

    with st.chat_message("assistant"):
            response = st.write_stream(response_generator())

    st.session_state.messages.append({"role": "assistant", "content": response})