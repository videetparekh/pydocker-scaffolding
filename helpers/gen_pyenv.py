import os

def create_requirements_file(project_path):
    """Creates a requirements.txt file in the project folder."""
    requirements_path = os.path.join(project_path, "requirements.txt")
    print("Enter the required Python packages for your project (one per line). Leave blank to finish:")
    requirements = []
    while True:
        package = input("> ").strip()
        if not package:
            break
        requirements.append(package)
    with open(requirements_path, "w") as req_file:
        req_file.write("\n".join(requirements))
    print(f"requirements.txt created with {len(requirements)} package(s).")

def create_app_main(project_path):
    """Creates a basic main.py file in the app folder."""
    app_main_path = os.path.join(project_path, "app", "main.py")
    with open(app_main_path, "w") as main_file:
        main_file.write("""\ndef hello_world():\n    print("Hello, World!")\n\nif __name__=="__main__":\n    hello_world()\n""")
