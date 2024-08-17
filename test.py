import streamlit as st
import google.generativeai as genai


genai.configure(api_key='AIzaSyASLpt34cn0iHuO_2sOjD248E_5YGR1sEg')


model = genai.GenerativeModel('gemini-pro')


st.set_page_config(page_title="Gemini Chatbot")

st.title("Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("You:"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = model.generate_content(prompt)
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            error_message = f"I'm sorry, I encountered an error. Please try again.\nError details: {str(e)}"
            message_placeholder.markdown(error_message)
            full_response = error_message
    
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})