import streamlit as st
from streamlit_chat import message
from hugchat import hugchat


# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ",
            value="",  
            key="input")
    return input_text

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response


st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

with st.sidebar:
    st.title("ChatBot Using HugChat")
    st.markdown('''
        ## About
        This app is an LLM-powered chatbot
    ''')
    # add_vertical_space(5)
    st.text("")
    st.text("")
    st.text("")
    st.write('Click here to see the [Github Repository]()')


if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

input_container = st.container()
response_container = st.container()


## Applying the user input box
with input_container:
    user_input = get_text()

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in reversed(range(len(st.session_state['generated']))):
            message(st.session_state['generated'][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
