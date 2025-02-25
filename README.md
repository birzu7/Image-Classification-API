# Image Classification API

A FastAPI-based cloud-ready microservice for image classification using a pre-trained ResNet model.

Overview:

This project provides an image classification API built with FastAPI and PyTorch. The API loads a pre-trained ResNet model, processes uploaded images, and returns class predictions.

✅ Machine Learning: Uses ResNet for image classification

✅ Cloud-Ready: Dockerized for deployment on AWS, GCP, or Azure

✅ FastAPI: High-performance backend for real-time inference

✅ Scalable Microservice: Designed for easy scaling and integration

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
        
