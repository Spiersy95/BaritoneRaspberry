from audioreceiver import RATE
import numpy as np
from matplotlib import pyplot as plt


def get_top_frequency(audio_data):
    frequencies = np.fft.fft(audio_data)
    magnitudes = np.abs(frequencies)

    freq_values = np.fft.fftfreq(len(frequencies), 1 / RATE)

    range_of_frequencies = (20, 1000)

    range = np.where((freq_values >= range_of_frequencies[0]) & (freq_values <= range_of_frequencies[1]))

    plt.plot(freq_values[range], magnitudes[range])
    plt.title('Frequency Spectrum')
    plt.xlabel('Hz')

    plt.show()
