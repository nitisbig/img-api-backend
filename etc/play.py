
import sounddevice as sd
import numpy as np

# Load PCM
pcm_file = "my.pcm"
raw_data = np.fromfile(pcm_file, dtype=np.int16)

# Play audio
sd.play(raw_data, samplerate=24000)
sd.wait()
