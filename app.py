from flask import Flask, request
import sounddevice as sd
import vosk
import spacy
import json

model = vosk.Model("vosk-model-uk-v3-lgraph")
device = sd.default.device = 1,4
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
rec = vosk.KaldiRecognizer(model,samplerate)
print('Start')

app = Flask(__name__)

@app.route('/',methods=['POST'])
def handle_get_request():
    # Обробка GET-запиту
    data = request.data
    if rec.AcceptWaveform(data):
        text = json.loads(rec.Result())['text'].lower()
        return text
    else:
        return 'No text'
    
@app.route('/video',methods=['POST'])
def handle_get_video_request():
    data = request.data


if __name__ == '__main__':
    app.run(debug=True)