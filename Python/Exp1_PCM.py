"""Experiment 1: 3-bit PCM, quantization, decoding and reconstruction."""
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Original Message Signal
A, fm, fs = 4, 2, 200
t = np.arange(fs + 1) / fs
x = A * np.sin(2 * np.pi * fm * t)

# 2. Quantization (8 levels = 3 bits)
levels = np.arange(-3.5, 4, 1)
index = np.ceil(x + 4).astype(int) - 1
index = np.clip(index, 0, 7)
xq = levels[index]

# 3. PCM Encoding (Decimal to 3-bit Binary)
codes = [format(i, '03b') for i in index]
bits = [int(b) for code in codes for b in code]

# 4. PCM Decoding (Binary to Quantized Values)
decoded = np.array([levels[int(code, 2)] for code in codes])

# 5. (Optional) Signal Reconstruction using Low-Pass Filter 
try:
    # Sixth-order Butterworth LPF (if SciPy is installed)
    from scipy.signal import butter, lfilter

    b, a = butter(6, 4*fm/fs)
    reconstructed = lfilter(b, a, decoded)
    print("Using Butterworth Low-Pass Filter")

except ImportError:
    # (Optional) Simple first-order LPF (without SciPy)
    alpha = 1 - np.exp(-2*np.pi*(2*fm)/fs)
    reconstructed = np.zeros_like(decoded)

    for i in range(len(decoded)):
        previous = reconstructed[i-1] if i > 0 else 0
        reconstructed[i] = alpha*decoded[i] + (1-alpha)*previous

    print("Using Simple Low-Pass Filter")

# 6. Display Results
print("First 10 PCM Codes:", codes[:10])
print("PCM Bit Rate:", 3*fs, "bits/s")

# 7. Plot All Waveforms
fig, ax = plt.subplots(3, 2, figsize=(11, 8))

ax[0, 0].plot(t, x)
ax[0, 0].set_title("Original Message Signal")

ax[0, 1].stem(t, x, markerfmt='.')
ax[0, 1].set_title("Sampled Signal")

ax[1, 0].step(t, xq)
ax[1, 0].set_title("Quantized Signal")

ax[1, 1].step(range(60), bits[:60])
ax[1, 1].set_title("PCM Encoded Bits")

ax[2, 0].step(t, decoded)
ax[2, 0].set_title("Decoded Signal")

ax[2, 1].plot(t, x, 'k--', label="Original")
ax[2, 1].plot(t, reconstructed, label="Reconstructed")
ax[2, 1].legend()
ax[2, 1].set_title("Reconstructed Signal (LPF)")

# 8. Graph Formatting
for axis in ax.flat:
    axis.grid(True)

plt.tight_layout()
plt.show()
