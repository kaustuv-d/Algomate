# Algomate
## Overview

Algomate is a powerful virtual coding assistant that supports queries and doubts in multiple programming languages. It is built by fine-tuning the LLM, CodeLlama, under the LlamA 2.0 llm framework. Algomate is deployed on a local host using HTML, CSS, and Django.

## Key Features:

- Supports multiple programming languages like C/C++, Python, Java, JavaScript etc,.
- Provides instant coding assistance and answers to queries.
- Built by fine-tuning the LLM- codellama, over Llama 2.
- Deployed on a local host with a user-friendly UI using Django.

## Technologies Used

- **Large Language Model**: codellama (fine-tuned over LLaMA 2.0)
- **Backend**: Django (python)
- **Frontend**: HTML, CSS

## Model library

Ollama supports a list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library')
| Model              | Parameters | Size  | Download                       |
| ------------------ | ---------- | ----- | ------------------------------ |
| Code Llama         | 7B         | 3.8GB | `ollama run codellama`         |

### Database
- [MindsDB](https://github.com/mindsdb/mindsdb/blob/staging/mindsdb/integrations/handlers/ollama_handler/README.md) (Connects Ollama models with nearly 200 data platforms and apps)
- [chromem-go](https://github.com/philippgille/chromem-go/blob/v0.5.0/embed_ollama.go) with [example](https://github.com/philippgille/chromem-go/tree/v0.5.0/examples/rag-wikipedia-ollama)

