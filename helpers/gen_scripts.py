import os

def create_env_file(project_path, build_args):
    """Creates a .env file with blank values for the build arguments."""
    env_path = os.path.join(project_path, ".env")
    with open(env_path, "w") as env_file:
        for arg in build_args:
            env_file.write(f"{arg}=\"\"\n")
    print(f".env file created with {len(build_args)} argument(s).")

def create_setup_script(project_path, build_args):
    """Creates a setup script that builds the Docker image."""
    setup_path = os.path.join(project_path, "scripts", "setup.sh")
    with open(setup_path, "w") as setup_script:
        setup_script.write("#!/bin/bash\n\n")
        setup_script.write("set -a && source .env && set +a\n\n")
        setup_script.write(f"docker build \\\n")
        for arg in build_args:
            setup_script.write(f"    --build-arg {arg}=${{{arg}}} \\\n")
        setup_script.write(f"    -t {os.path.basename(project_path)}_image:latest \\\n")
        setup_script.write("    -f docker/Dockerfile .\n")
    os.chmod(setup_path, 0o755)

def create_run_script(project_path):
    """Creates a run script that starts a Docker container."""
    run_path = os.path.join(project_path, "scripts", "run.sh")
    with open(run_path, "w") as run_script:
        run_script.write("#!/bin/bash\n")
        run_script.write(f"docker run \\\n")
        run_script.write(f"    -v $(pwd)/app:/app \\\n")
        run_script.write(f"    -w /app \\\n")
        run_script.write(f"    --rm {os.path.basename(project_path)}_image:latest\n")
    os.chmod(run_path, 0o755)
