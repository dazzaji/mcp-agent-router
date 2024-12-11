FROM ubuntu:22.04

# Feel free to add other dependencies or packages
# however, `socat` MUST be installed for the server to work
RUN apt-get update -y && apt-get install -y \
    python3 python3-dev socat curl wget python3-pip

RUN pip install flask anthropic requests python-dotenv

WORKDIR /app
ADD . /app

CMD ["python3", "/app/server.py"]

