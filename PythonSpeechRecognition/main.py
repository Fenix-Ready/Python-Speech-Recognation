import os
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import webbrowser


def load_languages_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            languages = json.load(file)  # Загружаем данные как JSON
            return languages
    except Exception as e:
        print(f"Ошибка при загрузке языков из файла: {e}")
        return {}


def load_model(language, languages):
    model_path = languages.get(language)
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

    print("Начинайте говорить...")

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
    languages = load_languages_from_file("Dictionary\\Dictionary_settings.txt")

    print("Выберите язык (ru/en):")
    lang_input = input().strip().lower()

    if lang_input in languages:
        model = load_model(lang_input, languages)
        if model:
            recognize_speech(model)
    else:
        print("Язык не поддерживается. Используется русский по умолчанию.")
        model = load_model('ru', languages)
        if model:
            recognize_speech(model)


if __name__ == "__main__":
    main()
