import subprocess
from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # Return a CORS-friendly response
    return Response("Rasa server is running 🎉", headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    })

if __name__ == "__main__":
    # Start Rasa in background
    rasa_command = [
        "rasa", "run",
        "--enable-api",
        "--cors", "*",
        "--port", "10000",
        "--host", "0.0.0.0",
        "-m", "models"
    ]
    subprocess.Popen(rasa_command)

    # Start lightweight Flask app to help Render detect the port
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
