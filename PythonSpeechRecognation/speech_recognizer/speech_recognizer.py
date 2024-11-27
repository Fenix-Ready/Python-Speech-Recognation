import json
import pyaudio
from vosk import KaldiRecognizer


class SpeechRecognizer:
    def __init__(self, model):
        self.recognizer = KaldiRecognizer(model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

    def recognize(self):
        print("Начинайте говорить...")
        while True:
            data = self.stream.read(8192)
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                print(result)
                return json.loads(result)['text']

    # def close(self):
    # self.stream.stop_stream()
    # self.stream.close()
    # self.p.terminate()
