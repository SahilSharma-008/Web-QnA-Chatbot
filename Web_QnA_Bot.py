import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Initialize Gemini API
genai.configure(api_key='enter your api')
#initialize the google gemini model with the specified versionfor text generation
model = genai.GenerativeModel('gemini-2.5-pro')

# Fetching the HTML content of the webpage from the given url
def fetch_website_content(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch content: {e}")
        return None

# Extracting relevant information from the website
def fetch_relevant_information(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Removing unnecessary tags like scripts, styles, and ads cuz these don't contain useful information
    for script in soup(["script", "style", "aside", "header", "footer", "nav"]):
        script.extract()

    paragraphs = soup.find_all('p')
    headers = soup.find_all(['h1', 'h2', 'h3'])

    content = " ".join([header.get_text(strip=True) for header in headers])
    content += " ".join([para.get_text(strip=True) for para in paragraphs])

    return content[:2000]  # Limit to first 2000 characters for processing

def process_content(content, user_input):
    try:
        prompt = f"""Based on the following content:

{content}

Please provide a brief summary of the content and then answer this question: {user_input}

Format your response as follows:
Summary: [Your summary here]
Answer: [Your answer to the user's question here]"""

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error processing content: {e}")
        return None

# Main function to run the chatbot
def main():
    print("My ChatBOT :web scrapper:")
    print("Hello User! How can I assist you today?")

    # Ask for website URL
    user_input_url = input("Please provide a URL: ")

    website_content = fetch_website_content(user_input_url)
    if website_content:
        print("Website content fetched successfully.")

        # Ask for user question
        user_input = input("Chatbot: How can I assist you? : ")

        if website_content:
            extracted_info = fetch_relevant_information(website_content)

            if extracted_info:
                try:
                    chatbot_response = process_content(extracted_info, user_input)

                    if chatbot_response:
                        print("\nChatbot Response:\n", chatbot_response)

                except Exception as e:
                    print(f"Error generating response: {e}")
            else:
                print("Extracted information is empty. Please check the website content.")
        else:
            print("Please fetch valid website content first.")

if __name__ == '__main__':

    main()
