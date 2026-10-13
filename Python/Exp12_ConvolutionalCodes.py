"""Experiment 12: Convolutional Coding, Viterbi Decoding and SNR."""
import numpy as np
import matplotlib.pyplot as plt

# 1. Convolutional Encoding (2,1,2)
message = [1, 0, 1, 1]
input_bits = message + [0, 0]  # Two terminating zeros
d1 = d2 = 0
encoded = []

for bit in input_bits:
    c1 = bit ^ d1 ^ d2       # Generator g1 = 111
    c2 = bit ^ d2            # Generator g2 = 101
    encoded += [c1, c2]
    d2, d1 = d1, bit         # Update shift registers

# 2. Viterbi Decoder (Hard Decision)
def viterbi(rx):
    paths = {(0, 0): (0, [])}

    for i in range(0, len(rx), 2):
        new = {}
        for (d1, d2), (cost, path) in paths.items():
            for bit in [0, 1]:
                expected = [bit ^ d1 ^ d2, bit ^ d2]
                errors = sum(a != b for a, b in zip(expected, rx[i:i+2]))
                state = (bit, d1)
                candidate = (cost + errors, path + [bit])

                if state not in new or candidate[0] < new[state][0]:
                    new[state] = candidate
        paths = new

    return paths[(0, 0)][1][:-2]  # Remove two tail bits

# 3. Add One Manual Bit Error
received = encoded.copy()
received[3] ^= 1            # Flip fourth encoded bit
corrected = viterbi(received)

# 4. Add Noise using SNR (Eb/N0)
EbN0_dB = 2                 # Change to 0, 2, 5, 8 dB
R = 1/2                     # Code rate
rng = np.random.default_rng(1)

symbols = 1 - 2*np.array(encoded)  # BPSK: 0 -> +1, 1 -> -1
snr = 10**(EbN0_dB/10)
sigma = np.sqrt(1/(2*R*snr))

noisy = symbols + rng.normal(0, sigma, len(symbols))
rx_noisy = (noisy < 0).astype(int).tolist()
decoded_noisy = viterbi(rx_noisy)

# 5. Display Results
print("Original Message:", message)
print("Encoded Bits:", encoded)
print("With One Error:", received)
print("Viterbi Decoded:", corrected)
print("SNR (Eb/N0):", EbN0_dB, "dB")
print("Noisy Received:", rx_noisy)
print("Decoded After Noise:", decoded_noisy)

# 6. Plot Waveforms
fig, ax = plt.subplots(4, 1, figsize=(10, 8))

signals = [message, encoded, rx_noisy, decoded_noisy]
titles = ["Original Message", "Encoded Bits",
          "Received Bits (AWGN)", "Viterbi Decoded Bits"]

for a, signal, title in zip(ax, signals, titles):
    a.step(range(len(signal)+1), signal+[signal[-1]], where='post')
    a.set_title(title)
    a.set_yticks([0, 1])
    a.set_ylim(-0.2, 1.2)
    a.grid(True)

ax[-1].set_xlabel("Bit Index")
plt.tight_layout()
plt.show()