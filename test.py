from cic import CICDecimatorFilter
import matplotlib.pyplot as plt
import numpy as np

fs = 36000
duration = 0.2
decimation = 18

t = np.linspace(0, duration, round(fs * duration), endpoint=False)
t_filtered = np.linspace(0, duration, round(fs / decimation * duration), endpoint=False)

# generate a noisy waveform
waveform_frequency = 5
waveform = np.sin(2 * np.pi * waveform_frequency * t)
noise_amplitude = 0.3
noise = np.random.uniform(-noise_amplitude, noise_amplitude, len(t))
waveform += noise

filter = CICDecimatorFilter(R=decimation, N=6)
filtered = filter.update(waveform)
decimated = [x for (i, x) in enumerate(waveform) if i % decimation == 0]

plt.figure()
plt.plot(t, waveform, label="input waveform", color="blue")
plt.plot(t_filtered, decimated, label="decimated waveform", color="green")
plt.plot(t_filtered, filtered, label="filtered waveform", color="orange")
plt.legend()
plt.show()
