from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import torch
from torchvision import models, transforms
from PIL import Image
import io

app = FastAPI()

# Load pre-trained model (ResNet18 for example)
model = models.resnet18(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Define the transformation for the input image
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

class PredictionResponse(BaseModel):
    label: str
    confidence: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Read image
    img = Image.open(io.BytesIO(await file.read()))
    
    # Apply transformation
    img_tensor = transform(img).unsqueeze(0)  # Add batch dimension
    
    # Perform inference
    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
        confidence = torch.nn.functional.softmax(outputs, dim=1)[0][predicted].item()

    # Return the prediction result
    return PredictionResponse(label=str(predicted.item()), confidence=confidence)

@app.get("/health")
async def health():
    return {"status": "up and running"}
        