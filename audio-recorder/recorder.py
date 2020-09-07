import sounddevice
import soundfile

sample_rate = 44100
duration = 10
devices = sounddevice.query_devices()
print(devices)
device = input("Please enter the ID of the device to record from: ")
sounddevice.default.device = int(device)
print ("recording...")
audio_recorder = sounddevice.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sounddevice.wait()
soundfile.write("audio.wav",audio_recorder,sample_rate)
