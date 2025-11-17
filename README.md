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
