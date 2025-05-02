
# Bias Benchmarking in Large Language Models (Master's Thesis)

This repository contains the full pipeline for benchmarking social biases in large language models (LLMs), developed as part of a master's thesis in Information Science at the University of Bergen.

The study focuses on bias related to **age**, **disability**, and **nationality**, and evaluates how different models respond to structured prompts. Models include both Norwegian-specific and multilingual LLMs.

---

## 🧠 Models Evaluated

- **GPT-4** (via API from Groq)
- **Llama3** (run locally via Ollama)
- **Norwegian / Multilingual Models** from Hugging Face:
  - `NorBERT3-large`
  - `NorMistral`
  - `NorwAI-LLaMA2`
  - `nb-BERT`

---

## 🗂️ Repository Overview

| Folder/File            | Description |
|------------------------|-------------|
| `api/`                 | Scripts for interacting with remote models (e.g., GPT-4) |
| `llama3.py`            | Script to run Llama3 locally via Ollama |
| `reports/`, `outputs/` | Model outputs and generated evaluations |
| `x5_iterations/`       | Multiple-run analyses (e.g., GPT-4, Llama3) |
| `generate_reports.py`  | Generate final analysis and figures |
| `main.py`              | Main entry point for evaluating a model |
| `*_bert.py`            | Evaluation scripts for each model |
| `input_attributes/`    | Bias dimensions and prompt structure |
| `requirements.txt`     | Python dependencies |
| `statistics.ipynb`     | Statistical analysis (e.g., Kendall’s tau) |
| `eksampler.txt`        | Prompt examples |
| `README.md`            | You're reading it! |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/martinsjaavik/bias-benchmark-thesis.git
cd bias-benchmark-thesis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Benchmark

There are three execution methods depending on the model.

### ▶️ GPT-4 (Remote via Groq API)

1. Get an API key from [GROQ](https://console.groq.com)
2. Export credentials:

```bash
export GROQ_API_KEY=your_api_key_here
export MODEL=groq/llama2-70b-4096
```

3. Run:

```bash
python main.py --model remote
```

---

### ▶️ Llama3 (Local via Ollama)

1. [Install Ollama](https://ollama.ai)
2. Start model:

```bash
ollama run llama3
```

3. Run benchmark:

```bash
python main.py --model llama3
```

---

### ▶️ Norwegian and Hugging Face Models

These models are downloaded and run locally through scripts like `norbert.py`, `nb-bert.py`, etc.

Example:

```bash
python main.py --model norbert3
```

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
