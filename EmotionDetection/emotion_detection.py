
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        
        if "emotionPredictions" in response_data and response_data["emotionPredictions"]:
            emotions = response_data["emotionPredictions"][0]["emotion"]
            
            # highest
            dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
            
            # dictionary
            result = {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": dominant_emotion
            }
            
            return result
        else:           
            return {
                "anger": 0,
                "disgust": 0,
                "fear": 0,
                "joy": 0,
                "sadness": 0,
                "dominant_emotion": None
            }
    else:
        return f"Error: Received status code {response.status_code}"