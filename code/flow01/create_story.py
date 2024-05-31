from promptflow.core import Prompty, tool
from dotenv import load_dotenv
import os

# Load environment variables if not already set
if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
    load_dotenv()

@tool
def create_story(theme: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    prompty_file_path = os.path.join(current_dir, "creative_writing_assistant.prompty")
    print(prompty_file_path)

    # Load prompty as a flow
    prompty_flow = Prompty.load(prompty_file_path)
    result = prompty_flow(theme=theme)
    
    return result

if __name__ == "__main__":
    import json
    import sys

    json_input = sys.argv[1]  # Assume the input is passed as a JSON string
    args = json.loads(json_input)

    result = create_story(**args)
    print(result)
