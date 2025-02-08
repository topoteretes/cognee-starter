
# Cognee starter repo

## Install dependencies
```
uv sync
```

## Setup LLM
Add environment variables to `.env` file.
In case you choose to use OpenAI provider, add just the model and api_key.
```
LLM_PROVIDER=""
LLM_MODEL=""
LLM_ENDPOINT=""
LLM_API_KEY=""
LLM_API_VERSION=""

EMBEDDING_PROVIDER=""
EMBEDDING_MODEL=""
EMBEDDING_ENDPOINT=""
EMBEDDING_API_KEY=""
EMBEDDING_API_VERSION=""
```

## Run
Activate the Python environment:
```
source .venv/bin/activate
```

Run the code:
```
python src/pipelines/default.py
```

### Graph preview with Graphistry
In order to use Graphistry, create an account and API key.
Add environment variables to `.env` file:
```
GRAPHISTRY_USERNAME=""
GRAPHISTRY_PASSWORD=""
```
Note: `GRAPHISTRY_PASSWORD` is API key.