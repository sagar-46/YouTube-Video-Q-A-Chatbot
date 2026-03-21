import streamlit as st
from utils import get_transcript, create_vector_store, get_answer

st.title("YouTube Video Q&A Chatbot")

url = st.text_input("Enter YouTube URL")

if url:
    video_id = url.split("v=")[-1]

    transcript = get_transcript(video_id)

    vectorstore = create_vector_store(transcript)

    question = st.text_input("Ask a question about the video")

    if question:
        answer = get_answer(vectorstore, question)

        st.write("Answer:")
        st.write(answer.content)