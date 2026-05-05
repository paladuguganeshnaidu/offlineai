from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)
@app.route("/ask", methods=["POST"])
def ask():
    user_prompt = request.json.get("prompt")
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1:8b",
            "prompt": user_prompt,
            "stream": False
        }
    )
    output=response.json()["response"]
    return jsonify({"response":output})
if __name__ == "__main__":
    app.run(port=5000)