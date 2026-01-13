FROM mcr.microsoft.com/devcontainers/javascript-node:20

# Install additional OS packages if needed
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git curl

# Set workspace owner
USER node
