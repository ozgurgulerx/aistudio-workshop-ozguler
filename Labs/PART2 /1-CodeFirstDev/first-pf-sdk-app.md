# First App with PF SDK 

Prompty is announced at MS Build 2024, intends to turn prompts to coding assets. 
Refer to [Prompty.md] for more...

## Create your prompt as a Prompty file
```
---
name: Minimal Chat
model:
  api: chat
  configuration:
    type: azure_openai
    azure_deployment: gpt-35-turbo
  parameters:
    temperature: 0.2
    max_tokens: 1024
inputs:
  question:
    type: string
sample:
  question: "What is Prompt flow?"
---

system:
You are a helpful assistant.

user:
{{question}}
```

## Create a Flow 

```
import os

from dotenv import load_dotenv
from pathlib import Path
from promptflow.tracing import trace
from promptflow.core import Prompty

BASE_DIR = Path(__file__).absolute().parent

@trace
def chat(question: str = "What's the capital of France?") -> str:
    """Flow entry function."""

    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        # load environment variables from .env file
        load_dotenv()

    prompty = Prompty.load(source=BASE_DIR / "chat.prompty")
    # trigger a llm call with the prompty obj
    output = prompty(question=question)
    return output

if __name__ == "__main__":
    from promptflow.tracing import start_trace

    start_trace()

    result = chat("What's the capital of France?")
    print(result)