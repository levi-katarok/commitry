# Commitry CLI

A command-line tool that uses a local or remote LLM to automatically generate meaningful commit messages from git diffs.

## 🌟 Features

- Optionally can use local LLM (deepseek-r1:7b) through Ollama for privacy and speed. OpenAI models are also supported.
- Generates concise, meaningful commit messages
- Easy to integrate with existing git workflows
- Can set up with no external API dependencies

## 🚀 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- Git
- [Ollama](https://ollama.ai)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/commitry-cli.git
cd commitry-cli
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Install the required Ollama model:
```bash
ollama pull deepseek-r1:7b
```

## 🔧 Configuration

1. Ensure Ollama is running:
```bash
ollama serve
```
2. The tool will automatically connect to Ollama at `http://localhost:11434/v1`

## 💻 Usage
1. Make a change to your codebase
2. Stage your changes with `git add`
3. Run `commitry-cli` to proces the staged changes and generate a commit message (this will run `git diff` and pass the diff to the LLM). You may need to add it to your path. 
4. Commit your changes with the generated message

## 🤝 Contributing

Feedback and contributions are welcome! Please feel free to submit a PR.

## 📜 License

This project is open-sourced under the MIT License - see the LICENSE file for details.