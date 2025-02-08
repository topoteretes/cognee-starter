
# Cognee Starter Kit
Welcome to the cognee Starter Repo! This repository is designed to help you get started quickly by providing a structured dataset and pre-built data pipelines using cognee to build powerful knowledge graphs.

You can use this repo to ingest, process, and visualize data in minutes. 

By following this guide, you will:

- Load structured company and employee data
- Utilize pre-built pipelines for data processing
- Perform graph-based search and query operations
- Visualize entity relationships effortlessly on a graph

# How to Use This Repo 🛠
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

Activate the Python environment:
```
source .venv/bin/activate
```

## Run the Default Pipeline

This script will ingest text data, build a knowledge graph, and allow you to run search queries.

```
python src/pipelines/default.py
```

## Run the Low-Level Pipeline

This script processes the given JSON data about companies and employees, making it searchable via a graph.

```
python src/pipelines/low_level.py
```

## Run the Custom Model Pipeline

This script categorizes programming languages as an example and visualizes relationships.

```
python src/pipelines/custom-model.py
```

## Graph preview with Graphistry (Optional)
In order to use Graphistry for graph visualization:
- create an account and API key from https://www.graphistry.com
- add the following environment variables to `.env` file:
```
GRAPHISTRY_USERNAME=""
GRAPHISTRY_PASSWORD=""
```
Note: `GRAPHISTRY_PASSWORD` is API key.


# What will you build with cognee?

- Expand the dataset by adding more structured/unstructured data
- Customize the data model to fit your use case
- Use the search API to build an intelligent assistant
- Visualize knowledge graphs for better insights