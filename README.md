# Image Classification API

This project is a simple image classification API built using FastAPI and a pre-trained ResNet model.

## How to Run

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Run FastAPI server:
   ```sh
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Test API:
   ```sh
   curl -X 'POST' 'http://127.0.0.1:8000/predict' -F 'file=@image.jpg'
   ```

## Docker Instructions

1. Build Docker image:
   ```sh
   docker build -t image-classification-api .
   ```

2. Run Docker container:
   ```sh
   docker run -p 8000:8000 image-classification-api
   ```

## Endpoints

- `POST /predict`: Upload an image and get classification results.
- `GET /health`: Health check endpoint.

## Deployment

You can deploy this using AWS, Google Cloud, or Azure.
        