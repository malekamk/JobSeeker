import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

class ResumeParser:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
    
    def parse_resume(self, resume_text):
        doc = self.nlp(resume_text)
        experience = self.extract_experience(doc)
        # Return or process experience as needed
        return experience, None  # Adjust based on your implementation

    def extract_experience(self, doc):
        # Define your list of experience keywords or phrases
        experience_keywords = ["experience", "worked at", "role", "job", "position"]
        
        extracted_experience = []
        for sent in doc.sents:
            sentence_text = sent.text.lower()
            # Check if any keyword is in the sentence
            for keyword in experience_keywords:
                if keyword in sentence_text:
                    extracted_experience.append(sent.text)
                    break  # Stop checking after finding the first match in this sentence
        
        return extracted_experience

