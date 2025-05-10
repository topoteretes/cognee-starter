.PHONY: setup test run-default run-low-level run-custom test-all

setup:
	pip install uv
	uv sync
	@echo "Setup complete. Remember to set your environment variables in .env"

run-default:
	source .venv/bin/activate && python src/pipelines/default.py

run-low-level:
	source .venv/bin/activate && python src/pipelines/low_level.py

run-custom:
	source .venv/bin/activate && python src/pipelines/custom-model.py

test:
	source .venv/bin/activate && python -m unittest src/tests/test_pipelines.py

test-all: run-default run-low-level run-custom test

clean:
	rm -rf .artifacts
	rm -rf .cognee 