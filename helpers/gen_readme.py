import os
def create_readme(project_path, project_name):
    """Creates a README.md file with the specified content."""
    readme_path = os.path.join(project_path, "README.md")
    with open(readme_path, "w") as readme:
        readme.write(f"# {project_name}\n\n")
        readme.write("## Overview\n")
        readme.write("Provide an overview of your project here.\n\n")
        readme.write("## Instructions to Run\n")
        readme.write("1. Navigate to the project directory.\n")
        readme.write("2. Run the following commands from the base folder of the project:\n")
        readme.write("   ```bash\n")
        readme.write("   scripts/setup.sh\n")
        readme.write("   scripts/run.sh\n")
        readme.write("   ```\n\n")
        readme.write("## Running Code Inside the Docker Container\n")
        readme.write("After running the container, you can execute your code inside it with:\n")
        readme.write("```bash\n")
        readme.write("python3 main.py\n")
        readme.write("```\n")