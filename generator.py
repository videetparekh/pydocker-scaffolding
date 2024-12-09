import os
import re
import shutil
from helpers.gen_docker import create_dockerfile
from helpers.gen_scripts import create_setup_script, create_run_script, create_env_file
from helpers.gen_pyenv import create_requirements_file, create_app_main
from helpers.gen_readme import create_readme
from helpers.gitify import init_git_repo, create_gitignore

def validate_project_name(name):
    """Validates the project name to ensure it matches GitHub repo name rules."""
    pattern = r'^[a-zA-Z0-9_\-]+$'
    if not re.match(pattern, name):
        raise ValueError("Project name can only contain letters, numbers, underscores, and hyphens.")

def get_project_path(project_name):
    """Returns the full path to the project directory in the parent folder of this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    return os.path.join(parent_dir, project_name)

def create_folder_structure(project_path):
    """Creates the folder structure for the new project."""
    os.makedirs(f"{project_path}/docker", exist_ok=True)
    os.makedirs(f"{project_path}/scripts", exist_ok=True)
    os.makedirs(f"{project_path}/app", exist_ok=True)
    os.makedirs(f"{project_path}/assets", exist_ok=True)

def copy_assets(project_name):
    """Copies assets to the new project folder."""
    source_assets = "assets"
    dest_assets = os.path.join(project_name, "assets")
    if os.path.exists(source_assets):
        shutil.copytree(source_assets, dest_assets, dirs_exist_ok=True)

def main():
    # Step 1: Get the project name
    project_name = input("Enter project name (letters, numbers, underscores, hyphens only): ").strip()
    try:
        validate_project_name(project_name)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Step 2: Get the base Docker image
    base_image = input("Enter base Docker image (default: python:3.10): ").strip() or "python:3.10"

    # Step 3: Get the build arguments
    build_args = []
    print("Enter build arguments (one per line). Leave blank to finish: ")
    while True:
        arg_ = input("> ").strip()
        if not arg_:
            break
        build_args.append(arg_)
    
    project_path = get_project_path(project_name)
    # Create the project structure and files
    create_folder_structure(project_path)
    create_dockerfile(project_path, base_image, build_args)
    create_env_file(project_path, build_args)
    create_setup_script(project_path, build_args)
    create_run_script(project_path)
    create_requirements_file(project_path)
    create_app_main(project_path)
    create_readme(project_path, project_name)
    copy_assets(project_path)
    init_git_repo(project_path)
    create_gitignore(project_path)

    print(f"Project {project_name} initialized successfully!")

if __name__ == "__main__":
    main()