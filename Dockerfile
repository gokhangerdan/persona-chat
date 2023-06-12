FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENV OPENAI_API_KEY open-ai-api-key

ENTRYPOINT ["streamlit", "run", "hello.py", "--server.port=8501", "--server.address=0.0.0.0"]