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


## Introduction

AI Studio workshop is a set of labs that covers LLM App development capabilities...
Content can be used in a one-to-many delivery session in a workshop format.

Each lab goes through the implementation of a use-case in detailed steps and can be done separately.

[Azure AI Studio documentation](https://learn.microsoft.com/en-us/azure/ai-studio/what-is-ai-studio?tabs=home)

![Header Image](./media/openai-workshop.png

## Table of Contents
- [PART1 - INTRO to AI STUDIO - UI PATH](#part1---intro-to-ai-studio---ui-path)
- [PART2 - BUILD LLM APPS with AI STUDIO - "CODE FIRST" APPROACH](#part2---build-llm-apps-with-ai-studio---code-first-approach)
- [PART3 - BUILD ADVANCED CHAT UI's with Azure AI Studio](#part3---build-advanced-chat-uis-with-azure-ai-studio)
- [PART4 - Evaluate your AI Apps with Azure AI Studio](#part4---evaluate-your-ai-apps-with-azure-ai-studio)
- [PART5 - ADVANCED DATA INTEGRATION in AI STUDIO](#part5---advanced-data-integration-in-ai-studio)
- [PART6 - AI STUDIO LLMOPS with GITHUB INTEGRATION](#part6---ai-studio-llmops-with-github-integration)
- [PART7 - AGENCY FLOWS in AI STUDIO](#part7---agency-flows-in-ai-studio)
- [PART8 - SCALABLE AZURE AI APP INFRASTRUCTURES](#part8---scalable-azure-ai-app-infrastructures)
- [PART9 - LOGGING & OBSERVABILITY for LLM Apps on Azure AI Studio](#part9---logging--observability-for-llm-apps-on-azure-ai-studio)
- [Contributing](#contributing)
- [License](#license)
- [Connect](#connect)

## PART1 - INTRO to AI STUDIO - UI PATH (DAG FLOW's)
- [**AI Studio - Introduction**](./Labs/Lab0%20-%20Introduction%20to%20PromptFlow%20&%20AIStudio/AI%20Studio-GettingStarted.md)
- ### 1.1 - Basics - Build a Wikipedia ChatApp with AI Studio** </span>
    - [**Setting Up the Environment**](./Labs/Lab1%20-%20WikiPediaChatApp/1.1SettingUptheEnv.md)
    - [**Getting Familiar with PromptFlow**](./Labs/Lab1%20-%20WikiPediaChatApp/1.2GettingFamiliarWithPromptFlow.md)
    - [**Create a Basic Chat Flow**](./Labs/Lab1%20-%20WikiPediaChatApp/1.3CrateaBasicChatFlow.md)
        - [Add non-OpenAI models as MaaS](./Labs/Lab1%20-%20WikiPediaChatApp/1.3.1AddOpenWeightModelsasMaaS.md) 
        - [Understand PromptFlow "Tools" & Handle chat history with simple flow examples](./Labs/Lab1%20-%20WikiPediaChatApp/1.3.2BasicFlow.md)
        - [Prompt Tuning with "Prompt Variants"](./Labs/Lab1%20-%20WikiPediaChatApp/1.3.3PromptTuningwithPromptTool.md)
    - [**Create a Wikipedia Chat App**](./Labs/Lab1%20-%20WikiPediaChatApp/1.4CreateAWikiPediaChatApp.md)
    - Add a model routing layer with Phi3 & Promptflow Function Calling support

- ### 1.2 - Build a RAG chat app with AI Studio
    - [**RAG based chatbot with Vector Index Creation**](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.1CreateVectorIndex.md)
    - [**Deploying the RAG App**](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.2DeployingApp.md)
    - [**Add a Content Safety Filter to your Chatbot**](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.3AzureAIContentSafety.md)
    - [**Evaluate your RAG based Chatbot**](./Labs/Lab2%20-%20PersonalFinanceRecommender/2.4Eval.md)
    - Monitor your chatbot in production with PromptFlow inference metrics

*REST OF THE WORKSHOP is currently under CONSTRUCTION. Here is a sneak peek into what's upcoming...*

## PART2 - BUILD LLM APPS with AI STUDIO - "CODE FIRST" APPROACH (FLEX FLOW's)
- ### 2.1 **Build, Trace & Deploy LLM Apps with Azure AI SDK**
    - [**Developing LLMApps with PromptFlow SDK**](./Labs/PART2%20/1-CodeFirstDev/pf-main.md)
        - [**PromptFlow Core Concepts**](./Labs/PART2%20/1-CodeFirstDev/pf-concepts.md)
        - [**Installing the PromptFlow SDK**](./Labs/PART2%20/1-CodeFirstDev/pf-sdk-setup.md)
        - [**Your first LLM App with the PromptFlow SDK**](./Labs/PART2%20/1-CodeFirstDev/first-pf-sdk-app.md)
        - [**PromptFlow VSCode Plugin**](./Labs/PART2%20/1-CodeFirstDev/pf-vscode-plugin.md)
        - **Using Prompti with PromptFlow** 
            - [**What is Prompti & How it can help?**](./Labs/PART2%20/1-CodeFirstDev/prompti.md)
            - [**Using Prompti with PromptFlow**](./Labs/PART2%20/1-CodeFirstDev/prompti-pf.md)  
        - [**Debugging and Tracing with PromptFlow**](./Labs/PART2%20/1-CodeFirstDev/pf-tracing.md)

              

    - [**Use PromptFlow in the Cloud with Azure AI SDK**](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow?view=azureml-api-2)
        - **Azure Azure AI SDK - When do we need it?**
        - [**Installing the Azure AI SDK**](./Labs/PART2%20/1-CodeFirstDev/1-EnvSetup.md)
        - **Sample App with Azure AI SDK**
        - **Quick-start templates with azure developer CLI**
        - **Integration with AI Toolkit & Visual Studio Code**
    - **Prompti**
  


   
- ### 2.2 - Build a financial advice generator using AI Studio, AOAI, Phi3 and CosmosDB**
    - Create a PostgreSQL / CosmosDB instance 
    - Create a customer database within PostgreSQL 
    - Create a DB connection in PromptFlow 
    - Deploy and integrate Phi-3 as an RTE 
    - Create a text2sql DB enrichment flow 
    - Create a new summarisation flow with Phi3 
    - Create a RAG flow with IMF Economic Outlook document 
    - Integrate three separate flows and build the financial recommender 

 - ### 2.3 Deploying PromptFlow apps to Azure VMs, AppService, and Kubernetes
    - Deploying to Azure VM's 
    - Deploying to AppService 
    - Deploying to AKS - Azure Kubernetes Service

- ### 2.4 Tracing GenAI Apps in Azure AI Studip 


## PART3 - BUILD ADVANCED CHAT UI's with Azure AI Studio 
- Lab3.1 CosmosDB as ChatHistory logging

## PART4 - Evaluate your AI Apps with Azure AI Studio 
- Lab - Advanced automated Eval 

## PART5 - ADVANCED DATA INTEGRATION in AI STUDIO 
- **Lab6 - Advanced RAG Patterns**
    - Lab6.1 Agentic RAG 
    - Lab6.2 Graph RAG with CosmosDB 

## PART6 - AI STUDIO LLMOPS with GITHUB INTEGRATION  
- **Lab7 - LLMOPS with GitHub / PromptFlow Integration**

## PART7 - AGENCY FLOWS in AI STUDIO  
- **Lab8 - AutoGen integration through FlexFlows**

## PART8 - SCALABLE AZURE AI APP INFRASTRUCTURES 
- Lab - Multi-region AOAI deployments 
- Lab - Azure API Management Integration - AAA, enforce rate-limits, LB across AOAI endpoints 
- Lab - Redis as an LLM cache 
- Lab - Model routers for multi-model LLM Apps on AI Studio 

## PART9 - LOGGING & OBSERVABILITY for LLM Apps on Azure AI Studio 


## PART10 - ASSISTANTS API in AI Studio 

## Contributing

Please read the contributing guidelines for more information.

## License
Copyright OzgurGuler. All rights reserved.

This project is licensed under the MIT License - see the LICENSE file for details.

## Connect

Connect with me on LinkedIn:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/ozguler/)
