# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

# Copy Poetry files
COPY pyproject.toml poetry.lock* ./

# Install dependencies (without dev dependencies, skip installing current project)
RUN poetry install --only main --no-interaction --no-ansi --no-root

# Copy application code
COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/

# Expose port
EXPOSE 3000

# Run with gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:3000", "app:app"]

