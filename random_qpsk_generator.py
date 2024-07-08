import numpy as np
from scipy.io.wavfile import write

def generate_qpsk_signal(num_symbols, samples_per_symbol, noise_level):

    bits = np.random.randint(0, 2, num_symbols * 2)

    symbols = []
    for i in range(0, len(bits), 2):
        b0 = bits[i]
        b1 = bits[i + 1]
        if b0 == 0 and b1 == 0:
            symbols.append(1 + 1j)
        elif b0 == 0 and b1 == 1:
            symbols.append(1 - 1j)
        elif b0 == 1 and b1 == 0:
            symbols.append(-1 + 1j)
        elif b0 == 1 and b1 == 1:
            symbols.append(-1 - 1j)
    
    symbols = np.array(symbols)

    signal = np.zeros(num_symbols * samples_per_symbol, dtype=complex)
    signal[::samples_per_symbol] = symbols

    noise = noise_level * (np.random.randn(num_symbols * samples_per_symbol) + 
                           1j * np.random.randn(num_symbols * samples_per_symbol))
    signal += noise

    I = np.real(signal)
    Q = np.imag(signal)

    interleaved_signal = np.empty((num_symbols * samples_per_symbol * 2,), dtype=np.float32)
    interleaved_signal[0::2] = I
    interleaved_signal[1::2] = Q
    
    return interleaved_signal

def save_wav(file_path, signal, sample_rate):
    signal = signal / np.max(np.abs(signal))
    write(file_path, sample_rate, signal)

def main():
    num_symbols = 1000             # Number of QPSK symbols
    samples_per_symbol = 10        # Samples per QPSK symbol
    noise_level = 0.1              # Noise level (0 for no noise)
    sample_rate = 48000            # Sample rate for the WAV file
    file_path = 'qpsk_signal.wav'  # Output file path

    signal = generate_qpsk_signal(num_symbols, samples_per_symbol, noise_level)

    save_wav(file_path, signal, sample_rate)
    
    print(f"QPSK signal saved as '{file_path}'")

if __name__ == "__main__":
    main()
