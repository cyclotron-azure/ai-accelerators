import csv
import os
import requests
from bs4 import BeautifulSoup
from openai import AzureOpenAI

def load_repos(file_path):
    repos = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            repos.append(row)
    return repos

def download_and_strip_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def submit_to_azure_openai(text):
    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_API_BASE"),
        api_key=os.getenv("AZURE_API_KEY"),
        api_version=os.getenv("AZURE_API_VERSION")
    )

    system_prompt = """
        **Summarize: Extract Key Information from GitHub Repos**

        Take the context and extract the following key information:

        1. **Case Scenario:** Identify the primary use case or scenario for which this project is intended, e.g., "Use Case 1: [briefly describe the use case]."
        DO NOT GENERATE MARKDOWN
        
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": text
            }
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

def readme_repo_exists(repo_name, output_file='README.md'):
    if not os.path.exists(output_file):
        return False
    with open(output_file, 'r') as file:
        for line in file:
            if repo_name in line:
                return True
    return False

def generate_readme_file(repos, output_file='README.md'):
    if not os.path.exists(output_file):
        with open(output_file, 'w') as file:
            file.write("# AI Accelerators Repositories\n\n")
            file.write("This repository contains a list of AI accelerators repositories.\n\n")
            file.write("| Name | URL | Description | Language | Summary |\n")
            file.write("|------|-----|-------------|----------|---------|\n")

    with open(output_file, 'a') as file:
        for repo in repos:
            if not readme_repo_exists(repo['name'], output_file):
                stripped_text = download_and_strip_html(repo['html_url'])
                ai_summary = submit_to_azure_openai(stripped_text)

                file.write(f"| {repo['name']} | [{repo['html_url']}]({repo['html_url']}) | {repo['description']}| {repo['language']} | {ai_summary} |\n")

def repo_exists(repo_name, output_file='REPOS.md'):
    if not os.path.exists(output_file):
        return False
    with open(output_file, 'r') as file:
        for line in file:
            if repo_name in line:
                return True
    return False

def generate_repos(repos, output_file='REPOS.md'):
    if not os.path.exists(output_file):
        with open(output_file, 'w') as file:
            file.write("# AI Accelerators Repositories\n\n")
            file.write("This repository contains a list of AI accelerators repositories.\n\n")
            file.write("| Name | URL | Description | Language |\n")
            file.write("|------|-----|-------------|----------|\n")
    with open(output_file, 'a') as file:
        for repo in repos:
            if not repo_exists(repo['name'], output_file):
                file.write(f"| {repo['name']} | [{repo['html_url']}]({repo['html_url']}) | {repo['description']}| {repo['language']} |\n")

if __name__ == "__main__":
    file_path = 'data/repos.csv'
    repos = load_repos(file_path)
    # generate_repos(repos)
    generate_readme_file(repos)

