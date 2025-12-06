# Makefile
.PHONY: run decode-logo docker-build docker-up docker-down format install

install:
	poetry install

run:
	poetry run python -m app.app

decode-logo:
	@if [ -f static/logo.png.base64 ] && [ ! -f static/logo.png ]; then \
		python3 -c "import base64; data = open('static/logo.png.base64').read().strip(); open('static/logo.png', 'wb').write(base64.b64decode(data))"; \
		echo "Logo decoded successfully"; \
	else \
		echo "Logo already exists or base64 file not found"; \
	fi

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

format:
	@echo "Formatting code with black..."
	@poetry run black app/ || echo "black not available. Run: poetry install"

