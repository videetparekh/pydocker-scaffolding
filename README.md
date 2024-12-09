# PyDocker Scaffolding

A Python-based tool to generate a starter folder structure for new projects. This script helps you quickly set up a boilerplate with Docker support, scripts, and a basic Python application to get started immediately.

## Features

- Generates a structured project directory in the parent folder of the tool.
- Creates a customizable Dockerfile.
- Adds `setup.sh` and `run.sh` scripts for building and running the Docker container.
- Initializes a Python `main.py` file with a "Hello, World!" example.
- Generates a `requirements.txt` for specifying Python dependencies.
- Generates a template asset folder with a single default asset.
- Creates a `README.md` with placeholders for project details and instructions.

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script using Python:

```bash
python3 generator.py
```

### Script Prompts

1. **Project Name**: Enter the name of your project. It should only include letters, numbers, underscores, and hyphens.
2. **Base Docker Image**: Specify the base image for Docker (e.g., `python:3.9`). Defaults to `python:3.9`.
3. **Build Arguments**: List any build arguments required for Docker. Leave blank to finish.
4. **Python Requirements**: Provide the Python packages your project needs (e.g., `flask`, `numpy`). Leave blank to finish.

## Output Structure

The script generates the following structure in the parent folder:

```
<project_name>/
├── README.md
├── requirements.txt
├── docker/
│   └── Dockerfile
├── scripts/
│   ├── setup.sh
│   └── run.sh
├── app/
│   └── main.py
└── assets/
    └── images/
```

### Key Files

- **README.md**: Placeholder for project details.
- **requirements.txt**: Python dependencies.
- **Dockerfile**: Pre-configured for Python projects with dependency installation.
- **setup.sh**: Script to build the Docker image.
- **run.sh**: Script to run the Docker container.
- **main.py**: Entry point for your Python application.

## Example Workflow

1. Run the generator script:

   ```bash
   python3 generator.py
   ```

2. Navigate to the generated project folder:

   ```bash
   cd <project_name>
   ```

3. Build the Docker image:

   ```bash
   scripts/setup.sh
   ```

4. Run the Docker container:

   ```bash
   scripts/run.sh
   ```

5. Inside the container, run the Python application:

   ```bash
   python3 main.py
   ```

## Contributing

Feel free to fork the repository and contribute improvements. Open a pull request for review.

## License

This tool is provided under the [MIT License](LICENSE).
