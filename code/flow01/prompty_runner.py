from promptflow.core import Prompty
from promptflow.core import tool
from dotenv import load_dotenv

import os

@tool
def run_prompty_tool(theme: str) -> str:
    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Adjust the path to point to the flow01 directory
    prompty_file_path = os.path.join(current_dir, "creative_writing_assistant.prompty")
    print(prompty_file_path)
    
    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
    # load environment variables from .env file
        load_dotenv()

    # Load prompty as a flow
    prompty_flow = Prompty.load(prompty_file_path)
    
    
    # Execute the flow as a function
    result = prompty_flow(theme=theme)
    return result

if __name__ == "__main__":
    import json
    import sys

    json_input = sys.argv[1]  # Assume the input is passed as a JSON string
    args = json.loads(json_input)

    result = run_prompty(**args)
    print(result)
