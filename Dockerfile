
# Dockerfile for MedAssistAI
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "streamlit_medassistai.py", "--server.port=8501", "--server.address=0.0.0.0"]
