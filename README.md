
# Bias Benchmarking in Large Language Models (Master's Thesis)

This repository contains the full pipeline for benchmarking social biases in large language models, developed as part of my master's thesis in Information Science at the University of Bergen.

The thesis focuses on bias related to **age**, **disability**, and **nationality**, and evaluates how different models respond to structured prompts. Models include both Norwegian-specific and multilingual LLMs.

---

## 🧠 Models Evaluated

- **GPT-4** (via API)
- **Llama3** (run locally via Ollama)
- **Norwegian Models** from Hugging Face:
  - `NorBERT3-large`
  - `NorMistral`
  - `NorwAI-Llama2`
  - `nb-BERT`

---

## 🗂️ Repository Overview

| Folder/File            | Description |
|------------------------|-------------|
| `api/`                 | Scripts for interacting with local and remote models|
| `data/`                 | All datasets |
| `reports/`, `outputs/` | Model outputs and generated evaluations |
| `x5_iterations/`       | Multiple-run analyses (e.g., GPT-4, Llama3) |
| `generate_reports.py`  | Generate final analysis and figures |
| `<model_name>.py`      | Scripts to run each model |
| `input_attributes/`    | Bias dimensions and prompt structure |
| `requirements.txt`     | Python dependencies |
| `statistics.ipynb`     | Dataset statistics|
| `README.md`            | You're reading it! |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/martinsjaavik/llm-bias-norwegian.git
cd llm-bias-norwegian
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Benchmark

There are three execution methods depending on the model.

### ▶️ GPT-4 (Remote via OpenAI API)

1. Get an API key from [OpenAI]
2. Export credentials:

```bash
export OPENAI_API_KEY=your_api_key_here
export MODEL=openai/gpt-4
```

3. Run:

```bash
python gpt4.py --model remote
```

---

### ▶️ Llama3 (Local via Ollama)

1. [Install Ollama](https://ollama.ai)
2. Start model:

```bash
ollama run llama3
export MODEL=llama3
```

3. Run benchmark:

```bash
python llama3.py --model local
```

---

### ▶️ Norwegian and Hugging Face Models

These models are downloaded and run locally through scripts like `norbert.py`, `nb-bert.py`, etc.

Simply run the scripts

---

## 📊 Output

Reports and model outputs are saved in:

- `outputs/` – raw generations
- `reports/` – final bias reports
- `x5_iterations/` – repeated run summaries (x5)

---

## 📚 Citation

If you use this benchmark or code in your work, please cite this repository or the thesis (to be published at UiB).

---

## 👤 Author

**Martin Sjåvik**  
Master’s student in Information Science  
University of Bergen, 2025

---

## 📃 License

MIT License
