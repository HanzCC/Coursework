''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)

    for emotion, score in result:
        emotion_with_score = f" '{emotion}' : {score}, " 


    label = result['label']
    score = result['score']
    error_msg = "Invalid input! Try again"
    if label is not None: # pylint: disable=no-else-return
        return f"The text {text_to_analyse} has been identified as {label} with a score of {score}"
    else:
        return error_msg

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)