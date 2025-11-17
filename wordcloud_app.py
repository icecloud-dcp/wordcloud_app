import importlib.util
import sys
from collections import Counter

REQUIRED_DEPENDENCIES = ("streamlit", "wordcloud", "matplotlib")


def find_missing_dependencies():
    return [name for name in REQUIRED_DEPENDENCIES if importlib.util.find_spec(name) is None]


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


def run_streamlit_app():
    plt, st, WordCloud = import_dependencies()

    st.title("Word Cloud Generator")

    text_input = st.text_area("Enter text here:")

    if st.button("Generate Word Cloud"):
        if text_input:
            generate_wordcloud(text_input, WordCloud, plt, st)
        else:
            st.warning("Please enter some text.")


def build_cli_cloud(text):
    words = [word.strip() for word in text.split() if word.strip()]
    if not words:
        return []

    counts = Counter(words)
    max_count = max(counts.values())
    lines = [
        f"{word}: " + ("#" * max(1, counts[word] * 10 // max_count))
        for word, _ in counts.most_common()
    ]
    return lines


def run_cli_fallback(missing):
    missing_list = ", ".join(missing)
    print(
        "Dependencies are missing, so running in CLI mode instead of Streamlit.\n"
        f"Missing packages: {missing_list}."
    )
    print("Enter text to build a simple ASCII word cloud (Ctrl-D to submit):")
    text = sys.stdin.read().strip()
    if not text:
        text = input("Text: ").strip()

    if not text:
        print("No text provided; nothing to render.")
        return

    lines = build_cli_cloud(text)
    if not lines:
        print("No words detected in input.")
        return

    print("\nASCII word cloud:\n")
    for line in lines:
        print(line)


def main():
    missing = find_missing_dependencies()
    if missing:
        run_cli_fallback(missing)
        return

    run_streamlit_app()


if __name__ == "__main__":
    main()
