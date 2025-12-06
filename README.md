# Flask Message App

A simple Flask web application for sending and reading messages with JSON storage.

## Features

- Send messages with username and message text
- View all messages sorted by timestamp (newest first)
- Persistent JSON storage
- 404 error handling
- Docker support with volume persistence

## Requirements

- Python ≥3.10
- Poetry (for dependency management)

## Local Development

### Setup

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
# Or on macOS: brew install poetry
```

2. Install dependencies:
```bash
poetry install
```

Or using Makefile:
```bash
make install
```

3. Decode the logo (if not already done):
```bash
make decode-logo
# Or manually:
base64 -d static/logo.png.base64 > static/logo.png
```

### Running

Run the application:
```bash
poetry run python -m app.app
```

Or use the Makefile:
```bash
make run
```

The app will be available at `http://localhost:3000`

## Docker Setup

### Build and Run

```bash
docker compose up --build
```

Or using Makefile:
```bash
make docker-build
make docker-up
```

### Stop

```bash
docker compose down
```

Or:
```bash
make docker-down
```

The storage directory (`app/storage`) is mounted as a volume, so `data.json` persists on the host.

## Routes

- `GET /` - Home page (index.html)
- `GET /message` - Message form page
- `POST /message` - Submit a message (redirects to /read)
- `GET /read` - View all messages
- Any other route - 404 error page

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Factory function
│   ├── app.py               # Routes and handlers
│   └── storage/
│       ├── __init__.py
│       └── data.json        # Message storage
├── templates/
│   ├── index.html
│   ├── message.html
│   ├── read.html
│   └── error.html
├── static/
│   ├── style.css
│   ├── logo.png.base64
│   └── logo.png            # Auto-generated from base64
├── pyproject.toml        # Poetry configuration
├── poetry.lock           # Poetry lock file (generated)
├── Dockerfile
├── docker-compose.yaml
├── Makefile
└── README.md
```

## Screenshots

<!-- Add screenshots here -->
- Home page
- Message form
- Messages list
- 404 error page

## Makefile Targets

- `install` - Install dependencies with Poetry
- `run` - Run the app locally (via Poetry)
- `decode-logo` - Decode logo.png from base64
- `docker-build` - Build Docker image
- `docker-up` - Start Docker container
- `docker-down` - Stop Docker container
- `format` - Format code with black (via Poetry)

## Notes

- The app listens on `0.0.0.0:3000` by default
- Messages are stored in `app/storage/data.json` with timestamps as keys
- The logo is automatically decoded from base64 on first run if missing
- This project uses Poetry for dependency management

