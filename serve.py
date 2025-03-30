# serve.py
import os
import threading
from flask import Flask, Response, send_from_directory
from rasa.__main__ import main as rasa_main

app = Flask(__name__, static_folder="static")

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/health")
def health():
    return Response("Rasa server is running 🎉", headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    })

def run_rasa():
    rasa_main([
        "run",
        "--enable-api",
        "--cors", "*",
        "--port", os.environ.get("PORT", "10000"),
        "--host", "0.0.0.0",
        "--connector", "rest",  # ✅ Enables /webhooks/rest/webhook
        "-m", "models"
    ])

if __name__ == "__main__":
    threading.Thread(target=run_rasa).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
