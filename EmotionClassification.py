import torch
from transformers import pipeline

from IOUtils import read_params

# Считывание параметров из json-файла
params = read_params('params.json')

# Нужно ли использовать GPU или CPU
device = 0 if torch.cuda.is_available() and params['gpu'] else -1

# Создание пайплайна для emotion-detection
classifier = pipeline("text-classification",
                      model=params['model_name'],   # Название модели
                      return_all_scores=True,       # Возврат вероятностей по всем классам
                      device=device)                # На каком устройстве считать модель


"""
Определение эмоций по тексту
На выходе - словарь с вероятностями эмоций в формате {эмоция: вероятность}
Список определяемых эмоций: sadness, joy, love, anger, fear, surprise
"""
def classify_emotions(text: str) -> dict:
    try:
        # Находим распредим вероятности эмоций
        predictions = classifier(text.lower())[0]
        predictions = {emo['label']: emo['score'] for emo in predictions}
    except Exception:
        predictions = None
    return predictions
