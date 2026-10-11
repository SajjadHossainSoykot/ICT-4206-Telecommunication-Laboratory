"""Experiment 7: BPSK mixed with a synchronized 7-frequency hopping carrier."""
import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])
hop_index = np.array([7, 3, 5, 1, 4, 6, 2, 7, 2, 5])
freq = np.array([1, 2, 3, 4, 6, 12, 24])
N = 120
local_t = np.arange(N) / N
t = np.arange(len(data)*N) / N
polar = np.repeat(2*data-1, N)
base_carrier = np.tile(np.cos(2*np.pi*local_t), len(data))
bpsk = polar * base_carrier
hop_carrier = np.zeros_like(bpsk)
for k, choice in enumerate(hop_index):
    hop_carrier[k*N:(k+1)*N] = np.cos(2*np.pi*freq[choice-1]*local_t)
fhss = bpsk * hop_carrier

# Coherent dehopping and bit detection (ideal/no noise)
received = []
for k in range(len(data)):
    sl = slice(k*N, (k+1)*N)
    received.append(int(np.sum(fhss[sl]*hop_carrier[sl]*base_carrier[sl]) > 0))
print('Hop frequencies:', freq[hop_index-1])
print('Sent bits:      ', data)
print('Recovered bits: ', received)

fig, ax = plt.subplots(4, 1, figsize=(11, 9))
ax[0].step(t, polar); ax[0].set_title('Original polar bits')
ax[1].plot(t, bpsk); ax[1].set_title('BPSK signal')
ax[2].plot(t, hop_carrier); ax[2].set_title('Hopping carrier (7 frequencies)')
ax[3].plot(t, fhss); ax[3].set_title('FHSS signal')
for a in ax: a.grid(True); a.set_xlim(0, len(data))
ax[-1].set_xlabel('Time (bit periods)')
plt.show()
