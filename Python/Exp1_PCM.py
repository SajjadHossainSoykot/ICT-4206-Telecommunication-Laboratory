"""Experiment 1: 3-bit PCM, quantization, decoding and reconstruction."""
import numpy as np
import matplotlib.pyplot as plt

A, fm, fs = 4, 2, 200
t = np.arange(fs + 1) / fs
x = A * np.sin(2 * np.pi * fm * t)

levels = np.arange(-3.5, 4, 1)
index = np.clip(np.ceil(x + 4).astype(int), 1, 8) - 1
quantized = levels[index]
words = np.array([[int(b) for b in f"{v:03b}"] for v in index])
bits = words.ravel()
decoded = levels[words @ np.array([4, 2, 1])]

# Manual: sixth-order Butterworth; first-order fallback without SciPy
try:
    from scipy.signal import butter, lfilter
    b, a = butter(6, 4*fm/fs)
    reconstructed = lfilter(b, a, decoded)
    print('LPF: sixth-order Butterworth (matches manual)')
except ImportError:
    alpha = 1 - np.exp(-2 * np.pi * (2*fm) / fs)
    reconstructed = np.zeros_like(decoded)
    for k in range(len(decoded)):
        reconstructed[k] = alpha*decoded[k] + (1-alpha)*(reconstructed[k-1] if k else 0)
    print('LPF: simple first-order fallback (no SciPy)')

print('First 12 PCM words:', ' '.join(''.join(map(str, w)) for w in words[:12]))
print('Sampling rate:', fs, 'Hz; PCM bit rate:', 3*fs, 'bits/s')
print('Quantization MSE:', round(np.mean((x-quantized)**2), 4))

fig, ax = plt.subplots(3, 2, figsize=(11, 8))
ax[0, 0].plot(t, x); ax[0, 0].set_title('Original message')
ax[0, 1].stem(t, x, markerfmt='.'); ax[0, 1].set_title('Sampled message')
ax[1, 0].step(t, quantized); ax[1, 0].set_title('Quantized signal')
ax[1, 1].step(np.arange(60), bits[:60]); ax[1, 1].set_title('PCM bits (first 60)')
ax[2, 0].step(t, decoded); ax[2, 0].set_title('Decoded signal')
ax[2, 1].plot(t, x, 'k--', label='Original')
ax[2, 1].plot(t, reconstructed, label='Reconstructed')
ax[2, 1].legend(); ax[2, 1].set_title('Reconstructed (LPF)')
for a in ax.flat: a.grid(True); a.set_xlabel('Time / sample / bit index')
fig.tight_layout()
plt.show()
