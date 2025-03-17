# import os
# import openai
# from fastapi import FastAPI, HTTPException
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# OPENAI_KEY = os.getenv("OPENAI_KEY")
# OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")

# # Azure OpenAI Config
# openai.api_type = "azure"
# openai.api_base = OPENAI_ENDPOINT
# openai.api_version = "2023-03-15-preview"
# openai.api_key = OPENAI_KEY

# @app.post("/generate-text/")
# async def generate_text(prompt: str):
#     try:
#         response = openai.ChatCompletion.create(
#             engine="gpt-4",  # Change this to "gpt-35-turbo" if using GPT-3.5
#             messages=[{"role": "system", "content": "You are an eco-friendly assistant."},
#                       {"role": "user", "content": prompt}],
#             max_tokens=200
#         )
#         return {"response": response["choices"][0]["message"]["content"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import openai
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are EcoVoice, a sustainable living assistant focused on eco-friendly tips and environmental advice."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200
        )

        ai_response = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
