import os

def create_dockerfile(project_path, base_image, build_args):
    """Creates a Dockerfile with the specified base image and build args."""
    dockerfile_path = os.path.join(project_path, "docker", "Dockerfile")
    with open(dockerfile_path, "w") as dockerfile:
        dockerfile.write(f"FROM {base_image}\n")
        for arg in build_args:
            dockerfile.write(f"ARG {arg}\n")
        dockerfile.write("ENV PYTHONUNBUFFERED=1\n")
        dockerfile.write("RUN apt-get update && apt-get install -y --no-install-recommends \\\n")
        dockerfile.write("    python3-pip \\\n")
        dockerfile.write("    && rm -rf /var/lib/apt/lists/*\n")
        dockerfile.write("WORKDIR /app\n")
        dockerfile.write("COPY requirements.txt /app/\n")
        dockerfile.write("RUN pip install --no-cache-dir -r requirements.txt\n")