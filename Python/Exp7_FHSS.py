
"""Experiment 7: FHSS using BPSK and seven hopping frequencies."""
import numpy as np
import matplotlib.pyplot as plt

# 1. Message bits, hop order and available frequencies
bits = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])
hop_index = np.array([7, 3, 5, 1, 4, 6, 2, 7, 2, 5])
freq = np.array([1, 2, 3, 4, 6, 12, 24])  # cycles per bit period
N = 120                                       # samples per bit (one hop)
t_bit = np.arange(N) / N                      # time for one bit
t = np.arange(len(bits) * N) / N              # time for all bits

# 2. Binary Data -> Polar Bits -> BPSK Carrier
polar = np.repeat(2 * bits - 1, N)
base_carrier = np.tile(np.cos(2 * np.pi * t_bit), len(bits))
bpsk = polar * base_carrier

# 3. Frequency-Hopping Carrier
hop_carrier = np.zeros_like(t)

for i, hop in enumerate(hop_index):
    start, end = i * N, (i + 1) * N
    hop_carrier[start:end] = np.cos(2 * np.pi * freq[hop-1] * t_bit)

# 4. FHSS Modulation (Mix BPSK with Hopping Carrier)
fhss = bpsk * hop_carrier

# 5. Optional: De-hopping and Data Recovery
received = []
for i in range(len(bits)):
    start, end = i * N, (i + 1) * N
    score = np.sum(fhss[start:end] * hop_carrier[start:end] * base_carrier[start:end])
    received.append(int(score > 0))

# 6. Display Results
print("Hop Frequencies:", freq[hop_index-1])
print("Sent Bits:      ", bits)
print("Recovered Bits: ", received)

# 7. Plot FHSS Waveforms
fig, ax = plt.subplots(4, 1, figsize=(11, 9))

ax[0].step(t, polar)
ax[0].set_title("Original Polar Bits")

ax[1].plot(t, bpsk)
ax[1].set_title("BPSK Modulated Signal")

ax[2].plot(t, hop_carrier)
ax[2].set_title("Hopping Carrier (7 Frequencies)")

ax[3].plot(t, fhss)
ax[3].set_title("FHSS Signal")

for a in ax:
    a.grid(True)
    a.set_xlim(0, len(bits))

ax[-1].set_xlabel("Time (bit periods)")
plt.tight_layout()
plt.show()
