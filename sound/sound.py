from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 10

myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 2)
sd.wait()
write('your_sound.wav',fs, myrecording)

playsound('your_sound.wav')