# utils/save_credentials.py
from utils.constants import PROVIDERS
# Function to save credentials
def save_credentials(llm_choice: str, api_key: str):
    """
    Save API credentials based on the selected LLM choice.

    Args:
        llm_choice (str): The name of the LLM company.
        api_key (str): The API key/token to save.

    Returns:
        bool: True if the credentials were saved successfully.
    """
    for company in PROVIDERS:
        if llm_choice == company:
            try:
                with open('.env', 'w') as file:
                    file.write(f"{PROVIDERS[company]}='{api_key}'")
            except Exception as e:
                raise e
    return True
