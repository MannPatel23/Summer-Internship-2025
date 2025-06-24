# PDF Chat with AWS Bedrock

![PDF Chat](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)

PDF Chat is a powerful application that allows you to interact with PDF documents using natural language. Built with AWS Bedrock, it leverages state-of-the-art AI models to provide intelligent responses to your questions about PDF content.

## Features

- 📚 Document Upload: Support for PDF files
- 💬 Natural Language Interaction: Engage with PDF content using conversational queries
- 🤖 AI-Powered Responses: Utilizes AWS Bedrock's Claude and Llama2 models
- 🔍 Semantic Search: Vector-based similarity matching for accurate results

## Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd AWS-Bedrock
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. 🚀 Launch the Application:
```bash
streamlit run app.py
```

2. 📝 In the Web Interface:
   - 📤 Click the "Upload a PDF file" button to upload your document
   - ⏳ Wait for the processing to complete (you'll see progress messages)
   - 📝 Enter your question in the text input
   - 🤖 Click either "Claude Output" or "Llama2 Output" to get answers

## AWS Configuration

Make sure your AWS CLI is configured with the necessary permissions:
```bash
aws configure
```

## Technologies Used

- 🌐 AWS Bedrock: AI Models and Services
- 📱 Streamlit: Web Application Framework
- 🤖 LangChain: AI Application Framework
- 📊 FAISS: Vector Similarity Search
- 🐍 Python: Programming Language
