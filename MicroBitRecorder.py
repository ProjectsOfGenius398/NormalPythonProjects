import pyaudio
import wave
import radio

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recording.wav"

p = pyaudio.PyAudio()

def start_recording():
    print("Starting recording...")
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("Recording saved as recording.wav")

def stop_recording():
    print("Stopping recording...")

radio.config(channel=17)
radio.on()

while True:
    message = radio.receive()
    if message == 'start_recording':
        start_recording()
    elif message == 'stop_recording':
        stop_recording()
        break
