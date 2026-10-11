
"""Experiment 6: DSSS using 7-chip PN code and BPSK."""
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Binary Data and PN Code
data = np.array([1, 0, 1])
pn = np.array([0, 0, 1, 0, 1, 1, 1])
L, samples = len(pn), 40

# 2. Convert 0 to -1 and 1 to +1
message = 2 * data - 1
pn_polar = 2 * pn - 1

# 3. DSSS Spreading
message_chips = np.repeat(message, L)
pn_chips = np.tile(pn_polar, len(data))
spread = message_chips * pn_chips

# 4. BPSK Modulation with Cosine Carrier
baseband = np.repeat(spread, samples)
pn_wave = np.repeat(pn_chips, samples)
t = np.arange(len(baseband)) / (L * samples)
carrier = np.cos(2 * np.pi * 10 * t)
tx = baseband * carrier

# 5. Optional: Despreading and Data Recovery
despread = tx * carrier * pn_wave
received = []

for i in range(len(data)):
    start = i * L * samples
    end = (i + 1) * L * samples
    bit = int(np.sum(despread[start:end]) > 0)
    received.append(bit)

# 6. Display Results
print("Sent bits:    ", data)
print("Received bits:", received)
print(f"Processing Gain: {10*np.log10(L):.2f} dB")

# 7. Plot DSSS Waveforms
fig, ax = plt.subplots(3, 1, figsize=(11, 7))

ax[0].step(t, baseband)
ax[0].set_title("Baseband DSSS")

ax[1].plot(t, carrier)
ax[1].set_title("Carrier Signal")

ax[2].plot(t, tx)
ax[2].set_title("DSSS-BPSK Signal")

for a in ax:
    a.grid(True)
    a.set_xlim(0, len(data))

ax[-1].set_xlabel("Time (bit periods)")
plt.tight_layout()
plt.show()
