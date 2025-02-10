import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(URL, json=data, headers=headers)
    response_data = json.loads(response.text)

    if response.status_code == 200:
        emotion_scores = response_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)  # Calculate the dominant emotion
        
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion  # Add the dominant emotion to the result
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

def predict_emotions(emotion_data):
    if all(value is None for value in emotion_data.values()):
        return emotion_data

    if emotion_data['emotionPredictions'] is not None:
        emotion_scores = emotion_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
