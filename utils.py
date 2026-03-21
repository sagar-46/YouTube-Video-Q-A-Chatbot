

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join([t.text for t in transcript])

    return text

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_texts(docs, embeddings)

    return vectorstore


def get_answer(vectorstore, query):

    # retrieve relevant documents
    docs = vectorstore.similarity_search(query, k=3)

    # load LLM
    
    from langchain_groq import ChatGroq

    llm = ChatGroq(
    model="groq/compound",
)

    # combine retrieved text
    context = " ".join([doc.page_content for doc in docs])

    # create prompt
    prompt = f"""
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    # generate answer
    response = llm.invoke(prompt)

    return response