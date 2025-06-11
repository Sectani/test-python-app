# Use an official Python image from Docker Hub
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app code and requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py ./

# Run the Python app
CMD ["python", "app/main.py"]
