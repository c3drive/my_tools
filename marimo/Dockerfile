FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir \
    marimo \
    anthropic \
    python-dotenv \
    pandas \
    numpy \
    matplotlib \
    tqdm \
    sentence-transformers \
    rank_bm25 \
    pypdf \
    mcp \
    httpx

EXPOSE 2718

# ファイル名はdocker-compose側で制御するため、ここでは最小限の起動設定のみ
CMD ["marimo", "edit", "--host", "0.0.0.0", "--port", "2718"]