import os
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import webbrowser

# Словарь для поддержки языков и соответствующих моделей
LANGUAGES = {
    'ru': '/path/to/vosk-model-ru-0.10',  # Путь к русской модели
    'en': '/path/to/vosk-model-en-us-0.22',  # Путь к английской модели
    # Добавьте другие языки и пути к моделям по мере необходимости
}

def load_model(language):
    model_path = LANGUAGES.get(language)
    if model_path and os.path.exists(model_path):
        return Model(model_path)
    else:
        print(f"Модель для языка '{language}' не найдена.")
        return None

def recognize_speech(model):
    rec = KaldiRecognizer(model, 8000)

    # Настройка микрофона
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=8000, input=True, frames_per_buffer=8000)
    stream.start_stream()

<<<<<<< HEAD
    print("Скажите что-нибудь...")
=======
    print("Начинайте говорить...")
>>>>>>> origin/main

    # Распознавание «на лету» с микрофона
    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            print(result)
            process_command(json.loads(result)['text'])
        else:
            partial_result = rec.PartialResult()
            print(partial_result)

def process_command(command):
    command = command.lower()
    if "открой google" in command:
        webbrowser.open("https://www.google.com")
        print("Открываю Google...")
    # Добавьте другие команды по мере необходимости

def main():
    print("Выберите язык (ru/en):")
    lang_input = input().strip().lower()

    if lang_input in LANGUAGES:
        model = load_model(lang_input)
        if model:
            recognize_speech(model)
    else:
        print("Язык не поддерживается. Используется русский по умолчанию.")
        model = load_model('ru')
        if model:
            recognize_speech(model)

if __name__ == "__main__":
    main()
