# Contributing to VentureVal 🚀

First off, thank you for considering contributing to VentureVal! It's people like you that make open-source such a great community. 

This document provides guidelines and instructions for contributing to this repository.

## 🛠 Development Setup

We use modern Python tooling. You will need [uv](https://docs.astral.sh/uv/) installed on your system to manage dependencies.

### 1. Fork & Clone
Fork the repository to your GitHub account, then clone it locally:
```bash
git clone https://github.com/keshavagarwal321/VentureVal.git
cd VentureVal
```

### 2. Install Dependencies
Run the following command to create a virtual environment and install all required packages:
```bash
uv sync
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```ini
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the App
To start the Streamlit server locally:
```bash
uv run streamlit run app.py
```

## 🧑‍💻 Coding Standards

To maintain a clean and professional codebase, we enforce strict formatting and linting. 

Before committing your code, you **must** run `ruff` to format and check for errors:
```bash
# Format the code
uv run ruff format .

# Check and fix linting errors
uv run ruff check . --fix
```

## 📝 Commit Message Convention

We follow **Conventional Commits**. Please format your commit messages accordingly:
* `feat: add new data visualization chart`
* `fix: resolve API timeout issue`
* `docs: update setup instructions in README`
* `style: run ruff formatter`

## 🚀 Pull Request Process

1. Create a new branch for your feature: `git checkout -b feat/your-feature-name`
2. Write your code and ensure it passes all `ruff` checks.
3. Commit using conventional commit messages.
4. Push to your fork and submit a Pull Request to our `main` branch.
5. Wait for the maintainer to review and merge!