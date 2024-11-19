FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Update the package manager
RUN apt-get update -y

# Set the working directory
WORKDIR /workspaces

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt || true

# Default command for debugging
CMD ["/bin/bash"]
