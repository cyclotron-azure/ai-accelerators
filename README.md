# AI Accelerators Repositories

This repository contains a list of AI accelerators repositories.

## llama-index-python
### Description
This sample shows how to quickly get started with LlamaIndex.ai on Azure🚀
### Language
Python
### URL
[https://github.com/Azure-Samples/llama-index-python](https://github.com/Azure-Samples/llama-index-python)
### Summary

**GitHub Repository**: [Azure-Samples/llama-index-python](https://github.com/Azure-Samples/llama-index-python)

**Description**: This repository contains a sample application to quickly get started with LlamaIndex.ai on Azure. It demonstrates building a RAG (retrieval-augmented generation) chatbot application using Azure OpenAI services.

### Key Features:
1. **Functionality**: 
   - The sample app serves as a chat interface that ingests various data formats (PDF, text, CSV, Word, HTML) and answers questions about the data using Azure OpenAI (gpt-35-turbo model).
   - It includes a sample dataset in the `./data` directory.

2. **Architecture**:
   - Backend: Built using FastAPI (Python).
   - Frontend: Built using Next.js (JavaScript).
   - Hosted on Azure Container Apps.

3. **Getting Started**:
   - Multiple setup options: GitHub Codespaces, VS Code Dev Containers, and Local Environment.
   - Instructions for setting up Python environment, installing dependencies, and deploying to Azure.

4. **Personalization**:
   - Customize app data and appearance.
   - Modify data to be ingested and adjust frontend settings like app name and avatar.

5. **Security**:
   - Utilizes Managed Identity or Key Vault for credential management.
   - Includes GitHub Actions for secret scanning.

6. **Costs**:
   - Pricing information for Azure services used (Azure Container Apps and Azure OpenAI) with links to Azure pricing calculator for estimates.

### Prerequisites:
- Python (3.9, 3.10, or 3.11)
- Poetry
- Node.js LTS
- Azure Developer CLI
- Git
- PowerShell 7+ (for Windows users)

### Resources & Troubleshooting:
- LlamaIndex Documentation
- Azure AI and OpenAI documentation
- Azure AI samples
- Issues can be reported in the repository for assistance.

### Contributing:
- Contributions are welcome and managed under the Microsoft Open Source Code of Conduct. 
- Contributor License Agreement (CLA) required for contributions.

### License:
- The project is licensed under the MIT License.

For more detailed instructions and exact command-line inputs, refer to the [README.md](https://github.com/Azure-Samples/llama-index-python/blob/main/README.md) file in the repository.
## graphrag-accelerator
### Description
One-click deploy of a Knowledge Graph powered RAG (GraphRAG) in Azure
### Language
Python
### URL
[https://github.com/Azure-Samples/graphrag-accelerator](https://github.com/Azure-Samples/graphrag-accelerator)
### Summary
The repository "Azure-Samples/graphrag-accelerator" on GitHub provides a one-click deployment solution for a Knowledge Graph-powered Retrieval-Augmented Generation (GraphRAG) in Azure. The solution builds on the Graphrag Python package and offers API endpoints hosted on Azure to facilitate indexing and querying of the knowledge graph.

### Key Features:
- **Deployment Guide:** Instructions on deploying the solution as a complete API.
- **Quickstart Notebook:** Demonstrates various API calls.
- **Development Guide:** Instructions for those interested in contributing.
- **Issue Tracking:** Uses GitHub Issues for bug reports and feature requests.
- **Contribution Guidelines:** Contributors must agree to a Contributor License Agreement (CLA).

### Additional Information:
- **License:** MIT License.
- **Code of Conduct:** The project adopts Microsoft's Open Source Code of Conduct.
- **Trademarks:** Usage of Microsoft trademarks and logos should adhere to Microsoft's guidelines.

### Repository Stats:
- **Stars:** 1.2k
- **Forks:** 172
- **Primary Languages:** Python, Bicep, Jupyter Notebook, Shell, among others.

For more information, check out the README file and relevant links provided in the repository.
## gpt-video-analysis-in-a-box
### Description

### Language
Bicep
### URL
[https://github.com/Azure-Samples/gpt-video-analysis-in-a-box](https://github.com/Azure-Samples/gpt-video-analysis-in-a-box)
### Summary
## GitHub - Azure-Samples/gpt-video-analysis-in-a-box

### Overview
This repository features a solution called "GPT Video Analysis in-a-Box" which uses Azure OpenAI GPT-4 Turbo with Vision and Azure Data Factory for image and video analysis. It is part of the AI-in-a-Box framework designed by Microsoft to simplify AI and ML solutions deployment.

### Key Features
- **Low-Code Solution:** Utilizes Azure Data Factory for orchestrating Azure OpenAI service calls.
- **Integration:** Seamless integration with Azure services like Key Vault, Blob Storage, and Cosmos DB.
- **Parameterization:** Allows customization and reusability across different scenarios.
- **Stored Results:** Analysis results are stored in Azure Cosmos DB in JSON format.
- **Sample Assets:** Includes sample images, videos, and prompts for evaluation and testing.
  
### User Story
Enables insights from images and videos for various industries without the need to develop custom models. Example use cases include insurance claims assessment, product defect identification, store traffic tracking, and wildlife monitoring.

### What's in the Box
- Sample assets (images and videos) and prompts.
- Az Data Factory setup for managing analysis workflows.
- Managed Identities for secure integrations.
- Deployable resources including Azure Key Vault, OpenAI GPT-4V, AI Vision, Blob Storage, Data Factory, and Cosmos DB.

### Deployment and Running
1. **Prerequisites:** Install Azure CLI, Bicep, Azure Developer CLI, and Azure Function Core Tools.
2. **Deploy:** Clone the repository and run deployment scripts using Azure CLI commands.
3. **Upload:** Use Azure Portal or tools like Azure Storage Explorer to upload media files.
4. **Run:** Execute the orchestration pipeline in Azure Data Factory and review results in Cosmos DB.

### Customization
- Modify system and user prompts, temperature, and other parameters to finetune analysis.
- Adapt the solution for real-time analysis by setting storage event triggers.
- Extend the data factory for other use cases by adjusting parameters and triggers.
- Optionally, compare with other models like GPT-4o for performance benchmarking.

### Contribution
Welcomes contributions and involves signing a Contributor License Agreement (CLA). Adheres to the Microsoft Open Source Code of Conduct.

### Key Contacts
- **Jean Hayes:** @jehayesms, jean.hayes@microsoft.com
- **Chris Ayers:** @codebytes, chrisayers@microsoft.com

### License
The project is under the MIT license. Authorized use of trademarks and logos must follow Microsoft's Trademark & Brand Guidelines. 

The solution aims to empower users with straightforward AI/ML tools, enhancing quality and efficiency in video and image analysis.
## openai-chat-app-entra-auth-builtin
### Description
A simple chat application that integrates Microsoft Entra ID for user authentication. Designed for deployment on Azure Container Apps with the Azure Developer CLI.
### Language
Python
### URL
[https://github.com/Azure-Samples/openai-chat-app-entra-auth-builtin](https://github.com/Azure-Samples/openai-chat-app-entra-auth-builtin)
### Summary
### Project Overview
**Repository Name:** Azure-Samples/openai-chat-app-entra-auth-builtin

**Description:** 
A simple chat application written in Python that integrates Microsoft Entra ID (formerly Azure AD) for user authentication. It is designed to be deployed on Azure Container Apps using the Azure Developer CLI.

### Key Features
- **Backend:** Python Quart framework with OpenAI API for generating responses.
- **Frontend:** Basic HTML/JavaScript interface that streams responses using JSON Lines over a ReadableStream.
- **Infrastructure:** Provisioning scripts using Bicep for deploying Azure resources, Azure Container Apps, and Azure Container Registry.
- **Authentication:** Supports Microsoft Entra ID and Microsoft Entra External ID for user login.
- **Deployment:** Uses Azure Developer CLI (`azd`) to set up environments and deploy the app.

### Setup and Deployment Steps
1. **Opening the Project:** 
   - The project supports Dev Containers for easy setup in GitHub Codespaces or local VS Code with the Dev Containers extension.
   - If not using Dev Containers, create a Python virtual environment and install required packages.

2. **Azure Account Setup:**
   - Create a free Azure account and subscribe to Azure OpenAI Service.
   - Ensure the Azure account has necessary permissions for deployment.

3. **Microsoft Entra ID Setup:**
   - Configure an environment variable with the tenant ID for authentication.
   - Authenticate with Azure CLI and proceed with deployment.

4. **Microsoft Entra External ID Setup:**
   - Use for allowing external users to sign in using social identities.
   - Similar setup steps as Entra ID, with additional endpoints and scripting for setup.

5. **Deployment:**
   - Deploy using `azd up` after configuring Entra ID or External ID.
   - For continuous deployment, use the provided GitHub Actions workflow.

### Development Server
Run the Quart app locally:
```bash
python -m quart --app src.quartapp run --port 50505 --reload
```
Access the app at `http://localhost:50505`.

### Costs
The project incurs costs based on Azure resource usage, notably for Azure Container Registry and Azure OpenAI service. Use the Azure pricing calculator to estimate costs.

### Security Guidelines
- Uses Managed Identity for authenticating to Azure OpenAI.
- Stores client secrets in Azure Key Vault.
- Includes GitHub Actions for scanning infrastructure-as-code files.

### Additional Resources
- OpenAI Chat Application with MSAL SDK
- OpenAI Chat App with Managed Identity
- RAG Chat with Azure AI Search + Python

**License:** MIT License

### Repository Stats
- **Stars:** 17
- **Forks:** 7
- **Contributors:** 3
- **Languages:** Python, Bicep, HTML, PowerShell, Dockerfile, Shell, CSS

**Topics:** Python, OpenAI, Azure Container Apps, Azure OpenAI, Microsoft Entra, Entra External ID

For more detailed information, refer to the [README](https://github.com/Azure-Samples/openai-chat-app-entra-auth-builtin).
## azure-functions-openai-extension
### Description
An extension that adds support for Azure OpenAI/ OpenAI bindings in Azure Functions for LLM (GPT-3.5-Turbo, GPT-4, etc)
### Language
C#
### URL
[https://github.com/Azure/azure-functions-openai-extension](https://github.com/Azure/azure-functions-openai-extension)
### Summary
The "Azure/azure-functions-openai-extension" repository provides an extension that integrates support for Azure OpenAI and OpenAI bindings into Azure Functions, specifically for language models such as GPT-3.5-Turbo and GPT-4. This project facilitates the use of OpenAI's capabilities within the Azure Functions environment, enabling features like text completion, chat completion, embeddings generation, semantic search, and assistant skills.

### Key Features:
- **Text Completion**: Bindings to invoke OpenAI’s text completion API.
- **Chat Completion**: Supports creating and managing AI-powered assistants with stateful conversations.
- **Embeddings Generator**: Generates embeddings for text, which can be used for various purposes like search and clustering.
- **Semantic Search**: Allows importing documents into a vector database and querying them with semantic search.

### Setup Requirements:
- .NET 6 SDK or greater, preferably Visual Studio 2022.
- Azure Functions Core Tools v4.x.
- Specific Azure settings, such as `AZURE_OPENAI_ENDPOINT` and managed identity, for securing access.

### Sample Code:
- Provides detailed examples in multiple languages such as C# and Python for using the extension features including setting up models, generating embeddings, and performing semantic searches.

### Contribution:
- The project welcomes contributions, with guidelines requiring a Contributor License Agreement (CLA).
- It adheres to the Microsoft Open Source Code of Conduct.

### Licensing:
- The project is licensed under the MIT license.

This extension is ideal for developers looking to leverage the powerful capabilities of OpenAI models within their Azure Functions applications, enabling more sophisticated and AI-driven functionalities.
## enterprise-azureai
### Description
Unleash the power of Azure AI to your application developers in a secure & manageable way with Azure API Management and Azure Developer CLI.
### Language
TypeScript
### URL
[https://github.com/Azure/enterprise-azureai](https://github.com/Azure/enterprise-azureai)
### Summary
### Summary: GitHub - Azure/enterprise-azureai Repository

This repository, **Azure/enterprise-azureai**, offers tools and guidance for developers to integrate Azure AI capabilities securely and efficiently using Azure API Management and Azure Developer CLI (azd). Key highlights include:

1. **Infrastructure-as-Code**: Use Bicep templates to provision resources.
2. **CI/CD Pipeline**: GitHub Actions and Azure DevOps Pipelines for continuous deployment.
3. **Secure Access Management**: Best practices for managing secure access to Azure OpenAI services.
4. **Cost Control and Monitoring**: Track usage and allocate costs accurately.
5. **Load Balancing**: Utilize capacity across Azure regions.
6. **End-to-End Sample**: Sample ChatApp and dashboards demonstrating the usage.

### Key Features:
- **Bicep Templates**: IaC files for resource provisioning.
- **CI/CD Workflows**: Ready-to-use GitHub and Azure Pipelines scripts.
- **Sample Applications**: .NET 8.0 chargeback proxy and NodeJS ChatApp.
- **Optional Features**: Enable Redis Cache or secondary Azure OpenAI locations.
- **Documentation**: Detailed instructions on setting up and deploying.

### Getting Started:
1. **Prerequisites**: Azure Developer CLI, Azure CLI, .NET 8.0 SDK, Docker Desktop, Node.js v18.17+, jq (for Mac/Linux).
2. **Initialize Environment**: Use `azd init` to start.
3. **Provision and Deploy**: Use `azd up` for resource deployment.
4. **Monitoring**: Included Log Analytics workspace with custom dashboards.
5. **Clean Up**: `azd down --purge --force` to delete resources.

### Additional Information:
- **Architecture**: Integrates Azure OpenAI via Azure API Management and Azure Container Apps.
- **Security and Best Practices**: Utilize Azure Integration Service Landingzone Accelerator, OAuth authentication, and Private Link Scope for security.
- **Sample ChatApp**: Demonstrates API Management and Azure OpenAI service integration.

### Technologies Used:
- TypeScript, Bicep, C#, Shell, PowerShell, JavaScript.

### License and Contributions:
- **License**: MIT.
- **Contributors**: 8.

This repo provides a comprehensive solution for managing and deploying Azure AI capabilities within a secure and cost-effective framework, suitable for enterprise-scale applications.
## agent-openai-python-prompty
### Description
A creative writing multi-agent solution to help users write articles.
### Language
Python
### URL
[https://github.com/Azure-Samples/agent-openai-python-prompty](https://github.com/Azure-Samples/agent-openai-python-prompty)
### Summary
# "Azure-Samples/agent-openai-python-prompty" Summary

**Repository Overview:**
- **Name:** agent-openai-python-prompty
- **Description:** A creative writing multi-agent solution to assist users in composing articles using Python, Azure OpenAI, Bing Search API, and Azure AI Search.
- **License:** MIT License

**Key Features:**
- **AI-Driven:** Utilizes Azure OpenAI for various AI agents.
- **Integrated APIs:** Incorporates Bing Search API for research and Azure AI Search for semantic similarity searches.
- **Prompts Management:** Uses Prompty and Prompt Flow for prompt management and evaluation.

**Components:**
- **Flask App:** Takes user input for topics and instructions.
- **Agents:** 
  - *Research Agent:* Uses Bing Search API.
  - *Product Agent:* Uses Azure AI Search.
  - *Writer Agent & Editor Agent:* Combine and refine information to generate articles.

**Setup Options:**
1. **GitHub Codespaces:** Easiest method, sets up the environment in-browser.
2. **VS Code Dev Containers:** Runs the project locally within VS Code.
3. **Local Environment:** Requires installing Azure CLI, Docker, Git, and Python 3.10+.

**Deployment and Testing:**
- Sign in to Azure and set up the project using `azd up`.
- Special focus on regions for resource deployment (recommended France Central or East US 2).
- Run local testing with Flask webserver and additional example web app.

**CI/CD Setup:**
- Configurable GitHub Actions for CI/CD to automatically deploy.
- Requires setting up role assignments on Azure storage for GitHub actions.

**Costs:**
- Pricing varies based on resource usage, consultation with Azure pricing calculator recommended for:
  - Azure Container Apps
  - Azure OpenAI
  - Azure Monitor

**Security:**
- Uses Managed Identity and Key Vault for secrets management.
- Recommended enabling GitHub secret scanning.

**Documentation and Conduct:**
- Includes detailed documentation and guidelines.
- Adopts Microsoft's Open Source Code of Conduct.

**Technologies Used:**
- **Languages:** Python, HCL, TypeScript, Jupyter Notebook, Shell, Dockerfile
- **Azure Services:** Azure OpenAI, Bing Search API, Azure AI Search

**Community and Contributions:**
- 48 stars, 31 forks, and active contributions with 9 contributors.

For more detailed instructions and further information, review the [README.md in the repository](https://github.com/Azure-Samples/agent-openai-python-prompty).
## container-apps-dynamic-sessions-samples
### Description
Samples for Azure Container Apps dynamic sessions
### Language
Python
### URL
[https://github.com/Azure-Samples/container-apps-dynamic-sessions-samples](https://github.com/Azure-Samples/container-apps-dynamic-sessions-samples)
### Summary
The GitHub repository "container-apps-dynamic-sessions-samples" under Azure-Samples provides various samples for implementing dynamic sessions in Azure Container Apps. This repository includes tutorials for different frameworks and technologies such as LangChain, LlamaIndex, Semantic Kernel, and AutoGen. The repository is mainly written in Python (77.6%) with some Dockerfile (22.4%). It has an MIT license and includes essential files like the README.md, CHANGELOG.md, and a CONTRIBUTING.md. The repo is relatively small with 6 stars, 5 forks, and no published releases or packages. The repository also follows a code of conduct for contributors.
## AI-Gateway
### Description
APIM ❤️ OpenAI - this repo contains a set of experiments on using GenAI capabilities of Azure API Management with Azure OpenAI and other services
### Language
Jupyter Notebook
### URL
[https://github.com/Azure-Samples/AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)
### Summary
The repository `AI-Gateway` by Azure-Samples on GitHub explores using Generative AI (GenAI) capabilities within Azure API Management (APIM) with Azure OpenAI and other services. It features a series of experimental labs intended for organizations to experiment and stay at the forefront of AI innovation. The experimentation focuses primarily on Azure OpenAI, but the principles can apply to other large language models.

### Key Features:
- **Exploratory Labs**: Includes labs for load balancing, access control, token metrics, response streaming, vector searching, built-in logging, GPT-4o inferencing, and more.
- **Tools**: Provides tools for mocking OpenAI API, tracing, and streaming.
- **Well-Architected Framework**: Aligns labs with Azure's Well-Architected Framework to enhance security, reliability, performance, operations, and cost-efficiency.
- **Resources**: Offers a range of additional resources, step-by-step guides, and references for comprehensive AI solutions.
- **Prerequisites**: Requires Python 3.8+, VS Code with Jupyter extension, Azure CLI, and an Azure Subscription with Contributor permissions.

### Getting Started:
1. **Clone the Repo**: Set up the local environment with the prerequisites.
2. **Navigate Labs**: Choose and execute labs suitable for your needs.
3. **Customization and Contribution**: Tailor experiments as needed and contribute back through pull requests.

### Labs Overview:
- Labs are centered around practical applications like backend load balancing, access control, token metrics, and more, each featuring detailed Jupyter notebooks for structured experimentation.

### License:
- The repository is under the MIT license, encouraging open and collaborative development.

### Additional Information:
- The repo emphasizes the experimental approach required for leveraging AI services effectively with robust API management strategies, primarily using Azure OpenAI's capabilities.

Visit the repository for more details and to access the labs: [AI-Gateway](https://aka.ms/apim/genai/labs).
## ai-hub-gateway-solution-accelerator
### Description
Reference architecture that provides a set of guidelines and best practices for implementing a central AI API gateway to empower various line-of-business units in an organization to leverage Azure AI services
### Language
Bicep
### URL
[https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator](https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator)
### Summary
The Azure-Samples/ai-hub-gateway-solution-accelerator repository provides a reference architecture with guidelines and best practices to set up a central AI API gateway. This gateway allows various business units within an organization to leverage Azure AI services efficiently. Key features of this solution include:

- **Centralized AI API Gateway:** A shared entry point for AI services with secure and governed access.
- **Seamless Azure Integration:** Easy endpoint and key updates for existing applications.
- **AI Service Routing and Orchestration:** Prioritized and consistent management of AI services.
- **Granular Access Control:** Uses managed identities instead of master keys.
- **Private Connectivity:** Deployment in a private network with private endpoints.
- **Capacity Management, Usage, and Charge-back:** Monitors and manages requests and tokens; tracks usage for business unit charge-backs.
- **Resilience and Scalability:** Leverages Azure API Management for regional redundancy and scalability.
- **Full Observability:** Integrates Azure Monitor, Application Insights, and Log Analytics for performance and error insights.
- **Hybrid Support:** Supports deployment in Azure, on-premises, or other clouds.

Recent updates include support for private virtual networks, enhanced monitoring and reporting features, and new models such as GPT-4. The solution also offers a "one-click deploy" option through Azure Developer CLI or Bicep to set up the infrastructure, which includes Azure API Management, Application Insights, Event Hub, Azure OpenAI, Cosmos DB, Azure Function App, Virtual Network, and more.

Prerequisites for deploying this solution include an Azure account, appropriate Azure subscription permissions, Azure CLI, Azure Developer CLI, and Visual Studio Code. Deployment involves configuring environment parameters and running deployment commands through Azure CLI. Supporting documents provided cover detailed technical guides and deployment troubleshooting. The repository operates under the MIT license.
## rag-postgres-openai-python
### Description
A RAG app to ask questions about rows in a database table. Deployable on Azure Container Apps with PostgreSQL Flexible Server.
### Language
Python
### URL
[https://github.com/Azure-Samples/rag-postgres-openai-python](https://github.com/Azure-Samples/rag-postgres-openai-python)
### Summary
### Project Summary for Azure-Samples/rag-postgres-openai-python

**Description:**
This repository hosts a Retrieval-Augmented Generation (RAG) application designed for querying rows in a PostgreSQL database table using OpenAI chat models. The application can be deployed on Azure Container Apps with a PostgreSQL Flexible Server backend.

**Frontend and Backend:**
- **Frontend:** Built with React and FluentUI.
- **Backend:** Developed using Python and FastAPI.

**Deployment:**
The project supports deployment via Azure Developer CLI, hosting the app on Azure Container Apps, using Azure PostgreSQL Flexible Server for the database, and Azure OpenAI for the model integration.

**Features:**
1. **Hybrid Search:** Combines vector search using the pgvector extension and full-text search.
2. **OpenAI Functionality:** Transforms user queries into query filter conditions.
3. **Query Vector Conversion:** Uses the OpenAI embedding API to convert queries into vectors.

**Setup Options:**
- **GitHub Codespaces:** Enables virtual setup for development.
- **VS Code Dev Containers:** Allows local setup with Docker.
- **Local Environment:** Requires installation of tools like Azure Developer CLI, Node.js 18+, Python 3.10+, PostgreSQL 14+, Docker Desktop, and Git.

**Deployment Steps:**
1. Sign in to your Azure account and set up environment configurations.
2. Provision resources and deploy the code using `azd up`.

**Local Development:**
1. Adjust the environment file for OpenAI or Ollama models.
2. Install necessary packages and set up the local database.
3. Run both the frontend and backend with hot reloading.

**Costs:**
Deployment costs vary based on resource usage such as CPU, memory, tokens used, and data ingested. Example resources include Azure Container Apps, Azure OpenAI, Azure PostgreSQL Flexible Server, and Azure Monitor.

**Security:**
The template uses Managed Identity for Azure services authentication and includes a GitHub Action for scanning infrastructure-as-code files for security issues.

**Resources and Documentation:**
Additional documentation on existing resource deployment, monitoring, and load testing is available in the `docs/` folder. Issues and questions can be addressed in the repository's issue tracker.

**License:**
This project is licensed under the MIT License.

**Languages Used:**
- Python (52.6%)
- Bicep (21.7%)
- TypeScript (18.7%)
- CSS (4.0%)
- Shell (1.5%)
- PowerShell (1.0%)

**Contributors:**
- Pamela Fox
- John Aziz
- dependabot[bot]
- Daniel Martin

For more details and to access the repository, visit: [Azure-Samples/rag-postgres-openai-python](https://github.com/Azure-Samples/rag-postgres-openai-python).

---

**Summary:**
The `rag-postgres-openai-python` project uses Azure services to create a chat application capable of querying a PostgreSQL database. With deployment and local development guided via Azure Developer CLI, the application integrates OpenAI models for enhanced query functionality. It includes hybrid search capabilities, converts queries into vectors using OpenAI's embedding API, and employs Azure for seamless cloud hosting and resource management.
## contoso-chat-csharp-prompty
### Description

### Language
Bicep
### URL
[https://github.com/Azure-Samples/contoso-chat-csharp-prompty](https://github.com/Azure-Samples/contoso-chat-csharp-prompty)
### Summary
### Contoso Chat C# Sample README Summary:

This project, hosted on GitHub under the Azure-Samples organization, presents the **Contoso Chat Retail** application, an intelligent customer engagement and sales support chatbot for a conceptual outdoor gear store. The chatbot integrates Azure AI and Cosmos DB technologies for enhanced customer interactions.

#### Key Technologies Used:
1. **Azure AI Search**: Manages search indexes for product catalog data.
2. **Azure Cosmos DB**: Stores customer purchase histories.
3. **Azure OpenAI**: Deploys and manages AI models.
4. **Semantic Kernel**: Accesses AI models and integrates prompts.
5. **Prompty**: Simplifies the creation and iteration of prompts.
6. **ASP.NET Core WebAPI**: Exposes REST endpoints.

#### Features:
- Builds, evaluates, and deploys a retail copilot application.
- Demonstrates the use of AI to integrate personalized customer service experiences.
- Utilizes models like `text-embeddings-ada-002` and `gpt-35-turbo`.
- Showcases Azure Managed Identity for handling sensitive credentials.

#### Setup and Deployment:
- **Prerequisites**: Azure and GitHub accounts, access to specific Azure OpenAI models, and various development tools.
- **Development Environment**: 
  - Options to use GitHub Codespaces, Docker Desktop, or manual setup.
- **Provisioning Resources**: Use the Azure Developer CLI (`azd`) to provision necessary resources like Cosmos DB, Azure OpenAI, Azure AI Search, and Azure Container Apps.
- **Running the Application**: Instructions provided to start the application in Visual Studio Code, test APIs using Swagger UI, and interact with the deployed chat endpoint.

#### Costs:
- Detailed estimation of costs using Azure's pricing calculator across various services like Azure OpenAI, Azure AI Search, Cosmos DB, Monitor, and Container Apps.

#### Security Guidelines:
- Encourages the use of Managed Identity and GitHub Action tools for security scans.
- Recommends enabling GitHub secret scanning settings for security best practices.

#### Resources and Troubleshooting:
- Links to additional .NET AI samples, Azure learning resources, and a troubleshooting guide.
- Encourages contributions while ensuring adherences to a Contributor License Agreement (CLA) and the Microsoft Open Source Code of Conduct.

#### Contact and Contributions:
- Welcomes contributions with details on the CLA and open source code of conduct.
- Mentions possibly using trademarks according to Microsoft's guidelines. 

Overall, this README provides a comprehensive overview and step-by-step guide for developers to build, deploy, and maintain an AI-powered customer engagement chatbot using Azure technologies.
## summarization-openai-csharp-prompty
### Description
This solution converts speech to text and then processes and summarizes the text based on the prompt scenario.
### Language
Bicep
### URL
[https://github.com/Azure-Samples/summarization-openai-csharp-prompty](https://github.com/Azure-Samples/summarization-openai-csharp-prompty)
### Summary
### Summary of Azure-Samples/summarization-openai-csharp-prompty Repository

**Overview:**
This GitHub repository provides a solution that converts speech to text and then processes and summarizes this text based on predefined prompt scenarios. It is designed for use cases like workers at Contoso Manufacturing reporting issues via text or speech. The solution leverages Azure AI Speech Service, Azure OpenAI, and Semantic Kernel with Prompty files to manage, insert, and evaluate the effectiveness of prompts.

**Key Features:**
- **Speech to Text Translation:** Utilizes Azure AI Speech Service.
- **Text Summarization:** Uses Azure OpenAI to condense and focus text.
- **Prompty Files:** Defines and manages LLM prompts.
- **Sample Configuration:** Includes azd configurations for deploying necessary resources on Azure.
- **Managed Identity:** Follows best practices for credential management.

**Getting Started:**
- **GitHub Codespaces:** Quick setup with a web-based VS Code instance.
- **VS Code Dev Containers:** Local development using Docker and the Dev Containers extension.
- **Local Environment:** Requires .NET SDK, Git, Azure Developer CLI, and a suitable editor like VS Code or Visual Studio.

**Deployment:**
Deploy code and resources to Azure using the Azure Developer CLI commands `azd auth login` and `azd up`.

**Exploring the Sample:**
Three projects are available:
1. **SummarizationAPI.Console:** Test console for speech-to-text translation.
2. **Summarization.Evaluation.Test:** Unit tests for evaluating prompts.
3. **SummarizationAPI:** ASP.NET Core project providing an HTTP endpoint for text summarization.

**Cleaning Up:**
Use `azd down` command to remove all resources created by the sample.

**Guidance:**
- **Region Availability:** Ensures deployment in supported Azure regions.
- **Cost Estimation:** Outlined costs for the architecture using the Azure pricing calculator.
- **Security:** Emphasizes Managed Identity and security scans during deployment.

**Contribution:**
Contributions are welcomed, requiring a Contributor License Agreement (CLA).

**Licenses:**
MIT license

By following the guidelines provided, you can set up and explore this solution, tailor it to specific needs, and contribute to the repository if desired.
## aihub
### Description
AI Hub Executive Demo HandsOn
### Language
HTML
### URL
[https://github.com/Azure/aihub](https://github.com/Azure/aihub)
### Summary
# AI Hub Executive Demo HandsOn - Azure/aihub

## Overview

AI Hub is a project designed to showcase how various Azure cloud services can be integrated to create intelligent and scalable solutions. The project consists of multiple use cases demonstrating the capabilities of AI and cloud computing through hands-on demos and documentation.

### Key Features & Use Cases

1. **Chat on Your Own Data**:
   - Uses Azure OpenAI, Cognitive Search, Container Apps, Application Insights, and Azure API Management.
   - Provides a chat interface for document search and retrieval with features like suggested questions and citations.
   - Allows uploading custom data files for vector searches using semantic or hybrid methods.
   - Supports extensibility, security features, monitoring, and scalability.

2. **Call Center Analytics**:
   - Analyses call transcripts either provided or transcribed using Azure Speech Services.
   - Customizable template and query for detailed analysis.

3. **Image Analyzer**:
   - Uses GPT-4 and Azure Vision Services.
   - Supports image formats like .jpg and .png for analysis.

4. **Brand Analyzer**:
   - Analyzes internet reputation through Bing searches.
   - Sentiment analysis for company mentions or specific products/services.
  
5. **Form Analyzer**:
   - Uses GPT-4 and Azure Document Intelligence to analyze uploaded .pdf documents.
   - Chat with documents and extract custom information.

6. **Document Comparison**:
   - Compares different versions of documents using GPT-4 and Azure Document Intelligence.
   - Extracts and highlights content differences.

7. **Content Safety**:
   - Moderates user-generated content for safety risks using Azure AI Content Safety.
   - Includes image and text moderation for online platforms like social media.

### Contributing

The project is open to contributions and requires contributors to sign a Contributor License Agreement (CLA). The process is handled by a CLA bot that provides instructions and ensures compliance.

### Code of Conduct

The project adheres to Microsoft's Open Source Code of Conduct, promoting a respectful and collaborative environment.

### Additional Information

- **License**: MIT License
- **Languages Used**: HTML, HCL, C#, JavaScript, Python, CSS

### Resources

- [Project Documentation](azure.github.io/aihub)
- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct)

This repository offers extensive functionality and showcases AI integrations using Azure services, providing a comprehensive hands-on experience for users to explore and build upon.
## agent-python-openai-prompty-langchain
### Description
Function calling for vector database lookup based on user question
### Language
Bicep
### URL
[https://github.com/Azure-Samples/agent-python-openai-prompty-langchain](https://github.com/Azure-Samples/agent-python-openai-prompty-langchain)
### Summary
## Summary of the GitHub Repository: Azure-Samples/agent-python-openai-prompty-langchain

### Overview
This repository provides a sample project utilizing the Prompty tool, Langchain, and Elasticsearch to build a large language model (LLM) search agent. The agent uses Retrieval-Augmented Generation (RAG) technology to answer user questions by integrating real-time information retrieval with generative responses.

### Key Features
- **Chat Agent (`agent.py`)**: Receives user questions, generates queries, performs searches within an Elasticsearch data index, and refines search outputs for presentation.
- **Data Management**: A local data folder is used, and a new index is created during initialization for efficient searching.
- **Evaluations**: Built-in evaluations for testing Prompt Flow with telemetry pushed to Azure AI Studio.
- **Deployment**: The project can be deployed and evaluated using Azure AI Studio.

### Getting Started
To set up and run the project, you will need:
- An Azure account (with necessary permissions and possibly an Azure OpenAI service subscription).
- An Elasticsearch account with appropriate configuration.
- The project can be set up using GitHub Codespaces for a web-based development environment or locally with Docker and Python.

### Setup Steps
1. **Azure and Elasticsearch Accounts**: Create and configure accounts.
2. **Environment Variables**: Set environment variables for Elasticsearch and Azure OpenAI endpoints and keys.
3. **Deployment**: Use `azd` commands to initialize, authenticate, deploy, and manage Azure resources.
4. **Local Development**: Install dependencies using Poetry, configure environment variables, and run the app locally to test features.

### Important Commands
- **Initialize Project**: `azd init agent-python-openai-prompty-langchain`
- **Login to Azure**: `azd auth login`
- **Deploy to Azure**: `azd up`
- **Local Setup**:
  - Install dependencies: `poetry install --no-interaction --no-ansi`
  - Run locally: `langchain serve`

### Clean Up
To remove all deployed resources, use `azd down` and confirm actions.

### Additional Information
- **Costs**: Estimate using Azure's pricing calculator.
- **Security**: Recommended to use Azure Key Vault for securing API keys.
- **Documentation and Resources**: Links to further documentation are provided within the repository.

### About the Repository
The sample is designed for function calling for vector database lookups based on user questions. The repository includes a variety of files, including setup and configuration files, source code, and documentation.

### License
The project is licensed under the MIT License.

For more detailed instructions and steps, refer to the `README.md` in the repository.
## private-openai-with-apim-for-chargeback
### Description
Open AI with Private Endpoints behind APIM and functionality to get tokens consumption for each consumer
### Language
Bicep
### URL
[https://github.com/Azure-Samples/private-openai-with-apim-for-chargeback](https://github.com/Azure-Samples/private-openai-with-apim-for-chargeback)
### Summary
### GitHub Repository: private-openai-with-apim-for-chargeback

#### Overview
This repository focuses on integrating Azure OpenAI with private endpoints behind Azure API Management (APIM) and implementing functionality to monitor token consumption for each consumer.

#### Key Features
1. **Security and Privacy**:
   - Ensures private data transmission through Azure OpenAI Private Endpoints.
   - Provides centralized and secure access to govern API usage and chargeback mechanisms.

2. **Infrastructure as Code**:
   - Uses Bicep templates for provisioning Azure resources like OpenAI, APIM, Azure Event Hub, Azure Function App, and Azure Private Links.

3. **Token Usage Calculation**:
   - Includes a function app to compute token usage for streaming and non-streaming requests using the Tokenizer package.

4. **Test Scripts**:
   - Contains scripts to test OpenAI completion and chat endpoints via PowerShell or shell scripts.

5. **Comprehensive Observability**:
   - Leverages Azure Monitor and Application Insights for extensive logging, querying, and monitoring capabilities.

#### Deployment and Setup
- **Account Requirements**:
  - An Azure account with enabled access for the Azure OpenAI service.
  - Sufficient Azure account permissions for role assignments and deployments.

- **Deploy to Azure**:
  - Uses Azure Developer CLI for deployment.
  - Options to deploy both fresh setups and existing resource groups.

- **Testing**:
  - Instructions on running test scripts for both completion and chat endpoints.
  - Details on using Azure Monitor queries to analyze token usage metrics.

#### Benefits
- **Private and Secure**: Ensures protected data transmission and secure API access.
- **Token Management**: Automates the computation and logging of token usage.
- **Policy as Code**: Implements access control and logging policies within APIM.
- **End-to-End Observability**: Facilitates comprehensive monitoring and alerting through Azure services.
- **Flexible Data Analysis**: Supports logging and querying of token usage data for various analytical needs.

#### Contribution
- Welcomes contributions under Microsoft's Contributor License Agreement.
- Adopts the Microsoft Open Source Code of Conduct.

#### Additional Details
- **Architecture**: Detailed structure of client application interaction with Azure OpenAI via APIM and private links.
- **Azure OpenAI Swagger Specification**: Included for API documentation and testing.
- **Tiktoken Library**: Used for token calculations during streaming requests.

**License**: MIT License.

For complete setup, detailed instructions, and further information, refer to the repository's README.md file.
## serverless-chat-langchainjs
### Description
Build your own serverless AI Chat with Retrieval-Augmented-Generation using LangChain.js, TypeScript and Azure
### Language
TypeScript
### URL
[https://github.com/Azure-Samples/serverless-chat-langchainjs](https://github.com/Azure-Samples/serverless-chat-langchainjs)
### Summary
This GitHub repository, "serverless-chat-langchainjs," provides a comprehensive sample to build a serverless AI chat application using LangChain.js, TypeScript, and Azure technologies. The solution leverages Azure Static Web Apps, Azure Functions, and Azure AI Search for hosting a chatbot that uses enterprise documents to generate responses to user queries through Retrieval-Augmented Generation (RAG).

### Key Features:
- **Serverless Architecture**: Utilizes Azure Functions and Azure Static Web Apps.
- **RAG**: Combines Azure AI Search with LangChain.js for accurate responses.
- **Scalability and Cost-Effectiveness**: Achieved through Azure's serverless offerings.
- **Local Development**: Supports local development via Ollama for testing without cloud costs.

### Components:
1. **Web App**: Built with Lit and hosted on Azure Static Web Apps.
2. **Serverless API**: Built with Azure Functions for document ingestion and chat responses.
3. **Database**: Uses Azure AI Search for storing extracted text and generated vectors.
4. **File Storage**: Utilizes Azure Blob Storage for source documents.

### How to Get Started:
- **GitHub Codespaces**: Provides a preconfigured environment.
- **Local Environment**: Requires Node.js, Azure Developer CLI, Git, PowerShell, and Azure Functions Core Tools.
- **Run the Sample**: Execute locally or deploy to Azure. The repository includes comprehensive steps for both options.

### Deployment:
- Prerequisites include an Azure account, Azure OpenAI service access, and necessary permissions.
- Instructions provided to deploy the application using `azd` commands.
- Cost estimation details for running the sample on Azure are available.

### Clean-Up:
- Removes Azure resources using `azd down --purge`.

### Resources:
- Documentation on LangChain.js, Azure OpenAI Service, and Azure AI Search.
- FAQ and troubleshooting guides available for common issues.

### Contributing:
- Contributions are welcome with a Contributor License Agreement (CLA) required.
- Project adheres to the Microsoft Open Source Code of Conduct.

**Topics covered include**: JavaScript, TypeScript, MongoDB, Serverless, Azure, Chatbot, Azure Functions, RAG, Generative AI, LangChain.js, and Retrieval-Augmented Generation.

The repository aims to serve as a starting point for building more complex AI applications.
## GPT-RAG
### Description
Sharing the learning along the way we been gathering to enable Azure OpenAI at enterprise scale in a secure manner. GPT-RAG core is a Retrieval-Augmented Generation pattern running in Azure, using Azure Cognitive Search for retrieval and Azure OpenAI large language models to power ChatGPT-style and Q&A experiences.
### Language
Bicep
### URL
[https://github.com/Azure/GPT-RAG](https://github.com/Azure/GPT-RAG)
### Summary
### Summary of Azure/GPT-RAG GitHub Repository

The Azure/GPT-RAG repository is dedicated to sharing knowledge and resources to enable the use of Azure OpenAI at an enterprise scale securely. The primary focus is on a Retrieval-Augmented Generation (RAG) pattern using Azure Cognitive Search for data retrieval and Azure OpenAI large language models to support functionalities like ChatGPT and Q&A experiences.

#### Key Components:
1. **Data Ingestion**: Optimizes data chunking and indexing for retrieval.
2. **Orchestrator**: Manages LLMs and knowledge bases to generate responses.
3. **App Front-End**: Provides a scalable web interface using the Backend for Front-End pattern.

#### Deployment Options:
- **Basic Architecture**: Suitable for quick demos or PoC projects without stringent security needs. Deploy using Azure Developer CLI with simple steps like repository download and infrastructure setup.
- **Zero Trust Architecture**: Offers a secure, isolated deployment ideal for production environments. It includes steps for enabling network isolation and deploying Azure resources with additional security measures.

#### Customization:
Users can tailor their deployment and integrate additional data sources like Bing Custom Search, SQL Server, and Teradata. The repository offers troubleshooting, performance testing, and governance resources to ensure smooth deployment and operation.

#### Contribution:
The project welcomes contributions, requiring a Contributor License Agreement (CLA) in alignment with Microsoft Open Source Code of Conduct.

#### Resources:
- [Azure Cognitive Services OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service)
- [Code of Conduct](https://cla.opensource.microsoft.com)
- [Security Policy](Link in repository)

The repository is an open-source project under the MIT license, aiming to provide a robust and secure RAG model deployment framework for enterprises using Azure. Additional support and documentation are available for users transitioning from exploratory phases to full-scale production deployments.
## azure-sql-db-session-recommender-v2
### Description
Build a Retrieval Augmented Generation solution using OpenAI, Azure Functions, Azure Static Web Apps, Azure SQL DB, Data API builder and Text Embeddings
### Language
Bicep
### URL
[https://github.com/Azure-Samples/azure-sql-db-session-recommender-v2](https://github.com/Azure-Samples/azure-sql-db-session-recommender-v2)
### Summary
### Overview
The repository `azure-sql-db-session-recommender-v2` by Azure-Samples provides a sample solution to build a Retrieval Augmented Generation (RAG) recommender system using various Azure services and OpenAI. The main components of the solution include Azure Functions, Azure Static Web Apps, Azure SQL Database, Data API builder, and Text Embeddings.

### Key Components
- **Azure Static Web Apps**
- **Azure OpenAI**
- **Azure Functions**
- **Azure Functions SQL Trigger Binding**
- **Azure SQL Database**
- **Data API builder**

### Functionality
This repository demonstrates how to create a session recommender by storing and searching vector embeddings generated using OpenAI. The recommender system can generate responses to user queries using Retrieval Augmented Generation.

### Deployment
To deploy the sample, use the Azure Developer CLI (azd) which automates the provisioning and deployment of the resources necessary for the application. Essential prerequisites include:
- AZD CLI
- .NET SDK
- Node.js
- SWA CLI

Steps to deploy:
1. Install the required tools.
2. Authenticate with Azure using `azd auth login`.
3. Initialize the template with `azd init -t Azure-Samples/azure-sql-db-session-recommender-v2`.
4. Deploy the sample using `azd up`.

### Database Setup
Since the database uses private preview features, it should be deployed manually. By running the provided SQL statements, the database schema and necessary objects will be created. The SQL statements trigger Azure Functions to generate and store text embeddings for session recommender features.

### Running Locally
The solution can also be executed locally using the Static Web App CLI and Azure Function CLI after setting up `local.settings.json` and `.env` files. Install the required node packages and run `swa start` from the root folder to test the solution locally.

### User Interface
The UI is implemented using Fluent UI, providing consistent design language for the recommender app. 

### Credits
Special thanks to Aaron Powell for contributions to the RAG sample, UI revamp using Fluent UI, and implementation of the `ask` endpoint.

### Summary
This repository is a comprehensive guide to build, deploy, and test a retrieval-augmented session recommender system utilizing the synergy of OpenAI's vector embeddings and multiple Azure services. It involves initial setup, deployment steps, local testing, and utilization of advanced techniques in Azure SQL databases for vector similarity search.
## AzureOpenAILogProbs
### Description
Examples of how-to use Azure OpenAI Log Probabilities (LogProbs) feature to enhance Generative AI - Q&A grounding.
### Language
C#
### URL
[https://github.com/bartczernicki/AzureOpenAILogProbs](https://github.com/bartczernicki/AzureOpenAILogProbs)
### Summary
## AzureOpenAILogProbs Repository Summary

### Overview
The **AzureOpenAILogProbs** repository provides examples demonstrating how to utilize the Azure OpenAI Log Probabilities (LogProbs) feature to enhance the implementation of Generative AI, specifically for Question and Answer (Q&A) grounding.

### Key Features and Examples
1. **First Token Probability**:
   - Calculates the probability of the initial token being correct for answering a question.
   - Determines if the model has sufficient information to respond accurately.

2. **First Token Probability with Brier Scores**:
   - Includes Brier Scores to measure the prediction accuracy of probabilistic answers. 
   - Lower Brier Scores indicate better model accuracy.

3. **Weighted Probability of Confidence Score**:
   - Provides a self-confidence score weighted from the top 5 token probabilities.
   - Gives a calibrated confidence score for answering questions.

4. **95% Confidence Score Interval**:
   - Uses the distribution of multiple model calls to calculate a 95% confidence interval.
   - Helps understand the range of plausible answers rather than a single estimate.

### Getting Started
To use this repository:
1. Clone the repository.
2. Manage the necessary User Secrets in Visual Studio.
3. Enable the LogProbs feature:
   ```csharp
   chatCompletionOptionsConfidenceScore.EnableLogProbabilities = true;
   ```

### Background on Log Probs
Log Probabilities (LogProbs) are statistical distributions of possible tokens predicted by Large Language Models (LLMs) like GPT-4. They are instrumental in assessing the model's confidence in generating the next token accurately, which is especially useful for simulations, grounding, and improving overall AI response quality.

### Recommended Reading
- **OpenAI Cookbook - LogProbs**: https://cookbook.openai.com/examples/using_logprobs
- **What are LogProbs?**: https://www.ignorance.ai/p/what-are-logprobs

### Overall Capabilities
LogProbs empower AI systems to:
- Self-correct responses.
- Guide users to arrive at better answers.
- Improve probabilistic forecasting and confidence in generated answers.

### Advanced Considerations
Further simulated examples and discussions on calibration techniques are also included to ensure models deliver accurate and confident responses, which is crucial for high-stakes decision-making scenarios.

### Repository Details
- **Stars**: 7
- **Forks**: 2
- **Primary Language**: C#

This repository aims to provide a solid foundation for leveraging Azure OpenAI LogProbs for developing more reliable and confident AI-powered systems.
## azureai-assistant-tool
### Description
The Azure AI Assistant Tool is experimental Python application and middleware designed to simplify the development, experimentation, testing, and debugging of OpenAI assistants.
### Language
Python
### URL
[https://github.com/Azure-Samples/azureai-assistant-tool](https://github.com/Azure-Samples/azureai-assistant-tool)
### Summary
### Azure AI Assistant Tool - GitHub Repository Summary

The **Azure AI Assistant Tool** is an experimental Python application and middleware designed to simplify the development, experimentation, testing, and debugging of OpenAI assistants. 

#### Key Features:
- **Inbuilt thread and memory management**
- **Advanced Data Analysis**: Create data visualizations and solve complex code and math problems.
- **Function Calling**: Build or call external tools and APIs.
- **Retrieval Augmented Generation** (coming soon).
- **Speech transcription and synthesis** using Azure CognitiveServices Speech SDK.
- **Exportable assistant configurations** into simple CLI applications.

#### Assistants from Azure OpenAI Service:
- **Stateful evolution of Chat Completions API** for creating sophisticated copilot-like applications.
- Capabilities for **data sifting, solution suggestions, and task automation**.

#### Development Highlights:
- **Easy Configuration**: Set up your assistant with models, custom instructions, tools, etc.
- **Tool Integration**: Incorporate various functionalities to enhance assistant capabilities.
- **Dynamic User Functions**: Create and apply user-defined functions.
- **Task Management**: Efficient task management, including batch and multi-step operations.

#### Quick Start Guide:
1. **Azure Prerequisites**: Create an Azure Subscription and apply for access to Azure OpenAI Service.
2. **Install Python**: Ensure Python >= 3.8 and create a virtual environment.
3. **Install dependencies** via `pip`.
4. **Build & install azure.ai.assistant library** (optional) or use pre-built wheels.
5. **Configure Environment Variables**: Set up API keys and endpoints.
6. **Launch the application** via command line (`python main.py`).

#### Contribution and Feedback:
- The project welcomes contributions and feedback to refine and expand its capabilities.
- Licensed under the **MIT License**.
- Utilizes **PySide6** under GNU LGPL.

#### Getting Help and Documentation:
- **Issues**: For bugs or documentation errors, submit reports or pull requests.
- **Feature Requests**: File or implement desired features following contributing guidelines.

For more detailed instructions, video guides, and documentation, refer to the repository's README and resource links.
## Build-Modern-AI-Apps
### Description
Microsoft Official Build Modern AI Apps reference solutions and content. Demonstrate how to build Copilot applications that incorporate Hero Azure Services including Azure OpenAI Service, Azure Container Apps (or AKS) and Azure Cosmos DB for NoSQL with Vector Search.
### Language

### URL
[https://github.com/Azure/Build-Modern-AI-Apps](https://github.com/Azure/Build-Modern-AI-Apps)
### Summary
The "Azure/Build-Modern-AI-Apps" GitHub repository by Microsoft provides official reference solutions and content focused on building modern AI applications. This repository demonstrates how to create Copilot applications using key Azure services such as Azure OpenAI Service, Azure Container Apps (or Azure Kubernetes Service - AKS), and Azure Cosmos DB for NoSQL with Vector Search.

### Key Offerings:
- **Solution Accelerators and Hackathons:** Designed to demonstrate the creation of AI-enhanced applications and services in Azure. These include:
  - **Build Your Own Copilot:** An in-depth solution featuring a retail "Intelligent Agent" which allows users to ask questions on vectorized data in Azure Cosmos DB.
  - **Real-Time Payment and Transaction Processing:** A solution for handling accounts and transactions with AI-powered analysis tools.
  - **Medical Claims Processing:** Managing medical claims with business rules and AI-driven recommendations.

- **Workshops:**
  - **Intelligent App Workshop for Microsoft Copilot Stack:** Inspired by GitHub Copilot, this workshop focuses on integrating intelligence and productivity-boosting features into traditional software systems.

### Contributing:
- Contributions and suggestions are welcome, subject to a Contributor License Agreement (CLA).
- The repository follows Microsoft's Open Source Code of Conduct.

### Additional Information:
- The repository includes typical files like README.md, LICENSE (MIT), and SECURITY.md.
- The code and content are meant to lower the barrier to entry for organizations starting with AI projects in Azure and to expedite the development of prototypes.

This repository is a valuable resource for developers looking to accelerate the creation of AI applications utilizing Microsoft's Azure services.
## openai-apim-lb
### Description
Smart load balancing for OpenAI endpoints and Azure API Management
### Language
Bicep
### URL
[https://github.com/Azure-Samples/openai-apim-lb](https://github.com/Azure-Samples/openai-apim-lb)
### Summary
### GitHub Repository: Azure-Samples/openai-apim-lb

**Description:** This repository offers a smart load balancing solution specifically designed for managing Azure OpenAI endpoints through Azure API Management. The goal is to efficiently handle API rate limits and ensure seamless service usage across multiple backends, optimizing for availability and priority.

### Key Features:

- **Prioritized Traffic Routing:** Uses 'priority groups' to strategically allocate quotas, directing traffic to higher-priority instances first.
- **Immediate Backend Switching:** Quickly shifts traffic to available endpoints without delay when throttling occurs.
- **Scenarios and Priority Groups:**
  - **Provisioned Throughput Deployment (Priority 1):** Primary resource due to its fixed pricing.
  - **Fallback S0 Tier Deployments (Priority 2+):** Secondary resources used when PTU is at capacity.

### Installation Guides:

1. **Manual Setup:** Step-by-step instructions for setting up Azure API Management and configuring policies.
2. **Azure Developer CLI (azd) Setup:** Simplified deployment using Azure Developer CLI.

### Policy Overview:

- **Intelligent Load Balancing:** Reacts to 429 HTTP status codes by dynamically routing traffic based on backend availability and priority.
- **No Waiting Intervals:** Ensures real-time switching without delays, unlike many other API management policies.

### Additional Resources:

- **FAQ:** Common questions and answers about setup and usage.
- **Related Articles:** Detailed guides, such as the step-by-step article on smart load balancing by csiebler.

### Conclusion and Productionizing:

- The solution offers a robust approach to managing API constraints with Azure OpenAI, ensuring efficient application performance.
- To move to production, focus on security, performance optimization, and continuous monitoring.

### Repository Statistics:

- **Stars:** 52
- **Forks:** 19
- **Contributors:** 10
- **Primary Languages:** Bicep (94.8%), Python (3.8%), Shell (1.4%)

### License:

- **MIT License**

For more detailed implementation and to get started, visit the README file on the repository's GitHub page.
## openai-aca-lb
### Description
Smart load balancing for Azure OpenAI endpoints
### Language
Bicep
### URL
[https://github.com/Azure-Samples/openai-aca-lb](https://github.com/Azure-Samples/openai-aca-lb)
### Summary
The GitHub repository "Azure-Samples/openai-aca-lb" provides a solution for smart load balancing of Azure OpenAI endpoints. This project aims to handle service limitations imposed by providers like OpenAI by utilizing a sophisticated load-balancing approach. Here's a quick summary:

### Key Features:
- **Smart Load Balancing**: Manages multiple OpenAI endpoints based on availability and priority, intelligently redirecting traffic to prevent service throttling (HTTP 429 errors).
- **Use of YARP Framework**: Built using Microsoft's high-performance YARP C# reverse-proxy framework.
- **Priority-Based Routing**: Allows configuration of multiple endpoints with priority groups to optimize quota usage.
- **Immediate Retrying**: Unlike traditional round-robin methods, this solution tries different endpoints immediately in case of throttling, avoiding unnecessary wait times.
- **Deployment Options**: Supports multiple deployment methods including Azure Developer CLI, direct Azure Container Apps deployment, and Docker images (both custom-built and pre-built).
- **Custom Configuration**: Allows setting environment variables to configure OpenAI endpoints and global load balancer settings.

### Getting Started:
#### Deployment Options:
1. **Azure Developer CLI**: Quickly deploy using `azd up`.
2. **Direct Azure Container Apps**: Deploy using Azure's portal with a click.
3. **Custom Docker Image**: Build and deploy using the provided Dockerfile.
4. **Pre-built Docker Image**: Use the image from Docker hub (`andredewes/aoai-smart-loadbalancing:v1`).

#### Configuration:
- Set environment variable names for your OpenAI URLs, priorities, API keys, and optional deployment names.
- Example:
  ```sh
  BACKEND_1_URL=https://andre-openai.openai.azure.com
  BACKEND_1_PRIORITY=1
  BACKEND_1_APIKEY=your-api-key
  ```

### Testing:
- Use any client, such as OpenAI's Python SDK, to make requests to the load balancer's URL, ensuring proper setup and functionality.

### Advanced Features:
- **Passive Health Checks**: Automatically monitors backend health based on HTTP responses, updates statuses, and retries intelligently.
- **Logging**: Utilizes YARP’s default logging to track load balancer activities and backend health.
- **Scalability**: Balances multiple backend instances and manages throttling states efficiently.

### Additional Resources:
- **Security Policy**: Follows industry-standard security practices and includes a security policy.
- **MIT License**: Open source under MIT license, ensuring broad usage and contribution.

This solution is designed to transparently increase Azure OpenAI service reliability and scalability for applications by managing backend instances and intelligently routing traffic based on real-time availability and priority.
## Microsoft-Semantic-Kernel-Community-dotnet
### Description

### Language
C#
### URL
[https://github.com/Azure-AI-Community/Microsoft-Semantic-Kernel-Community-dotnet](https://github.com/Azure-AI-Community/Microsoft-Semantic-Kernel-Community-dotnet)
### Summary
## Microsoft-Semantic-Kernel-Community-dotnet Summary

The Microsoft-Semantic-Kernel-Community is a platform that supports various plugins and connectors within the .NET ecosystem. The project includes several plugins with functionalities ranging from YouTube video searches to speech-to-text conversion, translation, intent recognition, and Bing Map suggestions. 

### Available Plugins:
1. **YouTube Plugin**: Allows keyword-based video searches within specific channels.
2. **Speech Plugin**: Converts spoken language to text and vice versa.
3. **Translation Plugin**: Translates text between languages.
4. **Intent Plugin**: Helps find intents.
5. **BingMap Plugin**: Provides address suggestions for places like hotels and restaurants.

### Upcoming Plugins:
1. **TextNumericConverterPlugin**: Converts textual representations to numeric values.
2. **Bing Video Plugin**: Enables access to Bing Video Search.
3. **Bing News Plugin**: Enables access to Bing News Search.

### Technical Details:
- The project addresses the limitation that the semantic kernel plugin core doesn't support interface-based plugins by default. This package focuses on interfaces for KernelFunction and its description.

### Metadata:
- **License**: MIT
- **Stars**: 17
- **Forks**: 2
- **Languages**: 100% C#

### Contributing:
Currently, no specific information on how to contribute is provided. The repository includes standard GitHub files like `.gitignore` and `LICENSE`.

### Additional Information:
No releases or packages have been published yet. The repository is part of the Hacktoberfest initiative, indicated by its topics. The main contributors are Vinoth Rajendran and Arafat Tehsin.

For more details, please refer to the repository's [README.md](#).
## ai-rag-chat-evaluator
### Description
Tools for evaluation of RAG Chat Apps using Azure AI Evaluate SDK and OpenAI 
### Language
Python
### URL
[https://github.com/Azure-Samples/ai-rag-chat-evaluator](https://github.com/Azure-Samples/ai-rag-chat-evaluator)
### Summary
This repository, "ai-rag-chat-evaluator", provides tools and scripts to evaluate Retrieval-Augmented Generation (RAG) chat applications using the Azure AI Evaluate SDK and OpenAI models. It contains resources to help improve the quality of chatbot responses by evaluating factors like coherence, relevance, groundedness, and more.

### Key Features:

- **Evaluation Tools:** Scripts to assess the performance of chat applications built on RAG architecture.
- **Ground Truth Data Generation:** Methods to create ideal answers for comparison, including manual and automated approaches.
- **Evaluation Script:** A Python script to run evaluations against chat apps, supporting both local and deployed environments.
- **Custom Metrics:** Besides built-in GPT metrics, custom metrics like latency, answer length, and citation checks.
- **Result Analysis:** Tools to view and compare evaluation results, helping to identify areas for improvement.
- **I Don't Know Capability:** Specific scripts and metrics to evaluate how well the app can refrain from answering unknown questions.
- **Setup Instructions:** Detailed steps for setting up the project in various environments, including Dev Containers and GitHub Codespaces.

### Setup:

1. **Install Python 3.10 or higher.**
2. **Create a virtual environment and install dependencies:**
   ```sh
   python -m pip install -r requirements.txt
   ```

### Usage:

1. **Deploy GPT-4 Model:** 
   - Either by creating a new Azure OpenAI instance using Azure Developer CLI or using an existing instance.
   - Alternatively, use an OpenAI.com instance.
   
2. **Generate Ground Truth Data:**
   - Manually or using provided scripts.

3. **Run Evaluation:**
   - Execute the evaluation script with specific configuration files.
   ```sh
   python -m scripts evaluate --config=example_config.json
   ```

4. **View Results:**
   - Use built-in tools to summarize and compare evaluation runs.

### License:
- The project is licensed under the MIT License.

This repository aims to make it easier to iterate and improve RAG-based chat applications by providing comprehensive evaluation and analysis tools.
## ai-hub
### Description
Enterprise Azure OpenAI Hub provides prescriptive architecture and guidance to accelerate Generative AI on Azure for all organisations, in a secure, compliant, scalable, and resillient way, and to democratize proven use-cases to quickly realise business value
### Language
HCL
### URL
[https://github.com/Azure/ai-hub](https://github.com/Azure/ai-hub)
### Summary
# Azure AI Hub

**Overview:** 
The Enterprise Azure OpenAI Hub is designed to accelerate the adoption and implementation of Generative AI on the Azure platform for organizations, ensuring security, compliance, scalability, and resilience. It offers prescriptive architecture and guidance to help businesses unlock the value of AI quickly.

**Key Features:**
1. **Comprehensive Learning Resource:** Provides intuitive and practical insights into using Azure services for AI applications.
2. **Library of Use Cases:** Contains proven patterns and best practices aligned with industry standards.
3. **Security and Compliance:** Focuses on secure and compliant AI development, important for regulated industries.
4. **Scalability:** Offers infrastructure that supports everything from simple proofs of concept to complex enterprise-wide AI solutions.
5. **Responsible AI:** Emphasizes ethical principles, human values, and minimizing potential harms in AI usage.

**Highlighted Use Cases:**
- **Image and Video Recognition:** Utilizing GPT-4 Vision and Azure AI Vision services to understand image and video content.
- **"On Your Data":** Leveraging Azure AI search for data vectorization and Azure OpenAI for embeddings to generate text-based solutions from enterprise data.

**Contribution Guidelines:**
- Welcomes contributions and suggestions.
- Requires a Contributor License Agreement (CLA) for contributions.
- Follow the Microsoft Open Source Code of Conduct and Trademark guidelines.

**Resources and Additional Information:**
- Repository includes architecture, design guidelines, security, compliance considerations, and more.
- Extensive documentation and step-by-step guidance for deploying use cases.

**License:** MIT License

**Contact and Support:** For more details, questions, or contributions, visit the official repository, security policy, and code of conduct documents.
## SQL-AI-samples
### Description
Samples using AI and Azure SQL DB
### Language
HTML
### URL
[https://github.com/Azure-Samples/SQL-AI-samples](https://github.com/Azure-Samples/SQL-AI-samples)
### Summary
The repository "SQL-AI-samples" on GitHub, maintained by Azure-Samples, contains a collection of sample projects that integrate AI capabilities with Azure SQL Database. It showcases how to build AI-driven applications using various Azure services. Key samples include:

1. **Azure SQL + Azure Cognitive Services**: Demonstrates product recommendations based on user reviews using Azure Cognitive Search.
2. **Azure SQL + Azure Promptflow**: An end-to-end example of AI application development with Prompt Flow, Azure Cognitive Search, and Azure OpenAI.
3. **Azure SQL + Azure OpenAI**: Shows how to get vector embeddings of text from Azure SQL and perform cosine similarity searches.
4. **Generating SQL using Vanna.AI**: Uses the vanna Python package to generate SQL queries via AI.
5. **Retrieval Augmented Generation (RAG)**: A step-by-step guide illustrating how to use Azure SQL and OpenAI to perform RAG, enabling natural language querying.
6. **Content Moderation**: T-SQL scripts for text analysis using Azure OpenAI for content safety and language AI.
7. **LangChain and Azure SQL Database**: Python notebooks demonstrating the use of LangChain for NL2SQL translation.

The repository highlights practical applications like a similarity search solution and a session assistant using various Azure services and technologies. Each sample includes detailed instructions and some have a working implementation available through linked GitHub repositories or live examples.

**Getting Started**: Instructions for each project are provided within their respective README files or the notebooks.

The project is covered under the MIT license and includes a code of conduct and a security policy.

**Primary Technologies**:
- HTML, Jupyter Notebook, Python, Jinja, TSQL
## azureai-samples
### Description
Official community-driven Azure AI Examples
### Language
Jupyter Notebook
### URL
[https://github.com/Azure-Samples/azureai-samples](https://github.com/Azure-Samples/azureai-samples)
### Summary
The repository "Azure-Samples/azureai-samples" on GitHub is a collection of official, community-driven examples for Azure AI. It includes end-to-end samples and smaller code snippets to help developers implement common tasks using Azure AI services. This repository is open source and encourages contributions from the community, adhering to Microsoft's Open Source Code of Conduct.

### Key Sections:
1. **Welcome**: Introduction to the repository and its purpose.
2. **Supplementary Documentation**: Links to additional repositories and documentation on Azure AI projects, such as Azure AI Studio, Azure AI Search, Azure AI Assistant, and OpenAI.
3. **Contributing**: Guidelines on how to contribute, including submitting bug reports, feature requests, and pull requests.
4. **Getting Help**: Directions on how to seek help if you encounter issues or want to request new features.

### Additional Information:
- **Languages Used**: Jupyter Notebook (69.1%), C# (13.0%), Python (10.8%), Bicep (3.7%), HTML (3.3%), and Jinja (0.1%).
- **License**: The repository is under the MIT license.
- **Metrics**: The repository has 213 stars and 145 forks, indicating active community engagement.
  
This repository is ideal for developers looking to explore and experiment with Azure AI scenarios on their local machines using a variety of programming frameworks and languages.
## contoso-chat
### Description
This sample has the full End2End process of creating RAG application with Prompt Flow and AI Studio. It includes GPT 3.5 Turbo LLM application code, evaluations, deployment automation with AZD CLI, GitHub actions for evaluation and deployment and intent mapping for multiple LLM task mapping.
### Language
Jupyter Notebook
### URL
[https://github.com/Azure-Samples/contoso-chat](https://github.com/Azure-Samples/contoso-chat)
### Summary
### Azure-Samples/contoso-chat GitHub Repository Summary

**Repository Overview:**
- *Name:* contoso-chat
- *Description:* This sample contains the end-to-end process of creating a Retrieval Augmented Generation (RAG) application using Prompt Flow and AI Studio. It utilizes GPT-3.5 Turbo LLM application code, and includes evaluations, deployment automation with Azure Developer CLI (AZD CLI), GitHub actions, and intent mapping for various LLM tasks.
- *Languages:* Primarily Jupyter Notebook (48.7%), Bicep (45.8%), Python (2.4%), Shell (2.1%).

**Functionality:**
- **Main Goal:** Provides a customer support chat application for a fictional online retailer, Contoso Outdoors, using a retrieval-augmented generation pattern to give grounded responses based on the retailer's product data and customer purchase history.
- **Key Features:**
  - Sample model configurations and prompts for RAG-based applications.
  - Managed Identity configuration for securing credentials.
  - Uses Azure AI Search, Azure Cosmos DB, and Azure OpenAI.
  - Deployment and evaluations automated using GitHub Actions and AZD CLI.
  - Detailed guidance for setup, deployment, and local development.

**Getting Started:**
- **Pre-Requisites:** Docker Desktop, Visual Studio Code, Azure Developer CLI, Python 3.10+, and Promptflow 1.10+.
- **Setup Options:** 
  1. **GitHub Codespaces:** Simplifies the environment setup using a cloud-hosted dev container.
  2. **VS Code Dev Containers:** Offers a locally-hosted alternative using Docker.
  3. **Manual Setup:** For advanced users setting up locally.

**Deployment Steps:**
1. Authenticate with Azure and deploy the application using `azd up`.
2. Monitor the deployment progress through Azure Portal, AI Studio, and test the deployed chat functionality.

**Local Development:**
- **Prompty Asset Exploration:** Example `chat.prompty` asset is provided for prompt engineering.
- **Testing:** Flex-flow feature allows testing using various methods (direct script execution or via a UI).

**Additional Information:**
- **Documentation and References:** Links to Azure AI Studio Documentation, Promptflow/Prompty Documentation, and related samples.
- **Security:** Emphasizes the use of Managed Identity and GitHub secret scanning for secure application development.
- **Costs and Availability:** Provides guidance on region availability and cost estimation for various Azure services used.

**Contributing:**
- Welcomes contributions and suggestions, with a requirement to agree to a Contributor License Agreement (CLA).
- Adheres to Microsoft's Open Source Code of Conduct.

**License:** MIT License

**Activity:**
- Stars: 380
- Forks: 2.3k
- Watchers: 24
- Contributors: 17

**Links:**
- Code of conduct
- Security policy

This repository serves as a comprehensive resource for developers looking to implement a conversational AI agent using advanced LLM capabilities on Azure, with a focus on easy deployment and secure best practices.
## contoso-web
### Description
Contoso Outdoors Company web application shown at Microsoft Ignite
### Language
TypeScript
### URL
[https://github.com/Azure-Samples/contoso-web](https://github.com/Azure-Samples/contoso-web)
### Summary
This GitHub repository, "Azure-Samples/contoso-web," houses the Contoso Outdoors Company's web application showcased at Microsoft Ignite. The application is built using Next.js and Tailwind CSS and includes assets created by DALLE-3 and GPT-4.

### Key Features:
1. **Chat Functionality**: The application includes three types of chat experiences:
   - Regular Chat with prompt flow (requires Contoso Chat repo setup).
   - Grounded Chat via Azure AI Studio's "Add Your Data" feature.
   - Visual Chat using video or image upload, demonstrated at Microsoft Ignite.
   
2. **Setup Instructions**:
   - To run the development server, the following commands can be used: `npm run dev`, `yarn dev`, `pnpm dev`, or `bun dev`.
   - Essential environment endpoints must be defined in a `.env` file: `CONTOSO_SEARCH_ENDPOINT`, `CONTOSO_SEARCH_KEY`, `CONTOSO_AISERVICES_ENDPOINT`, `CONTOSO_AISERVICES_KEY`, `PROMPTFLOW_ENDPOINT`, `PROMPTFLOW_KEY`, `VISUAL_ENDPOINT`, and `VISUAL_KEY`.

3. **Debugging**:
   - The application includes console debug statements to track responses from various endpoints, aiding in debugging.

### Future Enhancements:
- Implementing streaming chat outputs instead of full response waits.
- Feedback and additional suggestions are welcome.

### Repository Details:
- **License**: MIT License
- **Contributors**: Microsoft Open Source and Seth Juarez
- **Primary Language**: TypeScript (93.8%), followed by Dockerfile (5.5%) and other files (0.7%).

### Additional Resources:
- README, code of conduct, and no packages or releases have been published yet. 

### Community:
- The repository has 40 stars, 55 forks, and 13 watchers. 

This repository is a practical demonstration of integrating AI-driven functionalities into a web application, providing developers with a robust example to follow.
## AI-in-a-Box
### Description

### Language
Jupyter Notebook
### URL
[https://github.com/Azure/AI-in-a-Box](https://github.com/Azure/AI-in-a-Box)
### Summary
**GitHub Repository: Azure/AI-in-a-Box**

**Overview:**
AI-in-a-Box is a repository developed by Microsoft Customer Engineers and Architects aimed at providing curated AI and ML solutions to the technical community. It includes solution accelerators designed to help engineers rapidly establish their AI/ML environments while maintaining quality and efficiency.

**Key Features:**
- **Accelerated Deployment**: Ready-to-use patterns for faster solution implementation.
- **Cost Savings**: Reuse existing code and patterns to maximize budgets.
- **Enhanced Quality & Reliability**: Real-world validated solutions.
- **Competitive Advantage**: Speed up solution deployment to outpace competition.

**Guidance Documentation:**
- **Responsible AI**: Essential guidelines on responsible AI usage.
- **Security for Generative AI Applications**: Specific security guidance for GenAI applications.
- **Scaling OpenAI Applications**: Best practices for scaling OpenAI apps within Azure.

**Available “-in-a-Box” Accelerators:**
1. **Azure ML Operationalization in-a-box**: End-to-end MLOps template.
2. **Edge AI in-a-box**: Model creation and deployment on edge devices.
3. **Doc Intelligence in-a-box**: Automate PDF form processing.
4. **Image and Video Analysis in-a-box**: Extract information using Azure AI Vision.
5. **Cognitive Services Landing Zone in-a-box**: Enterprise-ready networking for AI services.
6. **Semantic Kernel Bot in-a-box**: Extendable solutions for Azure OpenAI bots.
7. **NLP to SQL in-a-box**: Speech-enabled SQL query system with Azure OpenAI.
8. **Assistants API notebooks**: Integrate versatile digital assistants.
9. **Assistants API Bot in-a-box**: Deploy a virtual assistant using Azure OpenAI.

**Contributors and Contact Details:**
The repository lists key contacts and contributors with their GitHub IDs and email addresses for any queries or contribution discussions.

**Additional Information:**
- **License**: MIT License
- **Code of Conduct**: Provided for community interaction
- **Security Policy**: Detailed security measures

This comprehensive repository aims to equip the technical community with tools and resources for evolving AI and ML needs.
## semantic-kernel-bot-in-a-box
### Description
Extensible Semantic Kernel Bot Solution Accelerator
### Language
C#
### URL
[https://github.com/Azure/semantic-kernel-bot-in-a-box](https://github.com/Azure/semantic-kernel-bot-in-a-box)
### Summary
### Summary: Azure/semantic-kernel-bot-in-a-box

**Repository:** Azure/semantic-kernel-bot-in-a-box

**Description:** This project provides an extensible Semantic Kernel bot solution that can be deployed to Azure. It serves as a solution accelerator for creating bots that utilize Semantic Kernel, Azure OpenAI, and various Azure services.

#### Key Features:
1. **Extensible Bot Template:** Facilitates creating bots that handle various user requests via a stepwise planner.
2. **Integration:** Uses Azure Bot Services, .NET applications, Azure OpenAI, Cognitive Search, and Azure SQL.
3. **Sample Scenarios:** Covers various functionalities like general knowledge questions, retrieval-augmented generation, structured data retrieval, document uploads, and image generation.
4. **Custom Plugins:** Users can develop and integrate their own plugins.

#### Solution Architecture:
- **Message Flow:** 
  1. End-users interact via Web, PowerBI, or Teams.
  2. Messages processed by Azure Bot Services.
  3. Communicates with a .NET app running on App Services.
  4. The .NET app executes steps through Semantic Kernel, using Azure OpenAI for data source decisions.
  5. Uses Cognitive Search for hotel data, and Azure SQL for customer data.

#### Prerequisites:
- **Local Setup:** .NET & Bot Framework Emulator.
- **Azure Deployment:** Azure CLI, Azure Developer CLI, Azure subscription login.

#### Deployment Steps:
1. Clone the repository.
2. Deploy resources using `azd up`.
3. Test on Web Chat via Azure portal.

#### Local Development:
- Deploy resources to Azure first.
- Rename and configure `appsettings.example.json` to `appsettings.json`.
- Run with `dotnet run` and connect via Bot Framework Emulator.

#### Sample Scenarios:
- Supports questions related to general knowledge, hotels, customer data, and more.
- Allows document-based queries and image generation.

#### Customization:
- **Creating Plugins:** Develop new plugins within the project's Plugins directory and integrate them into the bot.
- **Web Chat Deployment:** Configure Azure Bot's Direct Line channel and make the bot publicly available (authentication recommended).

#### Contribution Guidelines:
- Contributions welcome, requires signing a Contributor License Agreement (CLA).
- Follow the Microsoft Open Source Code of Conduct.

#### Trademarks:
- Usage of Microsoft trademarks must comply with Microsoft's Trademark & Brand Guidelines. Third-party trademarks must follow respective policies.

**Languages Used:** 
- C# (71.1%)
- Bicep (25.9%)
- HTML (3%)

**License:** MIT

**Important Note:** This repository will be archived in February 2024. The latest version of this solution can be found in the [AI-in-a-Box repository](https://aka.ms/ai-in-a-box).

---

This summary captures the essence of the repository, including its features, setup instructions, and contribution guidelines. For more detailed information, visit the repository on GitHub.
## intro-to-intelligent-apps
### Description
This repository introduces and helps organizations get started with building Intelligent Apps and incorporating Large Language Models (LLMs) via AI Orchestration into them.
### Language
Jupyter Notebook
### URL
[https://github.com/Azure/intro-to-intelligent-apps](https://github.com/Azure/intro-to-intelligent-apps)
### Summary
### Summary of GitHub - Azure/intro-to-intelligent-apps Repository

**Purpose:**
This repository helps organizations get started with building Intelligent Apps and incorporating Large Language Models (LLMs) using AI Orchestration.

**Key Features:**
- **Workshop Agenda:**
  - **Morning (9:00 – 12:15):** Introduction, first steps, and prompt engineering.
    - Introduction and setting expectations.
    - Use case ideation and brainstorming.
    - Intro to Azure OpenAI, prompt engineering, and demonstrations.
    - Hands-on lab with prompt engineering exercises.
    - Introduction to AI orchestration with demos.
  - **Afternoon (1:15 – 4:30):** Building AI apps and integrating LLMs.
    - Continued AI orchestration exercises.
    - Hands-on labs for integrating, orchestrating, and deploying AI.
    - Use case validation, Q&A, and closing remarks.

- **Getting Started:** Steps to set up Azure OpenAI and configure necessary files for hands-on labs.

- **Post Workshop:** Suggestions for next steps after completing the workshop.

**Contributing:**
- Contributions and suggestions are welcome. Contributors need to agree to a Contributor License Agreement (CLA).
- The repository follows the Microsoft Open Source Code of Conduct.

**Technical Details:**
- The repository includes Jupyter Notebooks, Python scripts, C#, and Dockerfiles.
- It has an MIT license.

**Repository Activity:**
- Stars: 174
- Forks: 251
- Contributors: 19

This repository provides a comprehensive guide for organizations to incorporate LLMs into Intelligent Apps through hands-on labs and practical AI orchestration scenarios.
## aoai-net-starterkit
### Description
Azure OpenAI Starter Kit for .NET Developers
### Language
C#
### URL
[https://github.com/Azure-Samples/aoai-net-starterkit](https://github.com/Azure-Samples/aoai-net-starterkit)
### Summary
### Summary of Azure OpenAI Starter Kit for .NET Developers

The **Azure OpenAI Starter Kit for .NET Developers** repository is designed to assist developers in integrating Azure AI services, particularly Azure OpenAI, into applications. It provides resources for both learning and practical implementation:

1. **Learning Resources**: The `docs` folder contains polyglot notebooks that explain the fundamental concepts of integrating Azure OpenAI into custom applications. These notebooks include examples that are easy to understand and demonstrate Azure OpenAI functionalities.

2. **Practical Scenarios**: The repository offers detailed end-to-end scenarios that can be used as templates for incorporating Azure OpenAI functionalities into various applications. This helps developers quickly adopt and implement sophisticated AI features.

### Key Areas Covered:
- **Fundamental Concepts**: Basics of using Azure OpenAI, including Function Calling, Semantic Kernel, GPT-4 Vision for image analysis, and the Azure OpenAI Assistants API.
- **Call Center Use Cases**: Practical examples and solutions specific to call centers, such as building a custom policy check engine using embeddings.

### Getting Started:
1. Clone the repository.
2. Follow setup instructions provided in the notebooks to prepare the development environment.
3. Customize the provided code as needed.
4. Explore additional resources on Microsoft Learn for further insights into architecture and application.

### Technical Stack:
- Primarily written in **C#** (99.9%), with some **HTML** (0.1%).

The repository includes a comprehensive set of resources, guides, and practical examples aimed at helping .NET developers leverage Azure AI services to build AI-powered applications. 

**License**: MIT

For further details, refer to the README and associated documentation within the repository.
## Vector-Search-AI-Assistant
### Description
Microsoft Official Build Modern AI Apps reference solutions and content. Demonstrate how to build Copilot applications that incorporate Hero Azure Services including Azure OpenAI Service, Azure Container Apps (or AKS) and Azure Cosmos DB for NoSQL with Vector Search.
### Language
C#
### URL
[https://github.com/Azure/Vector-Search-AI-Assistant](https://github.com/Azure/Vector-Search-AI-Assistant)
### Summary
The GitHub repository "Azure/Vector-Search-AI-Assistant" by Microsoft provides reference solutions and content for building modern AI applications. The main focus is on creating Copilot applications using key Azure services such as Azure OpenAI Service, Azure Container Apps (or AKS), and Azure Cosmos DB for NoSQL with Vector Search. This repository includes code and resources to demonstrate a Generative AI solution using a retail bike shop scenario as an example. Key concepts covered include real-time vector generation, vector searches, integrating large language models, managing conversational context, and using the Semantic Kernel SDK. Deployment scripts and instructions are provided for Azure Kubernetes Service (AKS) and Azure Container Apps (ACA). 

**Key highlights:**
- Incorporates Azure Cosmos DB, Azure OpenAI, and other Azure services for building AI solutions.
- Example scenario: Intelligent Agent for a retail bike shop.
- Covers concepts like Retrieval Augmented Generation (RAG), token management, and vectorized data search.
- Detailed deployment steps for AKS and ACA.
- Cleanup scripts for resource management.

**Resources included:**
- Azure Cosmos DB Vector Database Concepts
- Semantic Kernel Overview
- Code, issues, and pull request management

**Usage:**
Deploy and manage using provided scripts, explore solution architecture, and understand key concepts for AI and vectorized data applications. The repository is under the MIT license, and contributions are welcome.
## communication-services-AI-customer-service-sample
### Description
A sample app for the customer support center running in Azure, using Azure Communication Services and Azure OpenAI for text and voice bots.
### Language
C#
### URL
[https://github.com/Azure-Samples/communication-services-AI-customer-service-sample](https://github.com/Azure-Samples/communication-services-AI-customer-service-sample)
### Summary
The repository `Azure-Samples/communication-services-AI-customer-service-sample` on GitHub provides a sample application intended for customer support centers using Azure Communication Services combined with Azure OpenAI for creating text and voice bots. This application, fit for deployment on Azure, integrates various Azure services to provide an intelligent customer service solution capable of natural language interactions. Key features include:

1. **Chat Bot**: Utilizes company knowledge base for answering questions.
2. **Retrieval Augmented Generation (RAG)**: Leverages Azure Cognitive Search with Azure OpenAI for retrieving and processing information.
3. **Escalation Path**: From chatbot interaction to human technician via a PSTN call.
4. **Job Router**: Assigns tasks to suitable technicians based on various criteria.
5. **Communication Services for Automation**: Converts voice to text and vice versa, sends emails, and generates summaries using AI.

### Deployment and Running:

- **Costs**: Varies by region and resource use, with potential to reduce costs by using free SKUs for some services.
- **Pre-requisites**: Active Azure account, local environment setup including Azure Dev Tunnels CLI, .NET 7, and PowerShell 7+ for Windows.
- **Steps**: Clone the project, run deployment scripts (`start.ps1` or `start.sh`), configure Azure resources, and link communication services.

### Manual Setup:
Essential configurations via Azure portal such as connecting AI services, setting up phone numbers, and email domain.

### Local Environment:
Use Azure DevTunnels to host local services on the internet, update configurations, and run backend and frontend applications.

### Troubleshooting:
Check backend application logs via Azure portal to troubleshoot issues.

### Resources:
Links to Azure Communication Services Blog, Microsoft Mechanics video showcasing the sample, and other related Azure services documentation.

The app represents a demo of AI-driven customer service capabilities and features like speech-to-text are in public preview.
## azure-search-openai-javascript
### Description
A TypeScript sample app for the Retrieval Augmented Generation pattern running on Azure, using Azure AI Search for retrieval and Azure OpenAI and LangChain large language models (LLMs) to power ChatGPT-style and Q&A experiences.
### Language
TypeScript
### URL
[https://github.com/Azure-Samples/azure-search-openai-javascript](https://github.com/Azure-Samples/azure-search-openai-javascript)
### Summary
### Summary

This repository, **Azure-Samples/azure-search-openai-javascript**, contains a TypeScript sample application implementing the Retrieval Augmented Generation (RAG) pattern using Azure services. It leverages **Azure AI Search** for data retrieval and **Azure OpenAI** with **LangChain** large language models (LLMs) to provide ChatGPT-style and Q&A interactions.

**Key Features:**
- Integration of ChatGPT for chat and Q&A interfaces.
- Search service backend, data indexing, and a front-end web application.
- Examples of data preparation, prompt construction, and interactions between ChatGPT and Azure AI Search.
- Monitoring and performance tracing with Application Insights.

**Getting Started:**
- Requires an Azure account with specific permissions to deploy and execute.
- Supports various setups including GitHub Codespaces and local environments.
- Detailed instructions are provided for deploying from scratch or reusing existing Azure resources.
  
**Deployment:**
- Use Azure Developer CLI (`azd`) to automate the deployment.
- Cost considerations are outlined with links to detailed pricing information for relevant Azure services.
- Instructions for enabling optional features such as authentication and CORS.

**Resources and Clean-up:**
- Guides and references for further learning.
- Instructions for cleaning up resources created by the sample to avoid unnecessary costs.

**FAQs and Troubleshooting:**
- Addresses common issues and detailed steps for dealing with deployment and set-up problems.

**Technologies Used:**
- TypeScript, JavaScript, Node.js, Fastify for backend.
- React/Lit for frontend.
- Azure AI services including OpenAI and AI Search, with deployment orchestrated using Azure Developer CLI.

The README provides comprehensive instructions on how to set up, deploy, and use the sample application, along with necessary resource management and optional configurations for production use.
## azure-openai-rag-workshop
### Description
Create your own ChatGPT with Retrieval-Augmented-Generation workshop
### Language
Bicep
### URL
[https://github.com/Azure-Samples/azure-openai-rag-workshop](https://github.com/Azure-Samples/azure-openai-rag-workshop)
### Summary
# Summary for Azure-Samples/azure-openai-rag-workshop

## Overview
The **Azure OpenAI RAG Workshop** repository provides resources and instructions to create an AI chat experience similar to ChatGPT using Retrieval-Augmented Generation (RAG). This entails leveraging technologies like LangChain.js and OpenAI's language models and deploying them on Azure services. The goal is to help users build and deploy sophisticated AI applications.

## Key Features
- **Technologies Used**: The project employs Node.js, Fastify for server-side operations, Azure AI Search as the vector database, and a frontend for interaction.
- **Deployment Options**: Users can work on the project using GitHub Codespaces, Docker, or local development environments. Deployment to Azure is facilitated through easy-to-follow commands.
- **Workshop Instructions**: Comprehensive instructions are provided for setting up and deploying the application. Users must have permissions to access certain Azure resources.
  
## Architecture
The application is structured as a monorepo, with all source code located under the `src/` directory.

## Running and Deploying
1. **Local Development**: Users can set up the environment locally by following detailed instructions.
2. **Deployment**: Using `azd auth login` and `azd up` commands, users can deploy the app to Azure.

## Cleanup
To clean up the resources created in Azure, users can execute `azd down --purge`.

## Additional Resources and Versions
- **Multiple Versions**: The workshop is available in different tech stacks, including Java/Quarkus and various database integrations.
- **References**: Links to LangChain.js documentation, Azure AI service, and more are provided for further learning.

## Contributing
The project welcomes contributions. Contributors must sign a Microsoft Contributor License Agreement (CLA).

## Keywords
- Node.js
- Workshop
- Azure
- OpenAI
- Fastify
- RAG
- AI Chatbot

## License and Conduct
- **License**: MIT License
- **Code of Conduct**: The repository adheres to Microsoft's Open Source Code of Conduct.

For more detailed instructions and resources, users are encouraged to visit the repository and follow the provided guidelines.
## azure-search-power-skills
### Description
A collection of useful functions to be deployed as custom skills for Azure Cognitive Search
### Language
C#
### URL
[https://github.com/Azure-Samples/azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills)
### Summary
The Azure-Samples/azure-search-power-skills repository on GitHub provides a collection of useful functions intended to be deployed as custom skills for Azure Cognitive Search, now renamed to Azure AI Search as of November 15, 2023. These skills can serve as templates, starting points for creating your own skills, or can be used as-is if they suit your needs. Examples of provided skills include retrieving coordinates from place names (GeoPointFromName), defining known acronyms (AcronymLinker), anonymizing PII entities (Anonymizer), and various text and vision processing tasks.

### Key Features:

- **Custom Skills**: Includes geography, text, vision, utility, and template skills.
- **Deployment**: Skills can be run locally using Visual Studio or deployed to Azure. Some skills require additional configuration or external Azure services.
- **Getting Started**: Cloning the repository, opening it in Visual Studio, setting the function to test as the startup project, and hitting F5 to run locally. You can also test skills using Postman.
- **Contribution**: Users are encouraged to contribute by improving documentation, configurations, and deployment files.

### Prerequisites:
- Active Azure subscription.
- Visual Studio 2019 recommended.
- Postman for testing.

### Additional Resources:
- Contribution guidelines.
- References to Azure Search, Azure Functions, and other related tools.

The repository is open-source under the MIT license and has garnered attention with 273 stars, 164 forks, and contributions from 33 collaborators.
## openai-at-scale
### Description
Simple ChatGPT UI application
### Language
TypeScript
### URL
[https://github.com/Azure/openai-at-scale](https://github.com/Azure/openai-at-scale)
### Summary
**Azure/openai-at-scale: Simple ChatGPT UI Application**

This repository provides a simple ChatGPT user interface application, developed as part of the FastTrack for Azure workshop by Microsoft. It helps users build and deploy a ChatGPT application on Azure.

### Key Features:
- **Chat UI**: Provides a user interface for interacting with ChatGPT.
- **Configuration**: Allows setting system prompts and hyperparameters.
- **Authentication**: Uses Azure Active Directory for user authentication and retrieves user information from Microsoft Graph.
- **Logging**: Collects application logs using Azure Log Analytics.
- **Data Storage**: Stores prompt logs in Azure Cosmos DB.

### Getting Started:
To run this application, either locally or on Azure, the following prerequisites are needed:
- **OS**: Windows 11, macOS, or Linux.
- **For Windows users**: Use Ubuntu 20.04 LTS (Windows Subsystem for Linux).
- **Environments**: Azure CLI, Node.js (v16.20+), Python (v3.9+), Git client, and Docker Desktop.

### Steps to Deploy:
1. **Create Azure OpenAI Service**: Using either the Azure Portal or Azure CLI.
2. **Create Azure Active Directory Application**: Register the application.
3. **(Optional) Create Azure Cosmos DB**: Choose Core (SQL) API for your account.
4. **Deploy Locally**:
   - Set up environment variables.
   - Install necessary Python libraries and Node.js packages.
   - Launch backend and frontend services.
5. **Deploy to Azure**:
   - Use Azure App Service for deployment.
   - Optionally, configure VNET Integration and Private Endpoint.
   - Update environment variables and rebuild the frontend.

### Configuration:
(Optional) Application logs can be collected using Azure Log Analytics, and prompt log data can be stored in Azure Cosmos DB.

### Contribution:
Azure/openai-at-scale supports contributions from customers and Microsoft employees. Check out the CONTRIBUTING.md for more details.

### Resources:
- The repo is based on existing sample code for integrating ChatGPT with Azure OpenAI and Cognitive Search.
  
This project utilizes various technologies including JavaScript, Python, TypeScript, Azure services, and more. Contributions to the project are welcome and appreciated. 

**License**: MIT

For more details, refer to the repository on GitHub.
## azure-openai-samples
### Description
Azure OpenAI Samples is a collection of code samples illustrating how to use Azure Open AI in creating AI solution for various use cases across industries. This repository is mained by a community of volunters. We welcomed your contributions. 
### Language
Jupyter Notebook
### URL
[https://github.com/Azure/azure-openai-samples](https://github.com/Azure/azure-openai-samples)
### Summary
**Azure OpenAI Samples Repository Summary:**

This GitHub repository, managed by community volunteers, provides a collection of code samples demonstrating the use of Azure Open AI for various industry applications. Key features include:
- **Resources:** Quick Start guides, fundamental tutorials, sample use cases, and end-to-end solutions for tasks like question answering, text summarization, and sentiment analysis using GPT-3.5.
- **Setup:** Instructions for configuring an `.env` file for Azure service keys.
- **Contributions:** Open for community contributions to keep the repository updated.
- **Solution Accelerators:** Examples include Business Process Automation, Azure Cognitive Search + OpenAI, PowerApp integration, Azure SQL Database, and more.
- **Relevant Repositories:** Links to related projects and demos for further exploration.

The repository is under the MIT license and actively seeks contributions to expand its contents.
## aistudio-copilot-sample
### Description
Sample quickstart repo for getting started building an enterprise chat copilot in Azure AI Studio
### Language
Python
### URL
[https://github.com/Azure/aistudio-copilot-sample](https://github.com/Azure/aistudio-copilot-sample)
### Summary
### Azure AI Studio Copilot Sample Repository

This repository offers a quickstart guide for building an enterprise chat copilot using Azure AI Studio. Key features and steps include:

#### Important Notices
- **Deprecation**: This repository is no longer maintained. For the latest code, use the repository at [Azure-Samples/rag-data-openai-python-promptflow](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/tree/main).
- **Preview Features**: The features are in preview and come without any service level agreement. They are not recommended for production workloads.

#### Getting Started
1. **Development Environment Setup**:
   - **Cloud Development**: Use GitHub Codespaces or Azure AI curated VS Code environment.
   - **Local Development**: Clone the repository, create a Python virtual environment, and install the SDK packages.

2. **Azure Resource Configuration**:
   - Deploy necessary models in Azure AI Model Catalog.
   - Set Azure environment variables in a `.env` file.

3. **Build an Azure AI Search Index**:
   - Use the provided or your custom markdown files.
   - Create the index using provided Python scripts.

4. **Run the Copilot**:
   - Execute single question & answer queries.
   - Test different implementations such as `promptflow`, `langchain`, or `aisdk`.

5. **Evaluation**:
   - Evaluate copilot implementations using different models.

6. **Deployment**:
   - Deploy the implementation to an online endpoint and test it.

#### Customization and Contribution
- Customize the development container by updating the Dockerfile.
- Contributions are welcomed, with a Contributor License Agreement (CLA) required for submissions.
- The project adheres to the Microsoft Open Source Code of Conduct.

#### Additional Resources
- Detailed steps and code samples are provided for setting up, running, and customizing your copilot solutions.
- For further information and questions, refer to the Code of Conduct FAQ or contact opencode@microsoft.com.

The repository is maintained under the MIT license and primarily involves Python code.
## azure-search-vector-samples
### Description
A repository of code samples for Vector search capabilities in Azure AI Search.
### Language
Jupyter Notebook
### URL
[https://github.com/Azure/azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples)
### Summary
The repository "azure-search-vector-samples" on GitHub, created by Azure, contains a variety of code samples demonstrating the vector search capabilities in Azure AI Search. The samples include implementations in Python, C#, Java, and JavaScript, and cover features like vector indexing, vector queries, and integrated data chunking and embedding. These samples are designed to help developers create, load, and query vector data using Azure's AI Search services and tools.

Noteworthy aspects include:
- Generally available features like vector indexing and vector queries.
- Public preview features including integrated data chunking, embedding, vectorizers, quantization, and support for binary vectors.
- Several demonstration applications across different programming languages, showing practical usage examples and covering scenarios such as OpenAI integration and retrieval-augmented generation.

The repository also offers additional resources like documentation links and sample applications that apply vector search in various use cases using Azure OpenAI and Azure's cognitive search services.

Key technologies used in the repository include Jupyter Notebook, Bicep, Python, C#, Java, JavaScript, and PowerShell, with the bulk of the code being written in Jupyter Notebook. The project is licensed under the MIT license.
## azure-search-knowledge-mining
### Description
Azure Search Knowledge Mining Accelerator
### Language
CSS
### URL
[https://github.com/Azure-Samples/azure-search-knowledge-mining](https://github.com/Azure-Samples/azure-search-knowledge-mining)
### Summary
The "Azure Search Knowledge Mining Accelerator" repository on GitHub provides developers with resources to quickly build a Knowledge Mining prototype using Azure AI Search. This repository offers:

- **Templates** for deploying Azure resources and creating a search index.
- **Web UI Template** for building a basic web application interface.
- **Custom Skills** examples to tailor the solution for specific use cases.
- **PowerBI Reports** to monitor search solution performance.
- **Sample Documents** for testing purposes.
- **Workshop** materials for a self-paced learning experience.

### Prerequisites:
- An Azure subscription.
- Visual Studio 2019 or later.
- Postman API client.
- Data in supported formats for Azure Search Indexers.

### Key Steps:
1. **Resource Deployment**: Instructions for deploying necessary Azure resources.
2. **Search Index Creation**: Use of Postman collections to create and customize search indices.
3. **Web UI Template**: Guide to integrating search indices with a .NET Core web app.
4. **Data Science & Custom Skills**: Instructions for adding bespoke functionalities.
5. **Reporting**: Pre-built PowerBI templates to analyze user search behavior.

The accelerator aims to facilitate quick setup and deployment of a knowledge mining solution by using best practices and a structured approach. 

For more information, the repository includes comprehensive documentation and a licensing agreement under the MIT license.
## azure-sql-db-openai
### Description
Samples on how to use Azure SQL database with Azure OpenAI
### Language
TSQL
### URL
[https://github.com/Azure-Samples/azure-sql-db-openai](https://github.com/Azure-Samples/azure-sql-db-openai)
### Summary
**Repository Overview:**

- **Name:** `Azure-Samples/azure-sql-db-openai`
- **Description:** This repository provides samples on how to integrate Azure SQL Database with Azure OpenAI to perform vector similarity searches.

**Key Features and Instructions:**

1. **Vector Similarity Search:**
   - **Objective:** Use Azure OpenAI to obtain vector embeddings for given text and calculate cosine similarity with precomputed embeddings from Wikipedia articles.
   - **Native Option:** Utilize new Vector Functions in Azure SQL to perform vector operations. (Currently in Early Adopter Preview)
   - **Classic Option:** Use traditional T-SQL with columnstore indexes for vector operations.

2. **Setup Instructions:**
   - **Download Wikipedia Vector Embeddings:** Import the provided CSV file into Azure Blob Storage and then into Azure SQL Database.
   - **Add Embedding Columns:** Convert JSON arrays to a more efficient binary format using provided SQL scripts.
   - **Perform Similarity Search:**
     - Deploy an Azure OpenAI embeddings model.
     - Use stored procedures in Azure SQL to call OpenAI API, obtain embeddings, and calculate cosine similarity.
   
3. **Encapsulated Logic:**
   - Stored procedures and functions have been provided to streamline the process of retrieving embeddings and performing similarity searches.

4. **Alternative Approach with Python:**
   - Use local embeddings models (e.g., from Hugging Face) instead of OpenAI.
   - Python scripts provided to generate embeddings, perform similarity searches, and apply ranking techniques.

5. **Conclusions:**
   - Azure SQL now supports direct vector operations, enhancing its capability for vector similarity search and integration with fulltext search for more robust search engine solutions.

**Technical Details:**
- Primary Languages: T-SQL (51.7%), Python (48.3%)
- License: MIT License

**Additional Resources and Links:**
- [Azure SQL Vector Functions - Early Adopter Preview](https://aka.ms/azuresql-vector-eap-announcement)
- [More on Azure SQL & AI](https://docs.microsoft.com/en-us/azure/azure-sql/database/introduction-ai)
- Sample scripts for various setup stages and functionalities are provided within the repository.

**Repository Metrics:**
- **Stars:** 65
- **Forks:** 22
- **Watchers:** 14
## Build-Modern-AI-Apps-Hackathon
### Description
A 1-2 day hackathon to help users learn the concepts and technical skills to build AI-enabled applications and services in Azure.
### Language
C#
### URL
[https://github.com/Azure/Build-Modern-AI-Apps-Hackathon](https://github.com/Azure/Build-Modern-AI-Apps-Hackathon)
### Summary
### Summary of Azure/Build-Modern-AI-Apps-Hackathon

**Repository Purpose:**
This repository is designed for a 1-2 day hackathon aimed to teach users the technical skills and concepts necessary for building AI-enabled applications and services using Azure.

**Hackathon Scenario:**
Participants will work on developing a Proof of Concept (POC) for a chat interface. This chat interface enables users to interact with a virtual agent to fetch product and account information, using data from Azure Cosmos DB (a retail dataset) and managed with Azure Cognitive Search.

**Key Technologies and Tools:**
- **Azure Services:**
  - Azure Cosmos DB
  - Azure OpenAI Service
  - Azure Cognitive Search
  - Azure Kubernetes Service (AKS) or Azure Container Apps (ACA)
  
- **Development Tools:**
  - Visual Studio
  - .NET 7 SDK
  - Docker Desktop
  - Azure CLI (version 2.49.0)
  - Helm (for AKS deployments)

**Activities and Goals:**
1. **Store and Manage Chat Data:**
   - Store chat messages in a Cosmos DB database.
   
2. **Create Vector Embeddings:**
   - Use Azure OpenAI service to produce vector embeddings and chat completions.
   
3. **Search Functionality:**
   - Use Azure Cognitive Search to create a vector database for querying product and account information.
   
4. **Data Loading and Handling:**
   - Load existing data into Cosmos DB and Azure Cognitive Search.
   
5. **Conversation Management:**
   - Implement a process to manage chat flow, vectorization, search operations, data handling, and response generation.
   
6. **Deployment and Setup:**
   - Clone the repository and set up the environment.
   - Deploy Azure core services using scripts (`Starter-Deploy.ps1`).
   - Verify initial deployment.
   - Configure local settings for running the solution in Visual Studio.
   
7. **Debugging and Running Locally:**
   - Debug and run the application locally with Visual Studio.

**Practical Information:**
- Participants need an Azure subscription with specific permissions.
- Instructions on setting up Azure resources are provided.
- Consideration of containerization approach, choosing between AKS and ACA.
- Ensure necessary Azure services and models are appropriately configured and deployed.

**Teardown:**
- After completion of the hackathon, delete the created resource group to clean up.

**Repository Statistics:**
- Stars: 57
- Forks: 40
- Contributors: 9

**Licensing:**
- The project is licensed under the MIT license.

This setup facilitates learning in a hands-on environment, allowing participants to explore the practical application of Azure AI services and containerized deployment in modern software development.
## semantic-kernel-rag-chat
### Description
Tutorial for ChatGPT + Enterprise Data with Semantic Kernel, OpenAI, and Azure Cognitive Search
### Language
C#
### URL
[https://github.com/Azure-Samples/semantic-kernel-rag-chat](https://github.com/Azure-Samples/semantic-kernel-rag-chat)
### Summary
The repository "semantic-kernel-rag-chat" provides a comprehensive tutorial for developing an AI chat application using ChatGPT integrated with enterprise data through the Semantic Kernel, OpenAI, and Azure Cognitive Search. The tutorial is divided into three chapters:

1. **ChatGPT Integration** - It introduces setting up a basic chat application using Semantic Kernel in Azure Functions.
   
   - **Requirements**: Visual Studio Code, .NET 7 SDK, Azure Function Core Tools, OpenAI API key.
   - **Steps**: Clone the repository, configure an Azure Function project, integrate Semantic Kernel, and test locally.

2. **Memories for Enterprise Data** - This chapter extends the application by incorporating a memory store to enhance AI responses with enterprise data.

   - **Requirements**: Docker Desktop for hosting Qdrant, a vector search engine.
   - **Steps**: Add Qdrant memory store to the Azure Function, import data (e.g., Microsoft 2022 10-K financial report), and test the enhanced chat locally.

3. **Azure Cognitive Search Integration** - This chapter replaces the vector-based memory store with Azure Cognitive Search to utilize semantic search for more accurate responses.

   - **Requirements**: Azure Cognitive Search service, API key, and endpoint URL.
   - **Steps**: Add Azure Cognitive Search memory to the Azure Function, configure and import data into Azure Cognitive Search, and test the updated chat application.

The README also includes appendices for deploying the Azure Function to Azure and provides various resources, including links to more detailed documentation, a code of conduct, and security policies. 

Special acknowledgment is given to Adam Hurwitz for sample data used in the tutorial.

**Key Features:**
- Step-by-step instructions for building a chat application.
- Integration with enterprise data using Semantic Kernel.
- Detailed setup for Qdrant and Azure Cognitive Search.
- Guidance on running and testing the application locally and deploying it to Azure.

**Repository Meta:**
- License: MIT
- Contributors: Gina Triolo and Adrian Bonar
- Languages: C# only
- Archived Status: The repository is read-only as of January 21, 2024.
## azure-search-openai-demo
### Description
A sample app for the Retrieval-Augmented Generation pattern running in Azure, using Azure AI Search for retrieval and Azure OpenAI large language models  to power ChatGPT-style and Q&A experiences.
### Language
Python
### URL
[https://github.com/Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)
### Summary
The **Azure-Samples/azure-search-openai-demo** GitHub repository is a sample application demonstrating the Retrieval-Augmented Generation (RAG) pattern using Azure services. This app integrates Azure AI Search for data retrieval and Azure OpenAI models, specifically designed to create ChatGPT-style and Q&A experiences.

### Key Features:
- **Chat and Q&A interfaces:** Supports multi-turn chats and single-turn Q&A interactions.
- **Citations:** Provides references and thought processes for each answer.
- **Customization:** Includes UI settings to experiment with different behavior.
- **Integration:** Uses Azure AI Search for indexing and retrieval, with support for multiple document formats and vectorization.
- **Optional Features:** Supports GPT-4 (for vision-based reasoning), speech input/output, and automated user login via Microsoft Entra.
- **Performance Monitoring:** Utilizes Application Insights for tracing and monitoring.

### Requirements and Setup:
- **Azure Account:** Necessary for deploying and running this demo.
- **Cost Estimation:** Various Azure resources are required, and costs may vary based on usage.
- **Deployment Options:** Can be set up via GitHub Codespaces, VS Code Dev Containers, or locally.

### Deployment and Running:
1. **Azure CLI Authentication:** Log into your Azure account.
2. **Environment Setup:** Initialize a new environment and deploy the resources with `azd up`.
3. **Local and Remote Running:** Post-deploy, the app can be accessed via a provided URL or run locally.

### Customization and Monitoring:
- **UI and Data Customization:** Modify text, prompts, and integrate your data.
- **Application Insights:** Monitor performance and errors through Azure's Application Insights.

### Cleanup:
- **Resource Deletion:** Use `azd down` to remove all deployed resources when no longer needed.

### Documentation and Resources:
- Detailed documentation, video guides, and additional Azure AI resources are provided for support and further learning.

This sample is a powerful demonstration of integrating Azure AI services to create advanced AI-driven applications, with robust deployment, customization, and monitoring capabilities.
## intelligent-app-workshop
### Description
Immersive workshop showcasing the remarkable potential of integrating SoTA foundation models to enhance product experiences and streamline backend workflows. Leverages Microsoft's Copilot stack, Semantic Kernel and Azure primitives to offer an engaging and comprehensive introduction to AI-infused app development and deployment
### Language
Python
### URL
[https://github.com/Azure/intelligent-app-workshop](https://github.com/Azure/intelligent-app-workshop)
### Summary
The "Azure/intelligent-app-workshop" repository on GitHub provides an immersive workshop to showcase the potential of integrating state-of-the-art (SoTA) foundation models to enhance product experiences and streamline backend workflows. The workshop leverages Microsoft's Copilot stack, Semantic Kernel, and Azure primitives to offer a comprehensive introduction to AI-infused app development and deployment.

Key points about the workshop:
- Rethinks user experience, architecture, and app development using foundation models.
- Utilizes the Miyagi codebase and Semantic Kernel for application development, from identifying user needs to deploying production-grade apps on Azure.
- Encourages signing up for Azure OpenAI (AOAI) and completing the "Getting started with AOAI" module.
- Offers insights into integrating Large Language Models (LLMs) for streamlined development and user experience enhancement.

Additional information:
- The repository includes various files such as .gitignore, CHANGELOG.md, LICENSE.md, README.md, mkdocs.yml, requirements, and setup files.
- It remains a work in progress, with updates available on intelligentapp.dev.
- A detailed disclaimer about the software being provided "as is" for demonstration purposes only and not intended for any commercial use or reliance. 

The repository has 154 stars, 31 forks, and provides resources related to AI, ML, intelligent agents, MLOps, foundation models, LLMs, prompt engineering, and more. The project is licensed under the MIT license.
## openai-chat-app-quickstart
### Description
A simple chat application that uses managed identity for Azure OpenAI access. Designed for deployment on Azure Container Apps with the Azure Developer CLI.
### Language
Bicep
### URL
[https://github.com/Azure-Samples/openai-chat-app-quickstart](https://github.com/Azure-Samples/openai-chat-app-quickstart)
### Summary
### Summary of Azure-Samples/openai-chat-app-quickstart Repository

**Description:** 
This repository hosts a simple chat application developed in Python that uses Azure OpenAI to generate responses. It leverages managed identity for Azure OpenAI access and is meant for deployment using Azure Container Apps and the Azure Developer CLI.

**Key Features:**
1. **Backend:** A Python-based backend using the Quart framework and OpenAI API for message generation.
2. **Frontend:** Basic HTML/JavaScript frontend that streams responses from the backend.
3. **Infrastructure:** Bicep files for provisioning necessary Azure resources such as Azure OpenAI, Azure Container Apps, Container Registry, Log Analytics, and RBAC roles.
4. **Local Development:** Support for using local Language Models during development.

**Setup and Deployment Options:**
- **GitHub Codespaces:** Immediate setup via a web-based VS Code instance.
- **VS Code Dev Containers:** Use of Dev Containers extension in local VS Code.
- **Local Environment:** Detailed instructions for setting up the project locally using tools like Azure Developer CLI, Python 3.10+, Docker Desktop, and Git.

**Deployment Steps:**
1. **Set Up Azure Account:** Create a free Azure account and subscription, request access to Azure OpenAI Service.
2. **Login and Deployment:** Use `azd up` command to provision and deploy the resources.
3. **Continuous Deployment:** GitHub Actions workflow for automatic deployment on every push to the main branch.

**Running the App:**
- The development server can be started on port 50505 with local configurations.

**Cost Considerations:**
- Usage of Azure resources like OpenAI Service, Container Apps, Container Registry, and Log Analytics is cost-based, with specific pricing tiers detailed in the documentation.

**Security Measures:**
- Managed Identity for authentication.
- Recommendations for GitHub secret scanning and additional security measures like firewall or Virtual Network.

**Additional Resources:**
- Similar projects integrating Microsoft Entra Authentication and Azure AI Search.
  
**Repository Stats:**
- **Stars:** 137
- **Forks:** 71
- **Watchers:** 17
- **Languages:** Primarily Bicep, Python, HTML, Dockerfile, Shell, and CSS. 

**License:** MIT License

For more details and specific instructions, please refer to the [repository's README file](https://github.com/Azure-Samples/openai-chat-app-quickstart).
## chat-with-your-data-solution-accelerator
### Description
A Solution Accelerator for the RAG pattern running in Azure, using Azure AI Search for retrieval and Azure OpenAI large language models to power ChatGPT-style and Q&A experiences. This includes most common requirements and best practices.
### Language
Python
### URL
[https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator)
### Summary
### Summary

The repository "Azure-Samples/chat-with-your-data-solution-accelerator" provides a Solution Accelerator for the Retrieval-Augmented Generation (RAG) pattern leveraging Azure's capabilities. It integrates Azure AI Search for data retrieval and Azure OpenAI large language models to create ChatGPT-like and Q&A experiences. This tool incorporates best practices and covers common requirements for such applications.

#### Key Highlights

- **User Story**
  - Designed to create a conversational search experience using an Azure OpenAI GPT model and Azure AI Search index.
  - Offers functionalities like speech-to-text, data upload, and processing.

- **Key Features**
  - Chat with OpenAI models using your own data.
  - Support for uploading and processing various document types.
  - Configurable prompts and multiple chunking strategies.
  - Accessible orchestration via different orchestration choices (e.g., Semantic Kernel, LangChain).

- **When to Use**
  - When out-of-the-box solutions from Azure OpenAI are insufficient and custom configurations are required.
  - For advanced prompt engineering and various ingestion models (Push/Pull).
  - To experiment with and evaluate different RAG configurations before production.

- **Target Users**
  - Suitable for company personnel, including employees and executives, who need quick access to internal unstructured data through a natural language interface.
  - Ideal for tech administrators customizing internal data access.

- **Sample Use Case Scenarios**
  - Financial Advisor preparing for client meetings.
  - Contract Review and Summarization Assistant to manage large document collections.

#### Deployment and Resources

- **Pre-requisites**
  - An Azure subscription with owner access.
  - Approval to use Azure OpenAI services.
  - Optional: Enable custom Teams apps.

- **Products Used**
  - Azure App Service, Application Insights, Bot, Document Intelligence, Function App, Search Service, Storage Account, Speech Service, and optional Teams extension.

- **Deployment Instructions**
  - Offers both one-click deployment via "Deploy to Azure" and local deployment for developers.
  - Includes testing guidance and links to supporting documentation for deployed resources.

#### Licensing and Disclaimers

- Licensed under the MIT License.
- Data set in `/data` folder under CDLA-Permissive-2 License.
- Acknowledges use of third-party components and advises compliance with respective licenses.
- Highlights the software's limitations for high-risk and medical use cases.

#### Contributing and Languages

- Contributions are welcome with 48 contributors listed.
- The primary languages used are Python, Bicep, TypeScript, CSS, Jinja, Shell, and others.

This GitHub repository is a comprehensive resource for developers looking to implement and customize Retrieval-Augmented Generation solutions using Azure technologies.
## miyagi
### Description
Sample to envision intelligent apps with Microsoft's Copilot stack for AI-infused product experiences.
### Language
Jupyter Notebook
### URL
[https://github.com/Azure-Samples/miyagi](https://github.com/Azure-Samples/miyagi)
### Summary
**Project Miyagi Overview:**

**Description:**
Project Miyagi is a sample project developed to showcase Microsoft's Copilot Stack and its potential for creating AI-infused product experiences. It serves as an envisioning workshop designed to help developers design, develop, and deploy intelligent applications using generative and traditional machine learning (ML) technologies.

**Key Features:**
- **Uses Microsoft's AI Tools:** Demonstrates the use of Semantic Kernel, Promptflow, LlamaIndex, LangChain, Azure AI Search, CosmosDB, and other AI tools for creating intelligent applications.
- **Enables Hyper-Personalization:** Offers use cases and techniques for adding AI-driven personalization to applications.
- **Showcases Several ML Use Cases:** Includes examples like generative text and image generation for personalized financial coaching, summarization, and agent-like orchestration.
- **Cloud-Native Architecture:** Built on an event-driven architecture (EDA) backbone to ensure enterprise-grade quality attributes such as availability, scalability, and maintainability.

**Components and Use Cases:**
- **Personalize MVP:** Uses Semantic Kernel for synthesis and chat on Azure Container Apps.
- **RaG Quickstart and Agents:** Different implementations and APIs for agents.
- **Frontend Interaction:** Shows various use cases for interacting with foundation models.
- **Architectural Insights:** Provides detailed architectural designs for intelligent applications leveraging foundational models and prompt engineering strategies.

**Tech Stack:**
- **AI Services:** Azure OpenAI, Semantic Kernel, LangChain, AI Studio, AI Search, and more.
- **Event-Driven Services:** Azure Functions, Service Bus, Event Grid, Logic Apps.
- **Data Services:** Cosmos DB, Azure DB for PostgreSQL, Azure Redis Cache.
- **Other Tools:** Github Actions for CI/CD, Azure Monitor for observability.

**Contribution and Licensing:**
- Welcomes contributions; contributors must sign a Contributor License Agreement (CLA).
- The project follows the Microsoft Open Source Code of Conduct.
- Software provided is for demonstration purposes and comes with no warranties.

**Disclaimer:**
The project is provided "as is" and is not intended for commercial use. It is strictly for demonstration to showcase the potential of integrating AI capabilities using Microsoft's tools. Users assume all risks for using the software.
## qdrant-azure
### Description
Qdrant Vector Database on Azure Cloud
### Language
Shell
### URL
[https://github.com/Azure-Samples/qdrant-azure](https://github.com/Azure-Samples/qdrant-azure)
### Summary
The repository **"qdrant-azure"** on GitHub is an Azure sample project showcasing the deployment of the Qdrant Vector Database on the Microsoft Azure Cloud platform. The project aims to integrate vector search and embedding storage within AI products using Qdrant and Azure.

### Key Sections:
1. **Deployment Options**:
   - **Azure Kubernetes Service (AKS)**: Instructions to deploy Qdrant on AKS, including a "Deploy to Azure" button for quick setup.
   - **Docker**: Instructions for running Qdrant locally with Docker.

2. **Prerequisites**:
   - Requires an Azure subscription.
   - Write access and permission on resource deployments.

3. **Installation Instructions**:
   - For **AKS**: Specify prerequisites like creating a resource group and SSH key.
   - For **Docker (Local)**: Details on setting up a local development environment with Docker and VS Code Dev Container.

4. **Resources**:
   - Links to additional documentation and related Azure services.

5. **Technical Details**:
   - Various deployment files and directories (e.g., `.devcontainer`, `.github`, `Azure-Container-Apps`).
   - The repository emphasizes languages like Shell, Bicep, Python, and Smarty.

### Additional Information:
- **License**: MIT
- **Topics Covered**: Docker, Azure Container Instances, Azure Kubernetes Service, Azure Resource Templates, Qdrant Vector Database.
- **Community and Activities**:
  - Contributors: 9
  - Stars: 85
  - Forks: 22
  - Issues and pull requests are managed actively.

This repository is a valuable resource for developers looking to harness the capabilities of Qdrant within Azure's cloud ecosystem, bridging AI and containerized services.
## contoso-real-estate
### Description
Intelligent enterprise-grade reference architecture for JavaScript, featuring OpenAI integration, Azure Developer CLI template and Playwright tests.
### Language
JavaScript
### URL
[https://github.com/Azure-Samples/contoso-real-estate](https://github.com/Azure-Samples/contoso-real-estate)
### Summary
### GitHub Repository: Azure-Samples/contoso-real-estate

**Description:**  
The repository `contoso-real-estate` by Azure-Samples features an intelligent, enterprise-grade reference architecture for JavaScript. It includes integration with OpenAI, an Azure Developer CLI template, and Playwright tests.

**Key Features:**
- **AI Chatbot Integration:** Incorporates an AI support chatbot using Azure OpenAI.
- **Payments Integration:** Supports payment processing with Stripe.
- **Real-time Notifications:** Enables real-time notifications.
- **Portal Application:** Main entry point showcasing listings, favorites, user authentication, and profile management.
- **Headless CMS and Blog:** Content management using Strapi for a blog and CMS.

**Components:**
1. **Frontend:**
   - Angular
   - Next.js
   - Playwright (for testing)
   - Azure Static Web Apps (for hosting)
2. **Backend:**
   - Strapi (CMS)
   - Stripe (for payment processing)
   - Fastify (API)
   - Azure Functions
   - MongoDB for Azure Cosmos DB
   - Azure Database for PostgreSQL
   - Azure Storage
   - Azure Container Apps
   - Azure Application Insights
3. **DevOps:**
    - Azure CLI
    - GitHub Actions
    - Azure Developer CLI
4. **Developer Tools:**
    - Visual Studio Code
    - GitHub Codespaces
    - Azure Static Web Apps CLI

**Development Environment:**
Optimized for GitHub Codespaces with pre-configured dependencies. Easy setup by forking the repository and creating a new Codespace.

**Deployment to Azure:**
Uses Azure Developer CLI (`azd`) for provisioning, packaging, and deployment. Commands provided to simplify the process. Recommended region for deployment is `westeurope`.

**CI/CD Configuration:**
Instructions for configuring CI/CD pipelines using Azure Developer CLI are included.

**Project Structure:**
- Organized using npm workspaces.
- Contains directories for API, portal, blog, CMS, docs, Stripe webhook, and Playwright tests.

**Developer Guidelines:**
A standalone Developer Guide is included in the `packages/docs` directory, implemented using the Docusaurus platform.

**Contributing:**
Guidelines for contributing are provided, including filing bugs, contributing code, and improving documentation. 

**License:**  
This project is licensed under the MIT license.

For more detailed information, refer to the repository's README file and additional documentation.
## azure-search-openai-demo-csharp
### Description
A sample app for the Retrieval-Augmented Generation pattern running in Azure, using Azure Cognitive Search for retrieval and Azure OpenAI large language models to power ChatGPT-style and Q&A experiences. 
### Language
C#
### URL
[https://github.com/Azure-Samples/azure-search-openai-demo-csharp](https://github.com/Azure-Samples/azure-search-openai-demo-csharp)
### Summary
### Azure Search and OpenAI Demo in C#

This repository contains a sample application demonstrating the Retrieval-Augmented Generation (RAG) pattern using Azure Cognitive Search and Azure OpenAI to enable ChatGPT-like and Q&A functionalities for enterprise data.

#### Key Features
- Voice Chat, Chat, and Q&A functionalities.
- Trustworthy response evaluation with citations and source tracking.
- Advanced options for data preparation and prompt construction.
- Customizable settings for user experience (UX).

#### Application Architecture
- **User Interface**: Blazor WebAssembly application.
- **Backend**: ASP.NET Core Minimal API orchestrating interactions between Azure AI Search for document indexing and Azure OpenAI Service for generating responses.

#### Getting Started
1. **Account Requirements**:
   - Azure Account with access to Azure OpenAI Service and Azure Cognitive Search.
   - Necessary permissions in the Azure subscription.
   
2. **Project Setup**:
   - **GitHub Codespaces** or **VS Code Remote Containers** for setup.
   - **Local Environment** setup requires Azure Developer CLI, .NET 8, Git, Powershell 7+, and Docker.

#### Deployment Options
- **Deploying from scratch**: Provision necessary Azure resources and deploy.
- **Using existing resources**: Configure to use pre-existing Azure services.
- **Re-deploying**: Redeploy a local clone with updated resources.
- **Running locally**: Use Docker and local servers for development and testing.
- **Sharing Environments**: Allow others access to the deployed environment.

#### Optional Features
- Enabling Application Insights for monitoring and diagnostics.
- Enabling authentication through Azure AD.
- Support for GPT-4V for enriched RAG with text and image data.

#### Production Considerations
- Adjusting OpenAI capacity, storage configurations, search service replicas, container app resources, and authentication settings for production.
- Networking setup for deploying within a Virtual Network.

#### Cleanup
- Use `azd down` to clean up resources.

#### Resources
- Detailed guides and resources for further setup and development.

#### FAQ
- Explains the need for document chunking due to token limits and context retention.

#### Contributions
- The project is open to contributions with a diverse group of contributors and is governed under the MIT license. 

This sample application provides a comprehensive starting point for developing intelligent enterprise applications leveraging state-of-the-art AI technologies in Azure.
## openai
### Description
The repository for all Azure OpenAI Samples complementing the OpenAI cookbook. 
### Language
Jupyter Notebook
### URL
[https://github.com/Azure-Samples/openai](https://github.com/Azure-Samples/openai)
### Summary
### Summary of the Azure-Samples/OpenAI GitHub Repository

This repository contains a collection of Azure OpenAI Service samples and resources aimed at helping developers get started with Azure's OpenAI offerings. These samples complement the OpenAI cookbook and cover various use cases such as content generation, summarization, semantic search, and natural language code translation.

#### Key Features:
1. **REST API Access**: Provides access to OpenAI's language models via REST APIs, Python SDK, .NET SDK, or Azure's web-based interface.
2. **Models**: Supports models like GPT-3.5 Turbo, GPT-4, DALL-E, and Whisper.
3. **Sample Categories**:
   - Basic Samples: Small code snippets for specific actions.
   - End-to-End Solutions: Complete solutions with workflows and reference architectures.

#### Prerequisites:
- Azure Account and Subscription with access to Azure OpenAI Service.
- Deployed models on your Azure OpenAI resource.

#### Setup Options:
- **GitHub Codespaces**: For quick setup.
- **Local Setup**: Requires Visual Studio Code, Python (3.8+ and Jupyter Notebook), .NET 8 SDK, and required extensions.

#### Key Concepts:
- **Prompts & Completions**: Core component where an input prompt generates a text completion.
- **Tokens**: Text is processed by breaking it into tokens.
- **In-context Learning**: Models understand tasks based on provided examples in the prompt (Few-shot, One-shot, Zero-shot).

#### Model Families:
1. **GPT-4**: Latest models in preview.
2. **GPT-3**: Includes ChatGPT (in preview).
3. **Codex**: Translates natural language to code.
4. **Embeddings**: Represents semantic meaning of text for machine learning.

#### Responsible AI:
Microsoft emphasizes responsible AI usage, including content filtering and providing AI implementation guidance to onboarded customers.

#### Resources Provided:
- Documentation links for setup, usage, and responsible AI.
- Details on applying for access to Azure OpenAI Service.

#### Additional Information:
- Repository is licensed under MIT License.
- Contains contributions from 22 developers, with code mainly in Jupyter Notebook, Python, and other languages.

Visit [Azure OpenAI Service Documentation](https://aka.ms/azure-openai) for more detailed instructions and information.
## AzureSpeechReactSample
### Description
This sample shows how to integrate the Azure Speech service into a sample React application. This sample shows design pattern examples for authentication token exchange and management, as well as capturing audio from a microphone or file for speech-to-text conversions.
### Language
JavaScript
### URL
[https://github.com/Azure-Samples/AzureSpeechReactSample](https://github.com/Azure-Samples/AzureSpeechReactSample)
### Summary
The repository **Azure-Samples/AzureSpeechReactSample** demonstrates how to integrate Azure's Speech service into a React application. Key features include:

1. **Authentication Token Management**: Example design patterns for securely retrieving and managing authentication tokens.
2. **Audio Capture**: Instructions on capturing audio from a microphone or a file for converting speech-to-text.
3. **Operational Steps**:
   - **Prerequisites**: Requires Azure account with Speech service subscription and Node.js.
   - **Running the Application**: Steps to clone the repository, install dependencies, and run the server and application.
4. **Speech-to-Text Conversion**:
   - **From Microphone**: Code examples to capture and convert speech using the default microphone.
   - **From File**: Methods to select an audio file and convert its content to text.
5. **Token Exchange**: Utilizes an Express server to prevent exposing the Azure speech key by handling token generation and refresh on the backend.

Overall, the repository serves as a comprehensive guide to integrating Azure Speech services within a React application while emphasizing security best practices.
## azure-search-javascript-samples
### Description
Azure Search Javascript sample code
### Language
JavaScript
### URL
[https://github.com/Azure-Samples/azure-search-javascript-samples](https://github.com/Azure-Samples/azure-search-javascript-samples)
### Summary
The `Azure-Samples/azure-search-javascript-samples` repository on GitHub contains JavaScript sample code for Azure AI Search. It provides various examples and guidance on how to use Azure Cognitive Search with JavaScript applications. The primary samples include:

1. **Quickstart**: A Node.js console application demonstrating the fundamental tasks of working with a search index, including creating, loading, and querying data. It uses a subset of the Hotels dataset for simplicity.
2. **Search-website-functions-v4**: A sample application that adds search functionality to a book catalog web app. This sample provides configuration and runtime instructions in its README file.

The repository uses the MIT license, and most of the samples run on the shared (free) pricing tier of Azure AI Search service. The code primarily includes JavaScript, with some HTML, CSS, and Dockerfile.

Summary statistics of the repository:
- **Stars**: 23
- **Forks**: 146
- **Issues**: 0
- **Pull Requests**: 2
- **Releases**: 5

The repo is maintained by multiple contributors and includes a code of conduct.
## azure-search-dotnet-samples
### Description
Azure Search .NET sample code
### Language
C#
### URL
[https://github.com/Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples)
### Summary
### Summary of Azure-Samples/azure-search-dotnet-samples

This GitHub repository, maintained by Azure-Samples, provides C# code samples for Azure AI Search. The samples are primarily designed to help users understand and implement various functionalities of Azure AI Search using .NET. Key highlights include:

- **Types of Samples**: 
  - **quickstart-full-text**: Covers creating, loading, and querying search indexes.
  - **quickstart-semantic-search**: Adds semantic search capabilities.
  - **tutorial-skills-enrichment**: Implements an AI enrichment pipeline using Cognitive Services.
  - **tutorial-create-mvc-app**: Demonstrates search behaviors in an ASP.NET Core MVC application.
  - **tutorial-search-website-functions-v4**: Builds a website for searching through a book catalog using React.

- **Relocated Samples**: Some samples have been moved to new repositories to better align content with specific categories, including tasks like storage usage checks, data export, and optimizing data indexing.

- **Resources**: 
  - Links to other .NET samples for Azure AI Search.
  - Documentation for Azure AI Search.

- **Repository Details**:
  - **License**: MIT
  - **Language Breakdown**: Primarily C#, with some JavaScript, HTML, and CSS.
  - **Contributors**: 15 contributors
  - **Commits and Releases**: 444 commits, 56 releases

The repository aims to facilitate learning and implementation of Azure AI Search through comprehensive examples and structured tutorials.
## Serverless-microservices-reference-architecture
### Description
This reference architecture walks you through the decision-making process involved in designing, developing, and delivering a serverless application using a microservices architecture through hands-on instructions for configuring and deploying all of the architecture's components along the way. The goal is to provide practical hands-on experience in working with several Azure services and the technologies that effectively use them in a cohesive and unified way to build a serverless-based microservices architecture.
### Language
C#
### URL
[https://github.com/Azure-Samples/Serverless-microservices-reference-architecture](https://github.com/Azure-Samples/Serverless-microservices-reference-architecture)
### Summary
The **Azure-Samples/Serverless-microservices-reference-architecture** on GitHub is a practical guide designed to help users design, develop, and deploy serverless applications using a microservices architecture on Azure. The repository aims to provide hands-on experience with several Azure services and technologies. The focus is on a sample application for a fictitious company called Relecloud, which involves a ride-sharing service.

**Key Highlights:**
- **Objective:** Guide users through the decision-making process of creating a serverless microservices application on Azure.
- **Components:** Includes guidelines for configuring and deploying architecture components, using Azure services like Functions, Logic Apps, Event Grid, Cosmos DB, and more.
- **Customer Scenario:** Relecloud is a cloud service-focused organization aiming to explore serverless solutions for their ride-share application.
- **Technological Focus:** Emphasis on serverless components, microservices patterns, API Management, and DevOps for automated integration and deployment.
- **Hands-On Lab:** Provides a step-by-step lab to deploy the sample solution, explaining architectural components and deployment processes.
- **Detailed Documentation:** Comprehensive documentation covering architecture introduction, setup guidelines, API configurations, inter-component communication, data storage, client applications, and monitoring.

The repository is aimed at both beginners and experienced developers looking to explore serverless architectures and microservices on Azure, providing them with a solid foundation and practical insights.
