import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def read_audio(file_path):
    sample_rate, data = wavfile.read(file_path)
    data = data / np.max(np.abs(data))
    
    if len(data.shape) > 1:
        data = data[:, 0]
    
    return sample_rate, data

def extract_iq(data):
    I = data[0::2]
    Q = data[1::2]
    return I, Q

def plot_qpsk_constellation(I, Q):
    plt.figure(figsize=(6, 6))
    plt.scatter(I, Q, color='blue', s=1)
    plt.title('QPSK Constellation Diagram')
    plt.xlabel('In-phase (I)')
    plt.ylabel('Quadrature (Q)')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.show()

def main():
    file_path = 'LRPT.wav'

    sample_rate, data = read_audio(file_path)

    I, Q = extract_iq(data)

    plot_qpsk_constellation(I, Q)

if __name__ == "__main__":
    main()
