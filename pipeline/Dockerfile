FROM python:3.13-slim

WORKDIR /code 

# Package manager (uv) install karo speed aur reliability ke liye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Dependencies install karo using uv (fast)
RUN uv pip install --system pandas pyarrow sqlalchemy psycopg2-binary tqdm click

# Script ko container mein copy karo
COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]