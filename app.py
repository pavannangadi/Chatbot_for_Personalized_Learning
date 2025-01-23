import streamlit as st
import requests
from streamlit_lottie import st_lottie
# from botocore.endpoint import history_recorder

st.set_page_config(page_title="Rasa Chatbot",
                   page_icon=":technologist:",
                   layout="wide",
                   initial_sidebar_state="collapsed") # Options: "auto", "expanded", "collapsed")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -- load assets---
lottie_coding = load_lottieurl("https://lottie.host/6a2bfd58-39f4-4c42-af27-4f6704cc9f01/W4K91PVZ2U.json")



# --header--
left_column, right_column = st.columns(2)
with left_column:
    st.title("Rasa Chatbot")
    st.subheader("I am an Educational Chatbot")
with right_column:
    st_lottie(lottie_coding, height=200, key="educational")

#---sidebar---
with st.sidebar:
    st.write("This is the sidebar.")
    st.link_button("New Chat", url="http://localhost:8501", )
    st.button("History")

# with st.container():
#     messages = st.container(height=500)
# #
# #     if prompt := st.chat_input("What can I help with?"):
# #         messages.chat_message("user").write(prompt)
# #         messages.chat_message("assistant").write(f"Echo: {prompt}")
# # st.write("---")
#
#
#     # -----chat-------
#
#     # ----Initialize chat history-----
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#
#     # display chat messages from history on app rerun
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
#
#     if prompt := st.chat_input("What can I help with?"):
#         with st.chat_message("user"):
#             st.markdown(prompt)
#
#         st.session_state.messages.append({"role": "user", "content": prompt})
#
#         response = f"Bot: {prompt}"
#
#         with st.chat_message("assistant"):
#             st.markdown(response)
#         st.session_state.messages.append({"role": "assistant", "content": response})

# Create a container for the chat interface
with st.container():
    # messages = st.container(height=500)
    chat_container = st.container(height=400, key="chat")

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Add chat messages to the container
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # User input field (outside the chat container for better structure)
    st.markdown(
        """
       <p style="color: #000000; font-size: 50px; font-weight:bold; text-align: center;">
    What can I help with?
</p>
        """,
        unsafe_allow_html=True
    )
    # Inject custom CSS to style the chat input
    st.markdown(
        """
        <style>
        /* Style the chat input box */
        div[data-testid="stChatInput"] textarea {
            font-size: 20px; /* Change font size */
            color: #00000; /* Change text color */
        }

        /* Optional: Style the placeholder text */
        div[data-testid="stChatInput"] textarea::placeholder {
            font-size: 20px; /* Change placeholder font size */
            color: black; /* Change placeholder text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Chat input widget
    if user_input := st.chat_input("Type your message here..."):
        # st.write(f"You entered: {user_input}")
    # if user_input := st.chat_input( "What can I help you with?"):
        # Add user message to chat container
        with chat_container:
            with st.chat_message("user"):
                st.markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate assistant's response (replace with actual logic)
        assistant_response = f"Bot: {user_input}"

        # Add assistant message to chat container
        with chat_container:
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
local_css("style/style.css")



