import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv('api_key')


genai.configure(api_key=api_key)


model = genai.GenerativeModel('gemini-pro')


st.set_page_config(page_title="Learning Roadmap Generator")


st.title("Learning Roadmap Generator")


st.subheader("Get a comprehensive roadmap to learn any topic from beginner to advanced")


user_topic = st.text_input("Enter the topic you want to learn:")


if user_topic:
    prompt = f"Create a comprehensive roadmap to learn {user_topic} from beginner to advanced, including blog articles and YouTube videos. Structure the roadmap in clear stages (e.g., Beginner, Intermediate, Advanced) and provide specific resources for each stage."

    with st.spinner("Generating your learning roadmap..."):
        try:
            response = model.generate_content(prompt)
            roadmap = response.text

            
            st.subheader(f"Learning Roadmap for {user_topic}")
            st.markdown(roadmap)

            
            st.download_button(
                label="Download Roadmap",
                data=roadmap,
                file_name=f"{user_topic}_roadmap.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"An error occurred while generating the roadmap. Please try again. Error details: {str(e)}")
