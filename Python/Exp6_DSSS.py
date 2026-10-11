"""Experiment 6: DSSS with a 7-chip PN code and BPSK carrier."""
import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 0, 1])
pn = np.array([0, 0, 1, 0, 1, 1, 1])
L, samples = len(pn), 40
pn_polar = 2 * pn - 1
spread = np.concatenate([(2*b-1) * pn_polar for b in data])
baseband = np.repeat(spread, samples)
t = np.arange(len(baseband)) / (L * samples)
carrier = np.cos(2 * np.pi * 10 * t)
tx = baseband * carrier

# Despread and correlate using synchronized PN and carrier
pn_samples = np.repeat(np.tile(pn_polar, len(data)), samples)
received = []
for k in range(len(data)):
    sl = slice(k*L*samples, (k+1)*L*samples)
    received.append(int(np.sum(tx[sl]*carrier[sl]*pn_samples[sl]) > 0))
print('Sent bits:    ', data)
print('Received bits:', received)
print(f'Processing gain: {L} = {10*np.log10(L):.2f} dB')

fig, ax = plt.subplots(3, 1, figsize=(11, 7))
ax[0].step(t, baseband); ax[0].set_title('Baseband DSSS')
ax[1].plot(t, carrier); ax[1].set_title('Carrier')
ax[2].plot(t, tx); ax[2].set_title('DSSS-BPSK signal')
for a in ax: a.grid(True); a.set_xlim(0, len(data))
ax[-1].set_xlabel('Time (bit periods)')
plt.show()
