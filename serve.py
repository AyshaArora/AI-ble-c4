import os
import asyncio
from flask import Flask, Response
from rasa.__main__ import main

app = Flask(__name__)

@app.route("/")
def hello():
    return Response("✅ Rasa server is running!", headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    })

async def start_rasa():
    await main([
        "run",
        "--enable-api",
        "--cors", "*",
        "--port", "10000",
        "--host", "0.0.0.0"
    ])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_rasa())

    port = int(os.environ.get("PORT", 10000))  # Render sets this
    app.run(host="0.0.0.0", port=port)
