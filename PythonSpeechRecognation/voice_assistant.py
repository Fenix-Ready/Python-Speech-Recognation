from language_model.language_model import LanguageModel
from speech_recognizer.speech_recognizer import SpeechRecognizer
from command_processor.command_processor import CommandProcessor


class VoiceAssistant:
    def __init__(self):
        self.language_model = LanguageModel()

    def run(self):
        print("Выберите язык (ru/en):")
        lang_input = input().strip().lower()

        if lang_input in self.language_model.LANGUAGES:
            model = self.language_model.load_model(lang_input)
            if model:
                recognizer = SpeechRecognizer(model)
                command_processor = CommandProcessor()
                while True:
                    command = recognizer.recognize()
                    if command:
                        command_processor.process_command(command)
                        recognizer.close()
        else:
            print("Язык не поддерживается. Используется русский язык по умолчанию.")
            model = self.language_model.load_model('ru')
            if model:
                recognizer = SpeechRecognizer(model)
                command_processor = CommandProcessor()
                while True:
                    command = recognizer.recognize()
                    if command:
                        command_processor.process_command(command)
                        recognizer.close()


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
