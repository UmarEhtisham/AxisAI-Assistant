# utils/save_credentials.py

def save_credentials(llm_choice: str, api_key: str) -> bool:
    """
    Save API credentials based on the selected LLM choice.

    Args:
        llm_choice (str): The name of the LLM company.
        api_key (str): The API key/token to save.
    """
    api_keys = {
        "OpenAI": "OPENAI_API_KEY",
        "Google Gemini": "GOOGLE_API_KEY",
        "HuggingFace": "HUGGINGFACE_API_TOKEN",
        "ChatGroq": "CHATGROQ_API_KEY",
        "Anthropic": "ANTHROPIC_API_KEY"
    }

    if llm_choice in api_keys:
        env_variable = api_keys[llm_choice]
        with open('.env', 'w') as file:
            file.write(f"{env_variable}='{api_key}'")
        return True
    else:
        False
