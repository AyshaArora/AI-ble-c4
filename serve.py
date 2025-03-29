# serve.py
import subprocess
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Rasa server is running 🎉"

if __name__ == "__main__":
    # Start Rasa in background
    rasa_command = [
        "rasa", "run",
        "--enable-api",
        "--cors", "*",
        "-p", "10000",
        "-i", "0.0.0.0",
        "-m", "models"
    ]
    subprocess.Popen(rasa_command)
    
    # Start lightweight Flask app to satisfy Render's port detection
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
