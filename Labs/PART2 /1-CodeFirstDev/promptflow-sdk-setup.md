# GenAI App Development with PromptFlow SDK
![Alt text](../../../media/dalle02%20copy.png) 

PromptFlow is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications, from ideation, prototyping, testing, evaluation to production deployment and monitoring. It makes prompt engineering much easier and enables you to build LLM apps with production quality.

In this section you'll learn how to leverage the Promptflow SDK to streamline your LLM-based application development workflow. This workshop is designed for developers who are experienced in Python programming and are looking to enhance their capabilities in LLMOps.

PromptFlow UI is good for visually inspecting evaluation results and for flow traces. For the rest of the development tasks "code-first approach" with PromptFlow SDK is recommended.

You can refer to the following documentation for further details on PromptFlow...

- MS Learn Documentation [Code First: Dev to Prod](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-integrate-with-llm-app-devops?view=azureml-api-2&tabs=cli)

- [PromptFlow GitHub Documentation](https://microsoft.github.io/promptflow/index.html#)


## Install the PromptFlow SDK 

With PromptFlow SDK you can develop your prompts locally. \
You can then seamlessly integrate your flow to Azure ML or Azure AI Studio.

To install the promptflow SDK use...
```
pip install promptflow
pip install --upgrade python-dotenv
```


Confirm the required packages are installed...
```
pip list | grep promptflow
```
![Alt text](../../../media/74.png) 

Confirm the installation...
pip list | grep promptflow

```
pf --version 
```
![Alt text](../../../media/75.png)

### Add AOAI endpoint and key as environment variables
Create a file named .env in your project directory with the following content:

```
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
```
![Alt text](../../../media/73.png) 

