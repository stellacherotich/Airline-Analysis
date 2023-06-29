import streamlit as st
from transformers import pipeline

# Load the pre-trained text classification model using TensorFlow backend
sentiment_classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

def main():
    st.title("Sentiment Text Classifier")

    text = st.text_input("Enter a text:")
    if st.button("Analyze"):
        result = sentiment_classifier(text)
        sentiment = result[0]['label']
        score = result[0]['score']

        st.write(f"Sentiment: {sentiment}")
        st.write(f"Score: {score}")

if __name__ == '__main__':
    main()
