import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 LangChain App')

openai_api_key = st.sidebar.text_input('Paste OpenAI API key here:')

def generate_response(input_text: str):
      try:    
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))
      except Exception as ex:
        print(st.error(ex))

with st.form('my_form'):
  
      text = st.text_area('Enter text prompt:', 'What is the meaning of life the universe and everything?')
      submitted = st.form_submit_button('Submit')

      if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

      if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
