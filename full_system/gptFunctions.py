import base64
import requests
import whisper
from youtube_dl import YoutubeDL

# OpenAI API Key
api_key = "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" 

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function that takes in a photo path and a prompt and returns the response from the API
def getVisionResponse(path,prompt):

    # Function to encode the image

    # Path to your image
    image_path = path

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt + 'The above is an example of a conversation. You are the assistant. Keep the answer short an concise, unless specified otherwise.'
        
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

# Whisper transcript
def getWhisperTranscript(path):
    # model
    model = whisper.load_model("base")
    result = model.transcribe(path)
    print(result["text"])
    