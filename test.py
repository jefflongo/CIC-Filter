from cic import CICDecimatorFilter
import matplotlib.pyplot as plt
import numpy as np

fs = 36000
duration = 0.2
decimation = 16

t = np.linspace(0, duration, round(fs * duration), endpoint=False)
t_filtered = np.linspace(0, duration, round(fs / decimation * duration), endpoint=False)

# generate a noisy waveform
waveform_frequency = 5
waveform = np.sin(2 * np.pi * waveform_frequency * t)
noise_amplitude = 0.3
noise = np.random.uniform(-noise_amplitude, noise_amplitude, len(t))
waveform += noise

filter = CICDecimatorFilter(R=decimation, N=3)
filtered = filter.update(waveform)

plt.figure()
plt.plot(t, waveform, label="input waveform")
plt.plot(t_filtered, filtered, label="filtered waveform")
plt.legend()
plt.show()
