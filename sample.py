import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq, irfft

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone1 = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
_, noise_tone2 = generate_sine_wave(10000, SAMPLE_RATE, DURATION)
noise_tone1 *= 0.3
noise_tone2 *= 0.5

mixed_tone = nice_tone + noise_tone1 + noise_tone2

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

N = SAMPLE_RATE * DURATION

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()

new_sig = irfft(yf)

plt.plot(new_sig[:1000])
plt.show()