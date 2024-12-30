# Use an official Python runtime as a parent image 
FROM python:3.12-slim 
# Set the working directory in the container 
WORKDIR /app 
COPY . /app 
ENV PYTHONDONTWRITEBYTECODE=1 PIP_NO_CACHE_DIR=1 OLLAMA_MODELS="/app/ollama_models_local" OLLAMA_ORIGINS="*"
#### IMP :: DOWNLOAD ollama-linux-amd64.tgz using install-dependencies.sh or UNCOMMENT
# RUN curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
RUN tar -C /usr -xzf ollama-linux-amd64.tgz && apt update && apt install procps -y && pip install --no-compile --no-cache-dir -r req.txt && rm -rf /var/lib/apt/lists/*
RUN nohup ollama serve > /dev/null 2>&1 & sleep 10 && ollama pull nomic-embed-text && ollama pull qwen2:1.5b
# Make port 5000 available to the world outside this container 
EXPOSE 5000
ENTRYPOINT ["gunicorn", "app:app"]