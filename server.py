from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector  # Corrected import

app = Flask("Final Project")

@app.route("/")
def render_index_page():
    """
    Render the main application page. This is the root route.
    
    Returns:
        str: The rendered HTML page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    This function processes the input text, handles errors, and returns the
    emotion scores for the given input.
    
    Returns:
        jsonify: A JSON response containing the emotion analysis or an error message.
    """
    text_to_detect = request.args.get('textToAnalyze')

    # Handle blank input case
    if not text_to_detect or text_to_detect.strip() == "":
        return jsonify({"error": "Invalid text! Please provide a valid statement."}), 400

    response = emotion_detector(text_to_detect)

    # Check for None dominant emotion and 400 status code
    if response["status_code"] == 400 or response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Format and return the response
    formatted_response = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }

    return jsonify(formatted_response)

if __name__ == '__main__':
    """
    Run the Flask application on the specified host and port.

    Starts the Flask web server and listens on the provided host (0.0.0.0)
    and port (5000). The debug mode is enabled for development purposes.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)  # Runs Flask server
