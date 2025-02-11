from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector  # Corrected import

app = Flask("Final Project")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze')

    if not text_to_detect:
        return "Invalid text! Please provide a valid statement.", 400

    response = emotion_detector(text_to_detect)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    formatted_response = (
        f"For the input statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Runs Flask server
