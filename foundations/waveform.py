import librosa
import matplotlib.pyplot as plt
y,sr=librosa.load("sample.wav")
print("duration: ",librosa.get_duration(y=y, sr=sr))
print("sample rate: ",sr)
librosa.display.waveshow(y=y,sr=sr)
plt.savefig("C:/Users/abhin/git-test/ai-basics/artifacts/waveform.png")