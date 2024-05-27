# PromptFlow Core Concepts 

## DAG Flows 

In the context of PromptFlow, an “LLM flow” refers to a DAG-Directed Acyclic Graph-'s (acylic referring to flow's that are not cyclic) workflow or a sequence of function calls (tools in PromptFlow terminology) designed to utilize LLMs for various tasks. PromptFlow is a tool that helps in creating, managing, and optimizing these workflows, making it easier to integrate LLM capabilities into applications.

Key Components of an LLM Flow in PromptFlow

	1.	Prompts: The input queries or instructions that you provide to the LLM. These can be dynamically generated based on user input or predefined templates.
	2.	Models: The LLMs that process the prompts. This could be any LLM available through PromptFlow, including models from OpenAI, Azure OpenAI, or other providers.
	3.	Context Management: Handling the context in which the prompts are processed. This includes managing conversation history, maintaining state, and ensuring the model has the necessary information to generate relevant responses.
	4.	Data Preprocessing and Postprocessing: Steps to prepare input data for the model and to process the output data from the model. This can involve text normalization, filtering, formatting, and more.
	5.	API Integration: Using APIs to interact with the LLM, send prompts, and receive responses. PromptFlow often provides APIs to streamline this process.
	6.	Logic and Control Flow: Implementing logic to handle different scenarios based on the LLM’s responses. This includes branching, looping, and conditionally executing different parts of the workflow.
	7.	Error Handling: Mechanisms to manage errors or unexpected results from the LLM, ensuring robustness and reliability of the flow.

    A DAG flow represented as a YAML file (flow.dag.yaml) and can be visualized with our Prompt flow for VS Code extension (more on this in the VSCode extension part!).