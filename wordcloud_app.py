import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def main():
    st.title("Word Cloud Generator")

    text_input = st.text_area("Enter text here:")

    if st.button("Generate Word Cloud"):
        if text_input:
            generate_wordcloud(text_input)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
