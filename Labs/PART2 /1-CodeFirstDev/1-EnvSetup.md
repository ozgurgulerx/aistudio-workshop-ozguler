# Why prefer "code-first" development with Azure AI SDK over AI Studio UI?
![Alt text](../../../media/p01.webp)
"Code First" development with Azure SDK offers significant advantages over simple UI-based development due to its flexibility and control, version control and collaboration, and reusability and automation. By writing code, developers can achieve fine-grained customization and implement complex logic that might be challenging or impossible through a UI. This approach also enables the use of source control systems like Git, allowing for effective tracking of changes, collaborative efforts, and the ability to roll back to previous versions if needed. Code reviews through pull requests ensure high-quality code and adherence to best practices. Moreover, code-first development promotes the reuse of components and modules across different projects, reducing redundancy and increasing efficiency. Automation is another key benefit, as infrastructure and deployments can be scripted and automated, leading to more consistent and reliable processes.

# Preparing the Dev Environment

First create an Azure AI Studio Hub resource by following [Setting Up The Environment](../../Lab1%20-%20WikiPediaChatApp/1.1SettingUptheEnv.md). Make sure an Azure AI Studio Project has been successfully launched.

You can launch a new project via the Home page too...
![Alt text](../../../media/1420.png)

Make sure there is a running VM within the project. You can check via project settings. You can launch a new VM or restart an existing VM if created before. AI Studio / VS Code integration leverages VS Code Remote Development which runs a remote dev container within the Project VM and lets your client VS Code instance remotely run code on the server over an automatically set up SSH tunnel. Prebuilt development environments are based on a docker container that has the **Azure AI SDK generative packages, the Azure AI CLI, the Prompt flow SDK**, and other tools.  All config & setup is automatically done by AI Studio. Please follow the below steps to get your local VSCode env up and running!
![Alt text](../../../media/media/1422.png)

Once launched, open the project in VSCode by clicking on the button on top right. (First click on the pop down menu and choose "Open Project in VS Code" (Desktop). Otherwise by default it will be launched in your Web browser.)
![Alt text](../../../media/1425.png)

Choose the active VM (should have a green button next to it) and press the "Set Up" button. It will take a couple of minutes for the environment to be set up.
![Alt text](../../../media/1423.png)

Finally when the setup completes click on "Launch".
![Alt text](../../media/1424.png)

Allow the VS Code App to be launched.
![Alt text](../../../media/1426.png)

Choose your Azure subscription and AI Studio will configure your project VM as a remote development server and log you in.

Finally you will have your dev environment ready!
 ![Alt text](../../../media/1427.png)

Bonus Content: \
Have a look at the tutorial at MS Learn [Tutorial: Build and deploy a question and answer copilot with the Azure AI CLI and SDK](https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/deploy-copilot-sdk)

Other ways you can use Azure AI SDK...\
Option2 Visual Studio Code Dev Container \
Option3 GitHub Workspaces 
Follow the [documentation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/sdk-install?tabs=linux) to go forward with Option2/3.