import requests
import os
from dotenv import load_dotenv
load_dotenv()

import markdown2
import re 

from canvasapi import Canvas

import base64


def create_github_repository(repo_name, organization):
    """
    Create a new repository on GitHub.

    Args:
        repo_name (str): The name of the repository.
        description (str): Optional. Description of the repository.
        private (bool): Optional. Specifies if the repository should be private (True) or public (False).

    Returns:
        bool: True if the repository creation was successful, False otherwise.
    """
    url = f'https://api.github.com/orgs/{organization}/repos'  # Use 'users' instead of 'orgs' for user account
    access_token = os.getenv('GITHUB_TOKEN')
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
   }
    payload = {
        'name': repo_name,
        'auto_init': True,
        'initial_commit': {
            'message': 'Initial commit',
            'content': 'This is the initial README file.'  # Custom README content
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print('Repository created successfully!')
    else:
        print('Failed to create repository.')
        print('Response:', response.text)


        
def create_or_update_file(repo_name, organization, file_path, file_content, commit_message):
    """
    Create or update a file in a GitHub repository.

    Args:
        repo_name (str): The name of the repository.
        organization (str): The organization or user account name.
        file_path (str): The path to the file including the file name and extension.
        file_content (str): The content to be written to the file.
        commit_message (str): The commit message for the file operation.
    """
    url = f'https://api.github.com/repos/{organization}/{repo_name}/contents/{file_path}'
    access_token = os.getenv('GITHUB_TOKEN')
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Get the current commit SHA of the file
    response = requests.get(url, headers=headers)
    sha = response.json().get('sha', '')

    # Encode the file content in Base64
    encoded_content = base64.b64encode(file_content.encode()).decode()

    # Prepare the payload for creating/updating the file
    payload = {
        'message': commit_message,
        'content': encoded_content,
        'sha': sha
    }

    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 201 or response.status_code == 200:
        print('File created/updated successfully!')
    else:
        print('Failed to create/update file.')
        print('Response:', response.text)
