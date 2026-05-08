# faqs.py - Artificial Intelligence Basics FAQs

faqs = [
    {
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence (AI) is the ability of machines or computers to perform tasks that normally require human intelligence, such as learning, reasoning, problem-solving, and understanding language."
    },
    {
        "question": "What is the difference between AI and Machine Learning?",
        "answer": "AI is the broad field of creating intelligent machines. Machine Learning (ML) is a subset of AI where systems learn patterns from data without being explicitly programmed for every task."
    },
    {
        "question": "What is Deep Learning?",
        "answer": "Deep Learning is a subset of Machine Learning that uses multi-layered artificial neural networks to learn from large amounts of data. It is especially good for image recognition, speech, and complex patterns."
    },
    {
        "question": "How does AI learn?",
        "answer": "AI learns mainly through Machine Learning by analyzing large amounts of data, finding patterns, and improving its performance over time with more data and feedback."
    },
    {
        "question": "What are the main types of AI?",
        "answer": "There are mainly two types: Narrow AI (or Weak AI) which performs specific tasks (like Siri or recommendation systems), and General AI (AGI) which can perform any intellectual task a human can do (still mostly theoretical)."
    },
    {
        "question": "What is Generative AI?",
        "answer": "Generative AI can create new content such as text, images, music, or code. Examples include ChatGPT for text and DALL-E or Grok Imagine for images."
    },
    {
        "question": "Do I need to know programming to learn AI?",
        "answer": "Basic Python programming is very helpful, but many AI tools (like ChatGPT) can be used without coding. For building AI models, learning Python, math, and libraries like scikit-learn is recommended."
    },
    {
        "question": "What are common applications of AI?",
        "answer": "AI is used in recommendation systems (Netflix, YouTube), virtual assistants (Siri, Google Assistant), self-driving cars, medical diagnosis, fraud detection, chatbots, and language translation."
    },
    {
        "question": "Is AI going to take away all jobs?",
        "answer": "AI will automate some repetitive tasks, but it also creates new jobs in AI development, data science, ethics, and AI maintenance. Learning to work with AI is becoming important."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a computing system inspired by the human brain. It consists of layers of connected nodes (neurons) that process data and learn patterns."
    },
    {
        "question": "What is the difference between supervised and unsupervised learning?",
        "answer": "Supervised learning uses labeled data (input + correct output) to train the model. Unsupervised learning finds hidden patterns in unlabeled data without guidance."
    },
    {
        "question": "Can AI make mistakes?",
        "answer": "Yes, AI can make mistakes (called hallucinations in generative AI). It depends on the quality of training data and the specific task. Always verify important information."
    },
    {
        "question": "What ethical concerns exist with AI?",
        "answer": "Major concerns include bias in algorithms, privacy of data, job displacement, deepfakes, and accountability when AI makes wrong decisions."
    },
    {
        "question": "How can a beginner start learning AI?",
        "answer": "Start with Python basics, then learn Machine Learning concepts (Coursera or free YouTube courses), practice with simple projects, and explore tools like Google Colab."
    },
    {
        "question": "What is overfitting in Machine Learning?",
        "answer": "Overfitting happens when a model learns the training data too well, including noise, and performs poorly on new unseen data."
    },
    {
        "question": "What tools or libraries are used in AI?",
        "answer": "Popular ones: Python, scikit-learn (for ML), TensorFlow and PyTorch (for Deep Learning), NLTK or spaCy (for NLP), and pandas for data handling."
    },
    {
        "question": "Is AI the same as robotics?",
        "answer": "No. AI focuses on intelligence and decision-making. Robotics is about building physical machines. Many robots use AI, but not all AI involves robots."
    },
    {
        "question": "Hello, how are you?",
        "answer": "Hello! I'm an AI FAQ Chatbot specialized in Artificial Intelligence basics. How can I help you learn about AI today?"
    },
    {
        "question": "Thank you",
        "answer": "You're welcome! Feel free to ask more questions about Artificial Intelligence."
    },
    {
        "question": "What is the future of AI?",
        "answer": "AI is expected to grow rapidly in healthcare, education, autonomous systems, and personalized services. Responsible development and ethical guidelines will be very important."
    }
]

# For testing
if __name__ == "__main__":
    print(f"Total AI FAQs loaded: {len(faqs)}")