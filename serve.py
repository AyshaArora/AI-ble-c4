# serve.py
import os
import threading
from flask import Flask, Response
from rasa.__main__ import main as rasa_main

app = Flask(__name__)

@app.route("/")
def hello():
    return Response("Rasa server is running 🎉", headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    })

def run_rasa():
    # This is equivalent to: rasa run --enable-api --cors "*" --port 10000 --host 0.0.0.0 -m models
    rasa_main([
        "run",
        "--enable-api",
        "--cors", "*",
        "--port", os.environ.get("PORT", "10000"),
        "--host", "0.0.0.0",
        "-m", "models"
    ])

if __name__ == "__main__":
    # Start Rasa in a background thread (same process)
    threading.Thread(target=run_rasa).start()

    # Start Flask app on the same port to keep Render happy
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
