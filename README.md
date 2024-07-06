# Algomate
## Overview

Algomate is a powerful virtual coding assistant that supports queries and doubts in multiple programming languages. It is built by fine-tuning the LLM, CodeLlama, under the LlamA 2.0 llm framework. Algomate is deployed on a local host using HTML, CSS, and Django.




## Key Features:

- Supports multiple programming languages like C/C++, Python, Java, JavaScript etc,.
- Provides instant coding assistance and answers to queries.
- Built by fine-tuning the LLM- codellama, over Llama 2.
- Deployed on a local host with a user-friendly UI using Django.

## Techstack Used:

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

### Algomate UI
![Algomate SS](https://github.com/kaustuv-d/Algomate/blob/main/Algomate_working01.png)


### Steps in Detail

1. **Download Ollama:**
   - Go to [Ollama's website](https://ollama.ai).
   - Follow the instructions to download the necessary files for your operating system.

2. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Run the following command to clone the repository:
     ```bash
     git clone https://github.com/yourusername/algomate.git
     cd algomate
     ```

3. **Create and Activate a Virtual Environment:**
   - Run the following commands to create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
     ```

4. **Install the Dependencies:**
   - Install the required Python packages using pip:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Server:**
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```

6. **Access the Application:**
   - Open your web browser and navigate to `http://localhost:8000` to use Algomate.

Following these instructions, you can set up and run the Algomate app on your local machine.


## Creators:
- Kaustuv Devmishra (Mechanical Engineering Dept., IIT Indore)
