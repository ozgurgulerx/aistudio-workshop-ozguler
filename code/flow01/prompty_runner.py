from promptflow.core import Prompty
import os


def run_prompty(theme):
    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    prompty_file_path = os.path.join(current_dir, "creative_writing_assistant.prompty")
    
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
