# ChatBot-HugChat

This is a Streamlit app that uses the HugChat API and an LLM (Language Model) from the Hugging Face model repository to provide a chatbot experience. The chatbot can generate responses to user input in a conversational manner.

## Dependencies
- Streamlit
- hugchat


## Installation
To install the necessary dependencies, run:

```
pip install streamlit hugchat
```
## Running the App
To run the app, use the following command in the terminal:

```
streamlit run app.py
```
Once the app is running, a sidebar will appear with information about the chatbot and the option to enter user input. The app will display the chat history and the AI-generated responses to the user input.

## How it Works
The app uses Streamlit to display the user interface, hugchat to communicate with the HugChat API, and an LLM from the Hugging Face model repository to generate responses.

The input container contains a text input box where the user can enter their prompt. Once the user enters a prompt, the app uses the generate_response function to generate a response using the LLM model and the HugChat API. The response is stored in the st.session_state[generated] list, and the user input is stored in the st.session_state[past] list.

The response container displays the chat history and the AI-generated responses. The message function from the streamlit_chat package is used to display the chat history and the generated responses.

