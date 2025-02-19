"""
Flask web application for emotion detection.

This module provides a Flask-based API that detects emotions in user-provided text.
"""

from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector  # Ensure correct import path

app = Flask("Final Project")

@app.route("/")
def render_index_page():
    """
    Render the main application page.

    Returns:
        str: The rendered HTML page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.

    Retrieves the input text from the request, processes it using the 
    emotion detector function, and returns a JSON response containing 
    emotion scores.

    Returns:
        jsonify: A JSON response containing the emotion analysis or an error message.
    """
    text_to_detect = request.args.get("textToAnalyze")

    # Handle blank input case
    if not text_to_detect or text_to_detect.strip() == "":
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }), 400

    response = emotion_detector(text_to_detect)

    # If status_code = 400, return None for all values
    if response.get("status_code") == 400:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }), 400

    # If dominant_emotion is None, return an error message
    if response.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Format and return the response
    return jsonify({
        "anger": response.get("anger"),
        "disgust": response.get("disgust"),
        "fear": response.get("fear"),
        "joy": response.get("joy"),
        "sadness": response.get("sadness"),
        "dominant_emotion": response.get("dominant_emotion"),
    })

if __name__ == "__main__":
    """
    Run the Flask application.

    The app runs on host '0.0.0.0' and port 5000, with debug mode enabled 
    for development purposes.
    """
    app.run(host="0.0.0.0", port=5000, debug=True)  # Ensure no extra text here!
