from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector  # Corrected import

app = Flask("Final Project")

@app.route("/emotionDetector", methods=['GET'])
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze')

    # Handle blank input case
    if not text_to_detect or text_to_detect.strip() == "":
        return jsonify({"error": "Invalid text! Please provide a valid statement."}), 400

    response = emotion_detector(text_to_detect)

    # Check for None dominant emotion
    if response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

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
    app.run(host='0.0.0.0', port=5000, debug=True)