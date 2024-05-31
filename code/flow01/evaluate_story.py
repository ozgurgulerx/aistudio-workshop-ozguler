from promptflow.core import Prompty, tool
from dotenv import load_dotenv
import os

# Load environment variables if not already set
if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
    load_dotenv()

@tool
def evaluate_story(story: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    evaluation_prompty_file_path = os.path.join(current_dir, "story_evaluation.prompty")
    print(evaluation_prompty_file_path)

    # Load prompty as a flow
    evaluation_prompty_flow = Prompty.load(evaluation_prompty_file_path)
    evaluation_result = evaluation_prompty_flow(story=story)
    
    return evaluation_result

if __name__ == "__main__":
    import json
    import sys

    json_input = sys.argv[1]  # Assume the input is passed as a JSON string
    args = json.loads(json_input)

    result = evaluate_story(**args)
    print(result)

