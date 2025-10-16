# Repository Guidelines

## Project Structure & Module Organization
AppAgentX keeps orchestration scripts at the repository root (`chain_evolve.py`, `chain_understand.py`, `explor_auto.py`, `explor_human.py`). Persistence adapters live in `data/`, while perception utilities are in `tool/`. Visual references sit in `assets/`, and Dockerized FastAPI services for parsing run from `backend/` (`ImageEmbedding/`, `OmniParser/`).

## Build, Test, and Development Commands
Install dependencies with `pip install -r requirements.txt`. `python demo.py` launches the Gradio UI for a connected ADB device or emulator, and `python chain_evolve.py` rebuilds high-level action templates. From `backend/`, run `docker-compose up --build` to start OCR/embedding services and `docker-compose down` once finished. Maintain `.env` values that mirror keys consumed in `config.py`.

## Coding Style & Naming Conventions
Use four-space indentation, type hints, and docstrings as shown in `utils.py`. Prefer `snake_case` for functions and variables, `PascalCase` for classes, uppercase constants for defaults, and f-strings for interpolation. Group prompt templates in triple-quoted strings and keep configuration overrides in environment variables loaded via `python-dotenv`.

## Testing Guidelines
Automated coverage is not yet tracked, so smoke-test new work by running `python demo.py` and the explorer scripts that touch your changes. When adding modules, place integration-style checks under a new `tests/` package and run them with `pytest` (`pip install pytest`) before submitting. Capture device setup details or manual verification steps in the PR notes.

## Commit & Pull Request Guidelines
Recent commits show short imperatives (for example, `Update README.md`); tighten consistency by using `<type>: <summary>` such as `feat: add Pinecone reset helper`. Reference touched modules in the commit body and link related issues. PRs should include a problem statement, configuration or model updates, UI screenshots where relevant, and confirmation that local scripts or containers were exercised. Request reviews from maintainers closest to the changed area and wait for approval before merge.

## Security & Configuration Tips
Keep API keys for OpenAI, DeepSeek, Neo4j, and Pinecone in environment variables consumed by `config.py`; never commit credentials. Confirm GPU access with `nvidia-smi` prior to `docker-compose up` when you expect accelerated inference. Store screenshots or logs under `assets/` or `data/` only after removing user identifiers, and clear Neo4j/Pinecone state with helpers in `utils.py` after experiments.
