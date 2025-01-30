import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
# from botocore.endpoint import history_recorder

st.set_page_config(page_title="Rasa Chatbot",
                   page_icon=":alien:",
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
    st.link_button("New Chat", url="http://localhost:8501", )
    st.title("✨ Special Features of the Personalized Learning Chatbot ✨")
    with st.container():
        st.markdown("""
    1. 🌟 **Topic-Based Dynamic Responses**  
       The chatbot provides detailed explanations and insights on a wide range of topics tailored to the user's queries.

    2. 🎯 **Personalized Learning Recommendations**  
       Suggests videos, books, and courses based on the user's interests and learning needs.

    3. 🌐 **Course Integration with APIs**  
       Fetches course details from platforms to recommend relevant learning materials.

    4. 🎨 **Engaging UI with LottieFiles**  
       Incorporates interactive animations to create an appealing and user-friendly interface.

    5. 💡 **Motivational Content and Study Tips**  
       Offers personalized study advice and motivational support to enhance the learning experience.

    6. 📨 **Seamless Feedback Collection with FormSubmit**  
       Allows users to provide feedback easily, ensuring continuous improvement of the chatbot.

    7. 🚀 **Streamlit-Powered Interactive Frontend**  
       Combines Rasa's robust conversational AI with Streamlit's simple and intuitive UI framework.
    """)



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

    # Inject custom CSS to style the chat input
    st.markdown(
        """
        <style>
        /* Style the chat input box */
        div[data-testid="stChatInput"] textarea {
            font-size: 20px; /* Change font size */
            color: #00000; /* Change text color */
            background-color: white !important;
            text-border: 1px solid black;
        }

        /* Optional: Style the placeholder text */
        div[data-testid="stChatInput"] textarea::placeholder {
            font-size: 20px; /* Change placeholder font size */
            color: black; /* Change placeholder text color */
            background-color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Chat input widget
    if user_input := st.chat_input("Type your message here..."):
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input}
        )

        # Add user input to the chat container
        with chat_container:
            with st.chat_message("user"):
                st.markdown(user_input)

        # Update session state
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate assistant's response (replace with actual logic)
        assistant_response = f"{user_input}"

        # Add assistant message to chat container
        with chat_container:
            with st.chat_message("assistant"):
                assistant_response = "\n\n".join(
                    msg['text'] for msg in response.json())  # Combine messages into one response
                st.text_area("Bot:", value=assistant_response, height=150)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})


# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
local_css("style/style.css")



