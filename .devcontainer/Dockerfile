FROM mcr.microsoft.com/devcontainers/python:3.12

# Install build-essential for potential binary package builds
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git curl build-essential

# Set workspace owner to vscode (standard for python devcontainers)
USER vscode
