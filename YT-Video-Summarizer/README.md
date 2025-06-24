# 🎥 YouTube Video Summarizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)

A powerful web application that generates concise summaries of YouTube videos by extracting and analyzing video transcripts, powered by Google's Gemini AI.

## ✨ Features

- 📺 Extract transcripts directly from YouTube videos
- 🤖 AI-powered summarization using Google's Gemini model
- 📝 Generate detailed notes from video content
- 🎨 Clean, user-friendly web interface
- 🔐 Secure API key management with environment variables

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BhumiPatel2309/YT-Video-Transcribe-Summarizer.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Add your API keys to .env file(if required)

## 🛠️ Usage

1. First, set up your Google API key in the `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to the local URL shown in the terminal (usually http://localhost:8501)

5. Enter a YouTube URL and click "Get Detailed Notes" to generate a summary

## 📦 Dependencies

- `streamlit` - For the web interface
- `python-dotenv` - For managing environment variables
- `google-generativeai` - Google's Gemini AI client library
- `youtube-transcript-api` - For fetching YouTube video transcripts

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) - For the powerful AI summarization
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) - For fetching video transcripts
- [Streamlit](https://streamlit.io/) - For the web interface framework
