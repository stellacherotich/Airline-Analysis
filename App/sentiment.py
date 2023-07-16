import streamlit as st
import pickle

# Load the pre-trained sentiment analysis model
with open('App/sentiment_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

def get_sentiment_type(sentiment_label):
    if sentiment_label == -1:
        return "Negative"
    elif sentiment_label == 0:
        return "Neutral"
    elif sentiment_label == 1:
        return "Positive"
    else:
        return "Unknown"

def main():
    st.set_page_config(page_title="Sentiment Analysis App", page_icon="✈️")

    # Custom CSS style
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #DAA520;
            color: #000000;
        }
        .stButton button {
            background-color: #DAA520;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Airline Sentiment Analysis App")

    # Input text for prediction
    input_text = st.text_area("Enter text:")

    if st.button("Predict"):
        # Perform sentiment prediction using the loaded model
        sentiment_label = pipeline.predict([input_text])[0]
        confidence = pipeline.predict_proba([input_text]).max()

        # Get the sentiment type based on the sentiment label
        sentiment_type = get_sentiment_type(sentiment_label)

        # Show the prediction result
        st.write("Sentiment Label:", sentiment_label)
        st.write("Sentiment Type:", sentiment_type)
        st.write("Confidence:", confidence)

if __name__ == "__main__":
    main()
