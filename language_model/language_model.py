import os
from vosk import Model


class LanguageModel:
    LANGUAGES = {
        'ru': r'language\russian_language\vosk-model-ru-0.42',  # Путь к русской модели
        'en': r'language\english_language\vosk-model-en-us-0.42-gigaspeech\vosk-model-en-us-0.42-gigaspeech'  # Путь к английской модели
    }

    @staticmethod
    def load_model(language):
        model_path = LanguageModel.LANGUAGES.get(language)
        if model_path and os.path.exists(model_path):
            return Model(model_path)
        else:
            print(f"Модель для языка '{language}' не найдена.")
            return None
