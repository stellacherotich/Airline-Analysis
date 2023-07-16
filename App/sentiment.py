import streamlit as st

def main():
    st.set_page_config(page_title="Sentiment Analysis App", page_icon=":smiley:")

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

    st.title("Sentiment Analysis App")

    # Input text for prediction
    input_text = st.text_area("Enter text:")

    if st.button("Predict"):
        # Perform sentiment prediction (replace this with your actual prediction code)
        sentiment_label = "POSITIVE"
        confidence = 0.95

        # Show the prediction result
        st.write("Sentiment Label:", sentiment_label)
        st.write("Confidence:", confidence)

if __name__ == "__main__":
    main()
