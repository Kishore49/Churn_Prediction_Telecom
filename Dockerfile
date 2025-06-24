FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# This Dockerfile sets up a Python environment for a Streamlit application.
# It installs the necessary dependencies and exposes port 8501 for the Streamlit server.