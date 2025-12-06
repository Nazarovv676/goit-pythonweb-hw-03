# Makefile
.PHONY: run docker-build docker-up docker-down format install

install:
	poetry install

run:
	poetry run python -m app.app

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

format:
	@echo "Formatting code with black..."
	@poetry run black app/ || echo "black not available. Run: poetry install"

