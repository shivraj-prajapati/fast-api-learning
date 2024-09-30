from enum import Enum
from fastapi import FastAPI, HTTPException

# Defining an Enum class for the model names
class ModelType(str, Enum):
    vgg16 = "vgg16"
    inception = "inception"
    mobilenet = "mobilenet"

app = FastAPI()

""" Define an endpoint to get the model name and return appropriate messages
and It is Generate a dropdown
"""
@app.get("/models/{model_type}")
async def get_model(model_type: ModelType):
    if model_type == ModelType.vgg16:
        return {"model_name": model_type, "message": "VGG16 for the win!"}
    
    elif model_type == ModelType.mobilenet:
        return {"model_name": model_type, "message": "MobileNet - Efficient and Lightweight!"}
    
    elif model_type == ModelType.inception:
        return {"model_name": model_type, "message": "Inception - GoogLeNet strikes again!"}
    
    raise HTTPException(status_code=404, detail="Model not found")

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8080)