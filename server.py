"""Serve the course emotion detector through Flask."""
from flask import Flask, render_template, request
from requests.exceptions import RequestException
from EmotionDetection import emotion_detector

APP = Flask(__name__)


@APP.route("/")
def index():
    """Display the supplied course template."""
    return render_template("index.html")


@APP.route("/emotionDetector")
def detect_emotion():
    """Analyze the input and present the required course response."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyze)
    except (RequestException, ValueError, KeyError, IndexError):
        return "Emotion analysis service is unavailable. Please try again later.", 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
