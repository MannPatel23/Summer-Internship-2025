import boto3
import json
import base64
from PIL import Image
from io import BytesIO

prompt_data = "Provide me a 4K HD image of a beach, with blue sky in the rainy season and cinematic display."

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "textToImageParams": {
        "text": prompt_data
    },
    "taskType": "TEXT_IMAGE",
    "imageGenerationConfig": {
        "cfgScale": 10,
        "seed": 42,
        "quality": "standard",
        "width": 1024,
        "height": 1024,
        "numberOfImages": 1
    }
}

body = json.dumps(payload)

response = bedrock.invoke_model(
    body=body,
    modelId="amazon.titan-image-generator-v1",
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
images = response_body.get("images", [])

if not images:
    raise Exception("No image returned from the model.")

for image_data in images:
    image_bytes = base64.b64decode(image_data)
    img = Image.open(BytesIO(image_bytes))
    img.show()  
