"""Experiment 12: (2,1,2) convolutional encoder, g1=111, g2=101."""
import numpy as np
import matplotlib.pyplot as plt

message = [1, 0, 1, 1]
input_bits = message + [0, 0]      # terminate two shift registers
d1 = d2 = 0
pairs = []
for bit in input_bits:
    pairs.append([bit ^ d1 ^ d2, bit ^ d2])
    d2, d1 = d1, bit
serial = [bit for pair in pairs for bit in pair]

print('Encoder input:', input_bits)
print('Output pairs:', ' '.join(''.join(map(str, p)) for p in pairs))
print('Encoded stream:', ''.join(map(str, serial)))

fig, ax = plt.subplots(2, 1, figsize=(10, 5))
ax[0].step(range(len(message)+1), message + [message[-1]], where='post')
ax[0].set_title('Original message')
ax[1].step(range(len(serial)+1), serial + [serial[-1]], where='post')
ax[1].set_title('Convolutionally encoded stream')
for a in ax: a.set_ylim(-0.2, 1.2); a.grid(True); a.set_yticks([0, 1])
ax[1].set_xlabel('Bit number')
fig.tight_layout(); fig.savefig('Exp12_ConvolutionalCodes_Output.png', dpi=160)
plt.show()
