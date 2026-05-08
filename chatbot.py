# chatbot.py

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

from faqs import faqs

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower().strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

faq_questions = [faq["question"] for faq in faqs]
cleaned_faq_questions = [preprocess(q) for q in faq_questions]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(cleaned_faq_questions)

def get_response(user_question, threshold=0.32):
    if not user_question or not str(user_question).strip():
        return "Please ask something about Artificial Intelligence."

    cleaned = preprocess(user_question)
    user_vec = vectorizer.transform([cleaned])
    
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]

    if best_score < threshold:
        return "Sorry, this question is not related to Artificial Intelligence. Try asking about AI concepts, Machine Learning, Deep Learning, or Generative AI."

    return faqs[best_idx]["answer"]