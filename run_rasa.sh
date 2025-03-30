#!/bin/bash

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source rasa38-env/bin/activate

# Train the Rasa model
echo "📦 Training Rasa model..."
rasa train

# Start Rasa server in the background
echo "🚀 Starting Rasa server..."
rasa run --enable-api --cors "*" --debug &

# Wait a moment to ensure Rasa starts before ngrok
sleep 5

# Start ngrok
echo "🌐 Launching ngrok tunnel on port 5005..."
ngrok http 5005
