FROM ubuntu:22.04

# Feel free to add other dependencies or packages
# however, `socat` MUST be installed for the server to work
RUN apt-get update -y && apt-get install -y \
    python3 python3-dev socat curl wget

# Use uv instead of pip
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app
ADD . /app

# You can add more uv packages here or in the pyproject.toml file
RUN uv add mcp && uv sync


