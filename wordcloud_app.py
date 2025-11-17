import importlib.util
import sys

REQUIRED_DEPENDENCIES = ("streamlit", "wordcloud", "matplotlib")


def find_missing_dependencies():
    return [name for name in REQUIRED_DEPENDENCIES if importlib.util.find_spec(name) is None]


def ensure_dependencies():
    missing = find_missing_dependencies()
    if missing:
        missing_list = ", ".join(missing)
        sys.exit(
            "Cannot start the app because required packages are not installed: "
            f"{missing_list}. Install them with 'pip install -r requirements.txt'."
        )


def import_dependencies():
    import matplotlib.pyplot as plt
    import streamlit as st
    from wordcloud import WordCloud

    return plt, st, WordCloud


def generate_wordcloud(text, WordCloud, plt, st):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

def main():
    ensure_dependencies()
    plt, st, WordCloud = import_dependencies()

    st.title("Word Cloud Generator")

    text_input = st.text_area("Enter text here:")

    if st.button("Generate Word Cloud"):
        if text_input:
            generate_wordcloud(text_input, WordCloud, plt, st)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
