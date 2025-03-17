import os
import requests
from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

VISION_KEY = os.getenv("VISION_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")

@app.post("/analyze-image/")
async def analyze_image(image: UploadFile = File(...)):
    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/octet-stream"
    }

    image_data = await image.read()

    response = requests.post(
        f"{VISION_ENDPOINT}/vision/v3.2/analyze?visualFeatures=Categories,Description,Objects",
        headers=headers,
        data=image_data
    )

    return response.json()
