import os
import google.generativeai as genai

class GeminiApi:
    def __init__(self):
        os.environ['GOOGLE_API_KEY'] = "AIzaSyAWBU58WEPq9JkwWFhr-q9aGniUIfrXlJE"
        genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def to_markdown(self, text):
        pass
    
    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text