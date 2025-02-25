FROM python:3.9-slim

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the FastAPI app
COPY ./app /app

# Expose port 8000 for FastAPI
EXPOSE 8000

# Set the working directory
WORKDIR /app

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
        