import streamlit as st
import requests
from PIL import Image
import random
import time
from streamlit_lottie import st_lottie

# Streamlit Frontend for Rasa Chatbot
st.set_page_config(page_title="LumiBot", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")

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
    st.title("LumiBot")
    st.subheader("I am an Educational Chatbot")
with right_column:
    st_lottie(lottie_coding, height=200, key="educational")

# Custom CSS for Vibrancy & Interactivity
st.markdown("""
<style>
/* Global Background */
body {
    background-color: white;
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Poppins', sans-serif;
    color: #333;
}

/* Sidebar Styling */
.sidebar-title {
    font-size: 22px;
    font-weight: bold;
    color: #2d3436;
    margin-bottom: 15px;
    text-shadow: 1px 1px #dfe6e9;
}

.sidebar-section {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    color: white;
    font-weight: bold;
    transition: transform 0.3s, background 0.3s;
}

.sidebar-section:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
}

/* Chat Container */
.chat-container {
    max-height: 600px;
    overflow-y: auto;
    padding: 15px;
    background-color: white;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

/* Chat Bubbles */
.chat-message {
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    max-width: 75%;
    word-wrap: break-word;
    font-size: 16px;
    font-weight: 500;
    animation: fadeIn 0.4s ease-in-out;
}

.chat-message.user {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    color: white;
    text-align: left;
    margin-left: auto;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.3);
}

.chat-message.bot {
    background: linear-gradient(to right, #fad0c4, #fbc2eb);
    color: #333;
    text-align: left;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.3);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #ff9966, #ff5e62);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 10px 20px;
    transition: transform 0.3s ease, background 0.3s ease-in-out;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.stButton>button:hover {
    background: linear-gradient(to right, #ff5e62, #ff9966);
    transform: scale(1.1);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
}

/* Floating Action Button */
.floating-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    text-align: center;
    font-size: 30px;
    line-height: 60px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    animation: bounce 2s infinite;
}

.floating-btn:hover {
    background: linear-gradient(to right, #2575fc, #6a11cb);
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)

# Sidebar Branding
# st.sidebar.image("Image.jpeg", caption="LearnAI", use_container_width=True)
st.sidebar.link_button("New Chat", url="http://localhost:8501", )
st.sidebar.markdown('<h2 class="sidebar-title">LumiBot</h2>', unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="sidebar-section">
📚 Learn interactively about AI, ML, DevOps, and more!
</div>
<div class="sidebar-section">
🚀 Key Features:
<ul>
  <li>Dynamic Learning Suggestions</li>
  <li>Interactive Visuals</li>
  <li>AI Fun Facts</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Floating Help Button
# st.markdown('<div class="floating-btn">❓</div>', unsafe_allow_html=True)

# Backend URL (Update with your Rasa server endpoint)
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ Chat messages appear **above** the input field
chat_container = st.container()
with chat_container:
    for msg in st.session_state["messages"]:
        if msg["sender"] == "user":
            # User message: Align right and add background color
            st.markdown(f'<div style="text-align: left; background-color: #DCF8C6; border-radius: 10px; padding: 10px; margin: 5px; max-width: 25%; margin-left: auto; margin-right: 0;color:black;">{msg["text"]}</div>', unsafe_allow_html=True)
        else:
            # Bot message: Align left and add background color
            st.markdown("Bot"f'<div style="text-align: left; text-color: black; background-color: #f1f0f0; border-radius: 10px; padding: 10px; margin: 5px; max-width: 50%; margin-left: 0; margin-right: auto; color:black;">{msg["text"]}</div>', unsafe_allow_html=True)

# ✅ Add space above input field using `st.markdown()`
st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)

# ✅ User input field **at the bottom**
user_input = st.text_input(
    "Type your message...",
    placeholder="Ask me anything...",
    label_visibility="collapsed"
)

# Send user input to the bot when Enter is pressed
if user_input:
    # Append the user message to session state
    st.session_state["messages"].append({"sender": "user", "text": user_input})

    # Display user's message instantly on the right
    with chat_container:
        st.markdown(f'<div style="text-align: left; background-color: #DCF8C6; border-radius: 10px; padding: 10px; margin: 5px; max-width: 25%; margin-left: auto; margin-right: 0; color:black;">{user_input}</div>', unsafe_allow_html=True)

    # Fetch bot response and store it in session state
    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_input})
        response_data = response.json()

        bot_reply = "\n".join(msg["text"] for msg in response_data) if response_data else "🤖 Sorry, I didn't get that."

        # Append bot response to session state
        st.session_state["messages"].append({"sender": "bot", "text": bot_reply})

        # Display bot's response on the left
        with chat_container:
            st.markdown("Bot"f'<div style="text-align: left; text-color: black; background-color: #f1f0f0; border-radius: 10px; padding: 10px; margin: 5px; max-width: 50%; margin-left: 0; margin-right: auto; color:black;">{bot_reply}</div>', unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f"⚠️ Error communicating with the bot: {e}")


# Sidebar dropdown menu for topic selection
topic = st.sidebar.selectbox(
    "Select a topic to get book recommendations:",
    ["Select a topic", "AI", "Machine Learning", "Deep Learning", "Data Science", "NLP"]
)

# Dictionary with book recommendations for each topic
book_recommendations = {
    "AI": [
        "1. Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig",
        "2. Superintelligence: Paths, Dangers, Strategies by Nick Bostrom",
        "3. The Age of Em: Work, Love, and Life when Robots Rule the Earth by Robin Hanson"
    ],
    "Machine Learning": [
        "1. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron",
        "2. Pattern Recognition and Machine Learning by Christopher Bishop",
        "3. Machine Learning Yearning by Andrew Ng"
    ],
    "Deep Learning": [
        "1. Deep Learning by Ian Goodfellow, Yoshua Bengio, and Aaron Courville",
        "2. Neural Networks and Deep Learning by Michael Nielsen",
        "3. Deep Reinforcement Learning Hands-On by Maxim Lapan"
    ],
    "Data Science": [
        "1. Data Science for Business by Foster Provost and Tom Fawcett",
        "2. Python Data Science Handbook by Jake VanderPlas",
        "3. Practical Data Science with R by Nina Zumel and John Mount"
    ],
    "NLP": [
        "1. Speech and Language Processing by Daniel Jurafsky and James H. Martin",
        "2. Natural Language Processing with Python by Steven Bird, Ewan Klein, and Edward Loper",
        "3. Transformers for Natural Language Processing by Denis Rothman"
    ]
}

# Display book recommendations based on the selected topic in the sidebar
if topic != "Select a topic":
    st.sidebar.write(f"### Book Recommendations for {topic}:")
    for book in book_recommendations.get(topic, []):
        st.sidebar.write(book)

import csv

# Create a container for the feedback buttons at the bottom-right corner
st.markdown("""
    <style>
    .feedback-container {
        position: fixed;
        bottom: 30px;
        right: 30px;
        display: flex;
        flex-direction: column;  /* Change from column to row */
        align-items: center;
        gap: 10px;  /* Adjust the space between the buttons */
        z-index: 100;
    }
    .feedback-button {
        background-color: #ff9a9e;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        cursor: pointer;
        font-weight: bold;
        font-size: 18px;
        color: white;
        transition: background-color 0.3s;
    }
    .feedback-button:hover {
        background-color: #ff5e62;
    }
    </style>
""", unsafe_allow_html=True)


# Function to save feedback to a CSV file
def save_feedback(feedback):
    # Open the CSV file in append mode to add new feedback
    with open("feedback.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write only the feedback (no timestamp)
        writer.writerow([feedback])


# Display feedback buttons
with st.container():
    st.markdown('<div class="feedback-container">', unsafe_allow_html=True)
    # Positive feedback button (Thumbs Up)
    if st.button("👍", key="positive_feedback", help="Thumbs Up - Positive Feedback"):
        save_feedback("positive")  # Save only "positive" to CSV
        st.write("Thank you for your positive feedback!")
        # Negative feedback button (Thumbs Down)
    if st.button("👎", key="negative_feedback", help="Thumbs Down - Negative Feedback"):
        save_feedback("negative")  # Save only "negative" to CSV
        st.write("Sorry to hear that! We appreciate your feedback.")



    st.markdown('</div>', unsafe_allow_html=True)
