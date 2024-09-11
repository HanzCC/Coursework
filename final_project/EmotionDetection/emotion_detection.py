import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myresult = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myresult, headers=header)
    formatted_response = json.loads(response.text)
    simplified_result = formatted_response['emotionPredictions'][0]['emotion']

    score_list = []
    emotion_list = []
    for k, v in simplified_result.items():
        emotion_list.append(k)
        score_list.append(v)
    simplified_result['dominant_emotion'] = emotion_list[score_list.index(max(score_list))]  

    return simplified_result

result = emotion_detector("I love this new technology.")

for emotion, score in result.items():
    emotion_with_score = f" '{emotion}' : {score}, " 
print(f"For the given statement, the system response is {emotion_with_score}")

# print(emotion_detector("I love this new technology."))

