from fastapi import FastAPI

from EmotionClassification import classify_emotions

app = FastAPI()

@app.post('/emotion-detection')
def emotion_classification(text_body: str):
    # Находим словарь с вероятностями эмоций
    emotions = classify_emotions(text_body)
    if emotions:
        return classify_emotions(text_body)
    # Если не удалось вычислить эмоции - возвращаем ошибку
    else:
        return {
            'Error': 1,
            'description': 'Error during classification'
        }
        

# uvicorn main:app --host 127.0.0.1 --port 8000 --reload

# docker build --no-cache -t emo-api .
# docker images
# docker run -t -p 8003:8080 emo-api

# docker ps
# docker builder prune -f