import webbrowser
from langdetect import detect
from translate import Translator


class CommandProcessor:
    def __init__(self):
        self.translator = Translator(to_lang="en")

    def process_command(self, command):
        command = command.lower()
        words = command.split()
        language_results = []

        for word in words:
            try:
                lang = detect(word)
                if lang in ['en', 'ru']:
                    language_results.append((word, lang))
                else:
                    print(f"Слово '{word}' не является английским или русским.")

            except Exception as e:
                print(f"Ошибка при определении языка для слова '{word}': {e}")
                language_results.append((word, 'unknown'))

        reconstructed_sentence = ' '.join([word for word, lang in language_results])
        print("Определенные языки слов:", language_results)
        print("Составленное предложение:", reconstructed_sentence)

        translated_command = self.translator.translate(reconstructed_sentence)

        if "открой google" in translated_command:
            webbrowser.open("https://www.google.com")
            print("Открываю Google...")
