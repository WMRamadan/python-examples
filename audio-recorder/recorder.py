import sounddevice
import soundfile

# Sample rate used for recording
sample_rate = 44100
# Duration of recording in seconds
duration = 10
# Get list of devices to record from
devices = sounddevice.query_devices()
print(devices)
# Select device to record from
device = input("Please enter the ID of the device to record from: ")
sounddevice.default.device = int(device)
# Start recording based on recording duration
print ("recording...")
audio_recorder = sounddevice.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sounddevice.wait()
# Write audio file to disk
soundfile.write("audio.wav",audio_recorder,sample_rate)
