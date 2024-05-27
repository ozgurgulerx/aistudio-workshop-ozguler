# PromptFlow Core 

PromptFlow is a tool that helps in creating, managing, and optimizing these workflows, making it easier to integrate LLM capabilities into applications. 

## FLOWS 
### DAG Flows 

In the context of PromptFlow, an “LLM flow” refers to a DAG-Directed Acyclic Graph-'s (acylic referring to flow's that are not cyclic) workflow or a sequence of function calls (**tools** in PromptFlow terminology) designed to utilize LLMs for various tasks. These functions/tools are connected via input/output dependencies and executed based on the topology by prompt flow executor.

A DAG flow represented as a YAML file (flow.dag.yaml) and can be visualized with our Prompt flow for VS Code extension (more on this in the VSCode extension part!).

DAG flows provides an UI-friendly way to develop your LLM app, which has the following benifits:
- Low code: user can drag-and-drop in UI to create a LLM app.
- DAG Visualization: user can easily understand the logic structure of the app with DAG view.
 
 ### FLEX Flows 

You can create LLM apps using a Python function or class as the entry point, which encapsulating your app logic. You can directly test or run these with pure code experience. Or you can define a flow.flex.yaml that points to these entries, which enables testing, running, or viewing traces via the Promptflow VS Code Extension.

## TOOLS 

The current list of PromptFlow tools please visit PromptFlow

## CONNECTIONS 
