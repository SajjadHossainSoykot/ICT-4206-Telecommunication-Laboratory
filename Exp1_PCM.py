import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
a = 4
fm = 2
fs = 100 * fm

# Time axis and original signal
t = np.arange(0, 1 + 1/fs, 1/fs)
x = a * np.sin(2 * np.pi * fm * t)

# Quantization levels and corresponding 3-bit codes
levels = np.array([
    -3.5, -2.5, -1.5, -0.5,
     0.5,  1.5,  2.5,  3.5
])

codes = [
    "000", "001", "010", "011",
    "100", "101", "110", "111"
]

# Quantization and encoding
xq = []
encoded = []

for sample in x:
    index = np.argmin(np.abs(levels - sample))
    xq.append(levels[index])
    encoded.append(codes[index])

xq = np.array(xq)

# Convert code words into a serial PCM bit stream
pcm_bits = []

for code in encoded:
    for bit in code:
        pcm_bits.append(int(bit))

pcm_bits = np.array(pcm_bits)

# Decoding
decoded = []

for code in encoded:
    index = codes.index(code)
    decoded.append(levels[index])

decoded = np.array(decoded)

# Simple reconstruction filter
window_size = 5
reconstructed = np.convolve(
    decoded,
    np.ones(window_size) / window_size,
    mode="same"
)

# Quantization error
quantization_error = x - xq
mse = np.mean(quantization_error ** 2)

print("First 20 PCM code words:")
print(" ".join(encoded[:20]))
print("Quantization MSE =", round(mse, 6))

# PCM waveform time axis
bit_time = np.arange(len(pcm_bits) + 1)
pcm_plot = np.append(pcm_bits, pcm_bits[-1])

# Plotting
plt.figure(figsize=(11, 14))

plt.subplot(6, 1, 1)
plt.plot(t, x)
plt.title("Original Message Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(6, 1, 2)
plt.stem(t, x, basefmt=" ")
plt.title("Sampled Message Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(6, 1, 3)
plt.step(t, xq, where="mid")
plt.title("Quantized Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(6, 1, 4)
plt.step(bit_time[:101], pcm_plot[:101], where="post")
plt.title("PCM Binary Waveform (First 100 Bits)")
plt.xlabel("Bit Number")
plt.ylabel("Binary Level")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.grid()

plt.subplot(6, 1, 5)
plt.step(t, decoded, where="mid")
plt.title("Decoded Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(6, 1, 6)
plt.plot(t, x, label="Original Signal")
plt.plot(t, reconstructed, label="Reconstructed Signal")
plt.title("Original and Reconstructed Signals")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()