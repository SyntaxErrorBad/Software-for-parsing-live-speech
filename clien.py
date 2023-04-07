import queue
import sounddevice as sd
import json
import requests



url = "http://127.0.0.1:5000"
headers = {"Content-Type": "application/octet-stream"}

q = queue.Queue()
device = sd.default.device = 1,4
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
print('Program started')

def callback(indata,frames,time,status):
    q.put(bytes(indata))


with sd.RawInputStream(samplerate=samplerate,blocksize=8000,device=device[0],dtype='int16',channels=1,callback=callback):
    #rec = vosk.KaldiRecognizer(model,samplerate)

    while True:
        data = q.get()
        response = requests.post(url, data=data,headers=headers)
        if response.text != "No text":
            print(response.text)
