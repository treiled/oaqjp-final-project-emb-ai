"""
Flask server for emotion detection.

This module provides a simple Flask API for detecting emotions from text input.
It uses the `emotion_detector` function from the `EmotionDetection` package.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index():
    """
    Route for the home page.

    Returns a welcome message to the user.
    """
    return "Welcome to the Emotion Detection API!"


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Endpoint for emotion detection.

    This function handles POST requests to the /emotionDetector endpoint.
    It extracts the 'statement' from the JSON payload, processes it using the
    `emotion_detector` function, and returns the result as a JSON response.

    Returns:
        dict: A JSON response containing the detected emotions and the dominant emotion.
        If the input is invalid, it returns an error message with a 400 status code.
    """
    data = request.json  # Extract JSON data
    text = data.get("statement")  # Get the statement from the JSON payload

    if not text:
        return jsonify({"error": "Invalid input! Please provide a statement."}), 400

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    response = {
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": result["dominant_emotion"],
    }

    return jsonify(response)


if __name__ == "__main__":
    # Entry point of the application.
    # Runs the Flask server on host '0.0.0.0' and port 5000.
    app.run(host="0.0.0.0", port=5000)
    