# opensourceASR

This repository aims to collect available open soure ASR model, and share the code on how to generate the transcript using the corresponding third-party ASR systems. 
We have also shared the code how to use Google API ASR and more recent Whisper OpenAI ASR systems. 

### Google API
First, you have to install the following package before able to run the code
```js
pip install SpeechRecognition
```

Then the code can be executed by using the following command
```js
python google_asr.py
```

### Whisper OpenAI
The installation of Whisper can be done using the following procedure
```js
pip install -U openai-whisper
```

For running the code, please use the following command
```js
python whisper_asr_all.py
```


