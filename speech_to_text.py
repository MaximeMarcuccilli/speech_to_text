import requests
import subprocess
import json
import pyaudio
import wave
import sys

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'QZUDTGCOIAI47OSLTI2YFY7UOB6VWG4G'

def read_audio(WAVE_FILENAME):
    # function to read audio(wav) file
    with open(WAVE_FILENAME, 'rb') as f:
        audio = f.read()
    return audio

def converter(input, output) :
    command = "ffmpeg -y -i "+input+" -ac 1 "+output
    subprocess.call(command, shell=True)

def RecognizeSpeech(AUDIO_FILENAME):
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/mpeg3'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    text = data['_text']
    
    # return the text
    return text


if __name__ == "__main__":
    converter(sys.argv[1],'son.mp3')
    text =  RecognizeSpeech('son.mp3')
    print("\nYou said: {}".format(text))
