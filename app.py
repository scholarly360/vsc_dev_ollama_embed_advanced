from flask import Flask, request, jsonify 
import ollama
from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__) 
# Entry endpoint 

import subprocess
def is_command_running(command_name):
    """
    Check if a command is running by using pgrep.
    Returns True if running, else False.
    """
    try:
        subprocess.run(
            ["pgrep", "-f", command_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def run_command_in_background(command):
    """
    Runs a command in the background.
    """
    subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# Command to check/run
command_name = "ollama list"
full_command = f"ollama serve"
if is_command_running(command_name):
    print(f"'{command_name}' is already running.")
else:
    print(f"'{command_name}' is not running. Starting it in the background...")
    run_command_in_background(full_command)

@app.route('/') 
def entry(): 
    return jsonify({'message': 'Healthy!'})
## Embed endpoint 
@app.route('/embed', methods=["POST"]) 
def embed(): 
    if is_command_running(command_name):
        pass
    else:
        run_command_in_background(full_command)
    data = request.json 
    text = data.get('text', '') 
    model_name = data.get('model', 'nomic-embed-text')
    response = ollama.embeddings(model=model_name, prompt=text)
    return jsonify(response.embedding) 
## Embed endpoint 
@app.route('/llm', methods=["POST"]) 
def llm(): 
    if is_command_running(command_name):
        pass
    else:
        run_command_in_background(full_command)
    data = request.json 
    messages = data.get('messages') 
    from pprint import pprint
    is_debug= False
    if(is_debug):
        pprint(messages)
    model_name = data.get('model_name', 'qwen2:1.5b')
    response: ChatResponse = chat(model=model_name, messages=messages)
    final_response = response['message']['content']
    return jsonify(final_response) 

if __name__ == '__main__': 
    app.run()