import json
import os
import sys
import boto3
import streamlit as st

## We will be suing Titan Embeddings Model To generate Embedding

from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock

## Data Ingestion

import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader

# Vector Embedding And Vector Store

from langchain.vectorstores import FAISS

## LLm Models
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

## Bedrock Clients
bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)


## Data ingestion
def data_ingestion():
    try:
        # Load PDFs from the uploads directory
        loader = PyPDFDirectoryLoader("uploads")
        documents = loader.load()
        
        if not documents:
            raise ValueError("No PDF files found in the uploads directory")

        # - in our testing Character split works better with this PDF data set
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000,
                                                     chunk_overlap=1000)
        
        docs = text_splitter.split_documents(documents)
        return docs
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        return []

## Vector Embedding and vector store

def get_vector_store(docs):
    if not docs:
        raise ValueError("No documents to process. Please upload a PDF file first.")
    
    try:
        vectorstore_faiss = FAISS.from_documents(
            docs,
            bedrock_embeddings
        )
        vectorstore_faiss.save_local("faiss_index")
    except Exception as e:
        raise Exception(f"Error creating vector store: {str(e)}")

def get_claude_llm():
    llm=Bedrock(model_id="anthropic.claude-v2",client=bedrock,
                model_kwargs={'max_tokens_to_sample':512})
    
    return llm

def get_llama2_llm():
    llm=Bedrock(model_id="meta.llama3-8b-instruct-v1:0",client=bedrock,
                model_kwargs={'max_gen_len':512})
    
    return llm

prompt_template = """

Human: Use the following pieces of context to provide a 
concise answer to the question at the end but usse atleast summarize with 
250 words with detailed explaantions. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

def get_response_llm(llm,vectorstore_faiss,query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_faiss.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
    answer=qa({"query":query})
    return answer['result']


def main():
    st.set_page_config("Chat PDF")
    
    st.header("Chat with PDF 💁")
    
    # Create a temporary directory for uploaded PDFs
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    # PDF upload section
    uploaded_file = st.file_uploader("Upload a PDF file", type=['pdf'])
    
    if uploaded_file:
        # Save the uploaded file
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process the uploaded PDF
        try:
            docs = data_ingestion()
            if docs:
                get_vector_store(docs)
            else:
                st.error("No text was extracted from the PDF. Please try uploading a different PDF.")
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")
    
    # Question input
    user_question = st.text_input("Ask a Question about the PDF")

    if st.button("Claude Output"):
        if not os.path.exists("faiss_index"):
            st.error("No vector store found. Please upload and process a PDF first.")
            return
        
        with st.spinner("Processing..."):
            try:
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
                llm = get_claude_llm()
                st.write(get_response_llm(llm, faiss_index, user_question))
                st.success("Done")
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")

    if st.button("Llama2 Output"):
        if not os.path.exists("faiss_index"):
            st.error("No vector store found. Please upload and process a PDF first.")
            return
        
        with st.spinner("Processing..."):
            try:
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
                llm = get_llama2_llm()
                st.write(get_response_llm(llm, faiss_index, user_question))
                st.success("Done")
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
            st.success("Done")

if __name__ == "__main__":
    main()