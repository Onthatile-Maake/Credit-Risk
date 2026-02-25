# 1. Use a lightweight Python image
FROM python:3.9-slim

# 2. Set the directory inside the container
WORKDIR /app

# 3. Copy your requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your folders and files into the container
COPY model/ ./model/
COPY main.py .

# 5. Tell Docker to open port 8000
EXPOSE 8000

# 6. Command to run the API when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
