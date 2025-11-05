# Web-QnA-Chatbot
The **Web QnA Chatbot** is a Python-based intelligent chatbot that dynamically interacts with website content. It scrapes information from a provided URL, processes it, and answers user queries based on the extracted data. By integrating **web scraping with Google Gemini (Generative AI)**, this project enables users to ask context-aware questions about any website and receive meaningful, AI-driven responses in real time.  

#  Tech Stack  
- **Language:** Python 3.8  
- **Libraries:** `requests`, `beautifulsoup4`, `google-generativeai`  
- **IDE/Platform:** Visual Studio Code (VSCode)  
- **AI Model:** Google Gemini (Generative AI)

# Features  
- **Website Scraping:** Fetches and parses HTML content using BeautifulSoup.  
- **AI-Powered Responses:** Uses Google Gemini API for contextual answers.  
- **Interactive CLI:** Simple and fast terminal-based chatbot interface.  
- **Content Summarization:** Summarizes website text before responding.  
- **Error Handling:** Handles invalid URLs, fetch errors, and API issues gracefully.

# Step-by-Step Setup 
**Install Dependencies**
pip install requests beautifulsoup4 google-generativeai

**Configure API Key**
Replace 'YOUR_API_KEY' in the script with your Google Gemini API key:
genai.configure(api_key='YOUR_API_KEY')

**Run the Chatbot**
python Web_QnA_Bot.py
