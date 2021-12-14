# Emotion Detection in Text
REST API для определения эмоций в тексте при на основе модели BERT от Huggingface

В качестве классификатора взята модель [bhadresh-savani/bert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion). Модель обучена на датасете [Dataset: emotion](https://huggingface.co/datasets/viewer/?dataset=emotion).

Для написания REST API использовалась библиотека FastAPI. Для запуска сервера - Uvicorn

API предоставляет возможность запуска как непосредственно с помощью скриптов, так и посредством сбора Docker-контейнера



## Params
Параметры сервиса описаны в файле ```params.json```:

- ```model_name``` - какая модель используется для классификации эмоций; по умолчанию - "bhadresh-savani/bert-base-uncased-emotion"
- ```gpu``` - нужно ли использовать модель на GPU (true - использовать gpu, falce - использовать cpu); по умолчанию - falce

Если вы собираете Docker-контейнер, то параметры необходимо указать в файле непосредственно перед его сбором



## Run server
Для запуска сервера с помощью скриптов воспользуйтесь следующим набором команд
```
cd ./TextEmotionDetection
pip install -r ./requirements.txt
python ./downloads_dependencies.py
uvicorn main:app --host 127.0.0.1 --port 8000
```

Если вы используете Docker, воспользуйтесь следующим набором команд
```
cd ./TextEmotionDetection
docker build --no-cache -t emo-api .
docker run -t -p 8000:8080 emo-api
```

После запуска сервера API будет доступно по адресу 127.0.0.1:8000

Для остановки работы сервера воспользуйтесь сочетанием клавиш ```Ctrl+C```



## API Access
Для нахождения эмоций по тексту используйте POST-метод API: ```127.0.0.1:8000/emotion-detection```

Метод принимает на вход параметр ```text_body```, посредством которого передается текст для дальнейшей классификации

То есть, чтобы классифицировать текст "Hello", передайте его API следующим образом: ```127.0.0.1:8000/emotion-detection?text_body=Hello```

API возвращает ответ в формате json. Всего используется 6 различных эмоций: ***sadness, joy, love, anger, fear, surprise***. Пример ответа представлен ниже:
```
{
  "sadness": 0.0007061687065288424,
  "joy": 0.00047654396621510386,
  "love": 0.000440794974565506,
  "anger": 0.9975681900978088,
  "fear": 0.0004177686059847474,
  "surprise": 0.00039057875983417034
}
```
Для более удобной работы с API в тестовом режиме, воспользуйтесть ```127.0.0.1:8000/docs```



## Errors
Если в ходе вычислениявозникла ошибка, вместо json c эмоциями API вернет словарь с ошибкой, имеющий следующий вид:
```
{
  "Error": 1,
  "description": "Error during classification"
}
```








