#curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.3.13 sh
##curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
file=ollama-linux-amd64.tgz
if [ ! -e "$file" ]; then
    echo "File does not exist"
    curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
else 
    echo "File exists"
fi 
sudo tar -C /usr -xzf ollama-linux-amd64.tgz
nohup ollama serve > /dev/null 2>&1 & sleep 10 && ollama pull nomic-embed-text && ollama pull qwen2:1.5b
# nohup ollama serve &
# sleep 5
# ollama pull all-minilm
sudo apt install procps -y && pip install --no-cache-dir -r req.txt