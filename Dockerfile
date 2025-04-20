# Use official Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY text_summarizer.py .

EXPOSE 8501

CMD ["streamlit", "run", "text_summarizer.py", "--server.port=8501", "--server.enableCORS=false"]
