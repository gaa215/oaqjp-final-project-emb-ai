import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Handle blank or None input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }

    data = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(URL, json=data, headers=headers)
        response_data = json.loads(response.text)

        if response.status_code == 200:
            emotion_scores = response_data['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            return {
                'anger': emotion_scores.get('anger'),
                'disgust': emotion_scores.get('disgust'),
                'fear': emotion_scores.get('fear'),
                'joy': emotion_scores.get('joy'),
                'sadness': emotion_scores.get('sadness'),
                'dominant_emotion': dominant_emotion,
                'status_code': response.status_code
            }
        else:
            # Handle unexpected status codes
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None,
                'status_code': response.status_code
            }
    except Exception as e:
        # Handle exceptions such as network errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 500  # Internal server error
        }
