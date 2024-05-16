# AZURE AI STUDIO WORKSHOP - Ozgur Guler
[![GitHub stars](https://img.shields.io/github/stars/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/network)
[![License](https://img.shields.io/github/license/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/blob/main/LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ozgurgulerx/aistudio-workshop-ozguler/your-workflow.yml?branch=main)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/actions)
[![Open Issues](https://img.shields.io/github/issues/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/issues)
[![Contributors](https://img.shields.io/github/contributors/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/commits/main)
[![Code Size](https://img.shields.io/github/languages/code-size/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler)
[![Languages](https://img.shields.io/github/languages/top/ozgurgulerx/aistudio-workshop-ozguler)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler)
[![Watchers](https://img.shields.io/github/watchers/ozgurgulerx/aistudio-workshop-ozguler?style=social)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/watchers)
[![Version](https://img.shields.io/github/v/release/ozgurgulerx/aistudio-workshop-ozguler?include_prereleases)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/releases)
[![Downloads](https://img.shields.io/github/downloads/ozgurgulerx/aistudio-workshop-ozguler/total)](https://github.com/ozgurgulerx/aistudio-workshop-ozguler/releases)

AI Studio workshop is a set of labs that covers LLM App development capabilities...
Content can be used in a one-to-many delivery session in a workshop format.

Each lab goes through implementation of a use-case in detailed steps can be done seperately.

[Azure AI Studio documentation](https://learn.microsoft.com/en-us/azure/ai-studio/what-is-ai-studio?tabs=home)


##  PART1 - INTRO to AI STUDIO - UI PATH 
- [**AI Studio - Introduction**](./Labs/Lab0%20-%20Introduction%20to%20PromptFlow%20&%20AIStudio/AI%20Studio-GettingStarted.md)

- <span style="color: yellow;">**Lab1 - Basics - Build a Wikpedia ChatApp with AI Studio** </span>
    - [Lab1.1 Setting Up the Environment](./Labs/Lab1%20-%20WikiPediaChatApp/1.1SettingUptheEnv.md)
    - [Lab1.2 Getting Familiar with PromptFlow](/Labs/Lab1%20-%20WikiPediaChatApp/1.2GettingFamiliarWithPromptFlow.md)
    - [Lab1.3 Create a Basic Chat Flow](/Labs/Lab1%20-%20WikiPediaChatApp/1.3CrateaBasicChatFlow.md)
        - [1.3.1 Add non-OpenAI models as MaaS](./Labs/Lab1%20-%20WikiPediaChatApp/1.3.1AddOpenWeightModelsasMaaS.md) 
        - [1.3.2 Understand PromptFlow "Tools" & Handle chat history with simple flow examples](./Labs/Lab1%20-%20WikiPediaChatApp/1.3.2BasicFlow.md)
        - [1.3.3 Prompt Tuning with "Prompt Variants"](./Labs/Lab1%20-%20WikiPediaChatApp/1.3.3PromptTuningwithPromptTool.md)
    - [Lab1.4 Create a Wikipedia Chat App -includes input/output mapping & conditional activation](/Labs/Lab1%20-%20WikiPediaChatApp/1.4CreateAWikiPediaChatApp.md)
    - Lab1.5 Add a model routing layer with Phi3 & Promptflow Function Calling suppport

- <span style="color:yellow"> **Lab2 - Build a RAG chat app with AI Studio</span>** 

    - [Lab2.1 - RAG based chatbot with Vector Index Creation](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.1CreateVectorIndex.md)
    - [Lab2.2 - Deploying the RAG App](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.2DeployingApp.md)
    - [Lab2.3 - Add a Content Safety Filter to your Chatbot](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.3AzureAIContentSafety.md)
    - [Lab2.4 - Evaluate your RAG based Chatbot ](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.4Eval.md)
    - Lab2.5 -  monitor your chatbot in production with PromptFlow inference metrics


*REST OF THE WORKSHOP is currently under CONSTRUCTION. Here is a sneak peek into what's upcoming...*
*REST OF THE WORKSHOP is currently under CONSTRUCTION. Here is a sneak peek into what's upcoming...*




##  PART2  - BUILD LLM APPS with AI STUDIO - "CODE FIRST" APPROACH 
- ### **2.1 Build & Deploy LLM Apps with Azure AI SDK on VSCode**
    - [2.1.1 Setting Up the Dev Environment on VSCode](./Labs/PART2%20/1-CodeFirstDev/1-EnvSetup.md)
    - [2.1.2 Install Azure AI SDK to your environment](./Labs/PART2%20/1-CodeFirstDev/2-AzureAISDK.md)


- **Lab4 - Build a financial advise generator using AI Studio, AOAI, Phi3 and Cosmosdb**
    - Lab3.1 - Create a PostgreSQL / Cosmosdb db instance 
    - Lab3.2 - Create a customer database within PostgreSQL 
    - Lab3.3 - Create a db connection in PromptFlow 
    - Lab3.4 - Deploy and integrate Phi-3 as an RTE 
    - Lab3.5 - Create a text2sql db enrichmenet flow 
    - Lab3.6 - Create a new summarisation flow with Phi3 
    - Lab3.7 - Create a RAG flow with IMF Economic Outlook document 
    - Lab3.8 - Integrate three seperate flows and build the financial recommmender 

     - [Lab4.1 - Setting up your development environment in VSCode](./Labs/Lab4%20-%20CodeFirstDev/4.1%20EnvSetup.md)
- [Lab5 - Deploying PromptFlow apps to Azure VM's, AppService and Kubernetes](./)

## PART3 - BUILD ADVANCED CHAT UI's with Azure AI Studio 
- Lab3.1 - Cosmosdb as ChatHistory logging
## PART4 - Evaluate your AI Apps with Azure AI Studio 
- Lab - Advanced automated Eval 

## PART5 - ADVANCED DATA INTEGRATION in AI STUDIO 
- **Lab6 - Advanced RAG Patterns**
    - Lab6.1 - Agentic RAG 
    - Lab6.2 - Graph RAG with Cosmosdb 
- **Lab7 - Azure AI Studio / Fabric Integrations**

## PART6 - AI STUDIO LLMOPS with GITHUB INTEGRATION  
- **Lab8 - LLMOPS with GitHub / PromptFlow Integration**

## PART7 - AGENCY FLOWS in AI STUDIO  
- **Lab9 - AutoGen integration through FlexFlows**

## PART8 - SCALABLE AZURE AI APP INFRASTRUCTURES 
- Lab - multi-region AOAI deployments 
- Lab - Azure API Management Integration - AAA, enforce rate-limits, LB across AOAI endpoints 
- Lab - Redis as an LLM cache 
- Lab - model routers for multi-model LLM Apps on AI Studio 

## PART9 - LOGGING & OBSERVABILITY for LLM Apps on Azure AI Studio 