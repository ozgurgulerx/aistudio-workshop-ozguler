import json
import os 

from pathlib import Path
folder = Path(__file__).parent.absolute().as_posix()

from promptflow.core import tool, Prompty

@tool
def flow_entry(    
      question: any
) -> str:
  # path to prompty (requires absolute path for deployment)
  path_to_prompty = folder + "/chat.prompty"
  load_dotenv()

  # load prompty as a flow
  flow = Prompty.load(path_to_prompty)
 
  # execute the flow as function
  result = flow(
    question = question
  )

  return result

if __name__ == "__main__":
   json_input = '''{
  "question": "What is Prompt flow?"
}'''
   args = json.loads(json_input)

   result = flow_entry(**args)
   print(result)
