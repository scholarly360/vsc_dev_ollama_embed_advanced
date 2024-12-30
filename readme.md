
## BUILD IMAGE FOR DOCKER

docker build -t my-ollama-embed-adv . 

docker run -p 5000:5000 my-ollama-embed-adv


export OLLAMA_MODELS=ollama_models_local

## BULD LOCAL

python app.py
OR
gunicorn app:app
but before start ollma using 
>> ollama serve
or check 
>> ollama list


curl localhost:5000
curl http://127.0.0.1:5000

curl -X POST http://127.0.0.1:5000/embed -H "Content-Type: application/json" -d '{"text": "Your input text here"}'

EXAMPLE OF DOC TYPE

curl -X POST http://127.0.0.1:5000/llm -H "Content-Type: application/json" -d '{"messages":[{"role": "system","content": "You are a text classifier. classify into two categories 'contract' or 'non-contract' by reading the content."},{"role": "user","content": "This Request for proposal is asking about construction"}]}'

EXAMPLE OF INDUSTRY

curl -X POST http://127.0.0.1:5000/llm -H "Content-Type: application/json" -d '{"messages":[{"role": "system","content": "You are a text classifier. return list of industries separated by comma while reading the content."},{"role": "user","content": "This Request for proposal is asking about construction and cement"}]}'

SUMMARY

curl -X POST http://127.0.0.1:5000/llm -H "Content-Type: application/json" -d '{"messages":[{"role": "system","content": "You are a text summarizer. Summarize the content."},{"role": "user","content": "The Offer is the key element that defines the relevant issues in the contract. To be a legally valid offer, the offer must be effectively communicated so that the receiving party has the ability to accept or reject the offer. Whether or not the receiving party reads the contract has no bearing in determining the clarity of the offer. The offer must only provide the recipient with a clear opportunity to accept or reject the contract. Someone who signs a contract without reading it does so at his/her own risk.

In addition, a valid offer must contain certain and definite terms. For the terms to be considered definite, a reasonable person must be capable of readily understanding the terms. For example, in determining whether the terms of a procurement contract are definite, courts will often review the clarity within four primary elements:"}]}'