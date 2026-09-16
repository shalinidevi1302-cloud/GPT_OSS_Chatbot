# Hugging Face Model

A simple AI chatbot built using Streamlit, Python, and Hugging Face's OpenAI-compatible API. This project uses the OpenAI GPT-OSS 120B model to answer user questions and provide conversational AI responses.

## Project Overview

Hugging Face Model is a web-based chatbot application that allows users to interact with the GPT-OSS 120B language model through a simple and user-friendly interface.

The application is built using Python and Streamlit. Users can enter their Hugging Face API token and start chatting with the AI model.

## Features

* AI chatbot using GPT-OSS 120B.
* Hugging Face API integration.
* Simple and interactive Streamlit interface.
* User and assistant chat messages.
* Conversation history during the current session.
* Secure password-type API token input.
* Easy to run locally using Python.

## Technologies Used

* Python
* Streamlit
* OpenAI Python SDK
* Hugging Face API
* GPT-OSS 120B

## Project Structure

```text
GPT_OSS_Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd GPT_OSS_Chatbot
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Hugging Face API Token

To use the chatbot:

1. Create an account on Hugging Face.
2. Generate an API token with the required permissions.
3. Open the Streamlit chatbot.
4. Enter your Hugging Face API token.
5. Start asking questions.

## Model Used

```text
openai/gpt-oss-120b
```

The chatbot connects to the Hugging Face router using an OpenAI-compatible API.

## Example Questions

```text
Explain Data Science
```

```text
What is Machine Learning?
```

```text
Explain Python programming
```

```text
What is Artificial Intelligence?
```

## How It Works

1. The user opens the Streamlit chatbot.
2. The user enters a Hugging Face API token.
3. The application connects to the Hugging Face API.
4. The user enters a question.
5. GPT-OSS 120B processes the question.
6. The chatbot displays the AI response.

## Security

* Do not share your Hugging Face API token.
* Do not upload API tokens to GitHub.
* Do not hardcode secret API tokens in `app.py`.
* Use environment variables or Streamlit secrets for production deployments.
* If a token is accidentally exposed, revoke it and create a new one.

## Future Improvements

* Add a clear chat button.
* Add dark and light themes.
* Add chat export functionality.
* Add streaming responses.
* Deploy the chatbot online.
* Add conversation history storage.
* Improve the chatbot user interface.

## Author

Shalini Devi.V
BSC CS with AI

## License

This project is for educational and personal use.
