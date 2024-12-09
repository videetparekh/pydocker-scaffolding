import subprocess
import os
import shutil

def init_git_repo(project_path):
    """Initializes a Git repository in the specified folder."""
    try:
        subprocess.run(["git", "init"], cwd=project_path, check=True)
        print("Git repository initialized successfully in:", project_path)
    except subprocess.CalledProcessError as e:
        print("Error initializing Git repository:", e)
        
def create_gitignore(project_path):
    """Creates a default .gitignore for python projects"""
    source_path = "defaults/gitignore"
    dest_path = os.path.join(project_path, ".gitignore")
    if os.path.exists(source_path):
        shutil.copy(source_path, dest_path)
        