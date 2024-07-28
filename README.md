# TL;DR Bot

A script that takes a URL to a Twitter thread and outputs a TL;DR summary using OpenAI.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/david-saint/tldr-bot-cli.git
    cd tldr-bot-cli
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv tldr_bot_cli_env
    source tldr_bot_cli_env/bin/activate  # On Windows: tldr_bot_cli_env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the script**:
    ```bash
    python bot.py
    ```

## Usage

Enter the URL of the Twitter thread when prompted to get a summarized version of the thread in bullet points.
