# wordcloud_app
Use ChatGPT to create engaging and concise summaries for our blog posts with Streamlit.

## Installation

1. Create and activate a virtual environment if desired.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

If you are in an environment with a forced proxy that blocks access to PyPI (e.g., `Tunnel connection failed: 403 Forbidden`), either clear the proxy variables for the install command or install from a local wheelhouse:

```bash
# Option A: ignore proxy
env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY \
    PIP_NO_PROXY=* pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Option B: offline/local mirror
pip install --no-index --find-links /path/to/wheelhouse -r requirements.txt
```

## Running the app

```bash
streamlit run wordcloud_app.py
```

If the Streamlit dependencies are unavailable (for example, in an offline environment),
the script will fall back to a simple CLI mode that generates an ASCII word cloud from
text provided via standard input or a prompt:

```bash
python wordcloud_app.py <<'TEXT'
This is an offline word cloud example that will render in the terminal
TEXT
```
