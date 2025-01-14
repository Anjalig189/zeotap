from typing import List, Dict
import re
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CDPChatbot:
    def __init__(self):
        # Initialize NLTK components
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Store documentation content for each CDP
        self.docs = {
            'segment': self.fetch_documentation('https://segment.com/docs/?ref=nav'),
            'mparticle': self.fetch_documentation('https://docs.mparticle.com/'),
            'lytics': self.fetch_documentation('https://docs.lytics.com/'),
            'zeotap': self.fetch_documentation('https://docs.zeotap.com/home/en-us/')
        }
        
        # Create index for documentation
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = {}
        self.index_documentation()

    def fetch_documentation(self, url: str) -> List[Dict]:
        """
        Fetch and parse documentation from given URL
        Note: This is a simplified version. In production, you'd need proper web scraping
        with rate limiting and respect for robots.txt
        """
        try:
            # In real implementation, you would:
            # 1. Properly scrape the documentation
            # 2. Handle rate limiting
            # 3. Store results in a database
            # 4. Implement caching
            return []  # Placeholder for actual implementation
        except Exception as e:
            print(f"Error fetching documentation: {e}")
            return []

    def preprocess_text(self, text: str) -> str:
        """Preprocess text by tokenizing, removing stopwords, and lemmatizing"""
        tokens = word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and token.isalnum()]
        return ' '.join(tokens)

    def index_documentation(self):
        """Create TF-IDF vectors for all documentation content"""
        for cdp, docs in self.docs.items():
            processed_docs = [self.preprocess_text(doc['content']) 
                            for doc in docs]
            self.doc_vectors[cdp] = self.vectorizer.fit_transform(processed_docs)

    def identify_cdp(self, question: str) -> str:
        """Identify which CDP the question is about"""
        cdps = ['segment', 'mparticle', 'lytics', 'zeotap']
        for cdp in cdps:
            if cdp in question.lower():
                return cdp
        return None

    def is_cdp_question(self, question: str) -> bool:
        """Determine if the question is CDP-related"""
        cdp_keywords = ['cdp', 'customer data platform', 'segment', 'mparticle', 
                       'lytics', 'zeotap', 'integration', 'source', 'audience',
                       'profile', 'data']
        return any(keyword in question.lower() for keyword in cdp_keywords)

    def find_most_relevant_docs(self, question: str, cdp: str) -> List[Dict]:
        """Find most relevant documentation sections for the question"""
        processed_question = self.preprocess_text(question)
        question_vector = self.vectorizer.transform([processed_question])
        
        similarities = cosine_similarity(question_vector, 
                                      self.doc_vectors[cdp]).flatten()
        most_relevant_indices = np.argsort(similarities)[-3:][::-1]
        
        return [self.docs[cdp][i] for i in most_relevant_indices]

    def generate_response(self, question: str) -> str:
        """Generate response based on the question"""
        # Check if question is CDP-related
        if not self.is_cdp_question(question):
            return "I can only answer questions about Customer Data Platforms (CDPs). Please ask me about Segment, mParticle, Lytics, or Zeotap."

        # Identify which CDP is being asked about
        cdp = self.identify_cdp(question)
        if not cdp:
            return "Please specify which CDP you're asking about (Segment, mParticle, Lytics, or Zeotap)."

        # Find relevant documentation
        relevant_docs = self.find_most_relevant_docs(question, cdp)
        
        if not relevant_docs:
            return f"I couldn't find specific information about that in the {cdp} documentation. Could you rephrase your question?"

        # Generate response from relevant documentation
        response = f"Here's how to do that in {cdp}:\n\n"
        for i, doc in enumerate(relevant_docs, 1):
            response += f"{i}. {doc['content']}\n"
        
        return response

    def handle_comparison_question(self, question: str) -> str:
        """Handle questions comparing different CDPs"""
        cdps_mentioned = [cdp for cdp in self.docs.keys() 
                         if cdp in question.lower()]
        
        if len(cdps_mentioned) < 2:
            return "For CDP comparisons, please mention the specific CDPs you'd like to compare."

        # Find relevant docs for each CDP
        comparison = "Here's a comparison:\n\n"
        for cdp in cdps_mentioned:
            relevant_docs = self.find_most_relevant_docs(question, cdp)
            comparison += f"{cdp.capitalize()}:\n"
            for doc in relevant_docs:
                comparison += f"- {doc['content']}\n"
            comparison += "\n"
        
        return comparison

def main():
    chatbot = CDPChatbot()
    
    print("CDP Support Chatbot initialized. Type 'quit' to exit.")
    
    while True:
        question = input("\nHow can I help you? ")
        
        if question.lower() == 'quit':
            break
            
        if "compare" in question.lower() or "difference" in question.lower():
            response = chatbot.handle_comparison_question(question)
        else:
            response = chatbot.generate_response(question)
            
        print("\n" + response)

if __name__ == "__main__":
    main()