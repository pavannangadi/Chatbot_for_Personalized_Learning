<h1 align="center">Chatbot_for_Personalized_Learning</h1>

<p align="center">
  A Rasa-based conversational chatbot offering personalized recommendations for learning resources and detailed topic explanations.
</p>

<h2>🚀 Key Features</h2>
<ul>
  <li><strong>Topic-based Information:</strong> Provides detailed explanations for a variety of topics using Hugging Face's <code>Flan-t5-large</code> model.</li>
  <li><strong>Course Recommendations:</strong> Suggests courses from platforms like Udemy based on user queries.</li>
  <li><strong>Personalized Learning:</strong> Recommends books, videos, and other resources tailored to user interests.</li>
  <li><strong>Motivational Content:</strong> Shares study tips and motivational advice.</li>
  <li><strong>Interactive UI:</strong> Built with Streamlit and enhanced using <a href="https://lottiefiles.com/">LottieFiles</a> animations for an engaging experience.</li>
  <li><strong>Feedback Collection:</strong> Seamlessly collects user feedback using <a href="https://formsubmit.co/">FormSubmit</a>.</li>
</ul>

<h2>📚 How It Works</h2>
<ol>
  <li><strong>User Interaction:</strong> Users interact with the chatbot through the Streamlit-based UI.</li>
  <li><strong>Intent Recognition:</strong> Rasa handles intent classification and entity extraction.</li>
  <li><strong>Dynamic Responses:</strong> The chatbot retrieves relevant information, videos, or courses and provides detailed explanations using Hugging Face's Flan-t5-large model.</li>
  <li><strong>Engaging UI:</strong> Lottie animations create an interactive experience, and a FormSubmit-powered feedback form ensures seamless communication.</li>
</ol>

<h2>🛠️ Installation</h2>
<h3>Prerequisites</h3>
<ul>
  <li>Python 3.8 or later</li>
  <li>Rasa Open Source</li>
  <li>Streamlit</li>
  <li>Hugging Face Transformers Library</li>
  <li>Google API Key (for YouTube Data API)</li>
</ul>

<h3>Steps</h3>
<ol>
  <li>Clone the repository:
    <pre>git clone https://github.com/your-username/personalized-learning-chatbot.git</pre>
  </li>
  <li>Navigate to the project folder:
    <pre>cd personalized-learning-chatbot</pre>
  </li>
  <li>Install dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Train the Rasa model:
    <pre>rasa train</pre>
  </li>
  <li>Run the chatbot:
    <ul>
      <li>Start the action server:
        <pre>rasa run actions</pre>
      </li>
      <li>Start the Rasa server:
        <pre>rasa run --enable-api --cors "*" --debug</pre>
      </li>
      <li>Launch the Streamlit UI:
        <pre>streamlit run app.py</pre>
      </li>
    </ul>
  </li>
</ol>

<h2>📁 Project Structure</h2>
<pre>
📂 personalized-learning-chatbot/
├──.streamlit
      ├── config.toml
├── actions/                     # Custom Rasa actions (e.g., fetching courses, topic info)
      ├── __init__.py
      ├── actions.py
├── models/                      # Trained Rasa models
├── app.py                       # Streamlit-based user interface
├── config.yml                   # Rasa pipeline and policy configuration
├── credentials.yml              # API credentials for integrations
├── domain.yml                   # Rasa domain file for intents, slots, and actions
├── data/                        # NLU and training data
      ├── nlu.yml
      ├── rules.yml
      ├── stories.yml
├── pages/
      ├── feedback_form.py       # Lottie animations and FormSubmit setup
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
</pre>

<h2>🎓 Example Commands</h2>
<ul>
  <li><strong>User:</strong> "Explain machine learning." <br>
      <strong>Bot:</strong> Provides a detailed explanation of machine learning concepts.</li>
  <li><strong>User:</strong> "Recommend Udemy courses on Python." <br>
      <strong>Bot:</strong> Fetches and displays Python-related Udemy courses.</li>
  <li><strong>User:</strong> "Share some study tips." <br>
      <strong>Bot:</strong> Provides motivational advice and study strategies.</li>
</ul>

<h2>🔧 Future Improvements</h2>
<ul>
  <li>Add multilingual support to reach a wider audience.</li>
  <li>Enhance recommendation algorithms using advanced machine learning models.</li>
  <li>Implement caching for frequent user queries to improve response time.</li>
  <li>Incorporate a feedback loop for users to rate recommendations.</li>
  <li>Add progress tracking to monitor learning milestones.</li>
</ul>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! To contribute:</p>
<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch for your feature or bug fix:
    <pre>git checkout -b feature/YourFeatureName</pre>
  </li>
  <li>Commit your changes:
    <pre>git commit -m 'Add some feature'</pre>
  </li>
  <li>Push to the branch:
    <pre>git push origin feature/YourFeatureName</pre>
  </li>
  <li>Submit a pull request.</li>
</ol>

<h2>📄 License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>


<p>If you like this project, don't forget to ⭐ the repository!</p>
