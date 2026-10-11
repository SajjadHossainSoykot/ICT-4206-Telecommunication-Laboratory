
"""Experiment 12: (2,1,2) Convolutional Encoder."""
import matplotlib.pyplot as plt

# 1. Original Message and Two Terminating Zeros
message = [1, 0, 1, 1]
input_bits = message + [0, 0]

# 2. Initialize Two Shift Registers
d1 = d2 = 0
pairs = []

# 3. Convolutional Encoding using XOR
for bit in input_bits:
    c1 = bit ^ d1 ^ d2     # Generator g1 = 111
    c2 = bit ^ d2          # Generator g2 = 101
    pairs.append([c1, c2])
    d2, d1 = d1, bit       # Shift registers

# 4. Convert Output Pairs into Serial Bit Stream
encoded = [b for pair in pairs for b in pair]

# 5. Display Results
print("Encoder input:", input_bits)
print("Output pairs:", ' '.join(''.join(map(str, p)) for p in pairs))
print("Encoded stream:", ''.join(map(str, encoded)))

# 6. Plot Original and Encoded Signals
fig, ax = plt.subplots(2, 1, figsize=(10, 5))

ax[0].step(range(len(message)+1), message + [message[-1]], where='post')
ax[0].set_title("Original Message")

ax[1].step(range(len(encoded)+1), encoded + [encoded[-1]], where='post')
ax[1].set_title("Convolutional Encoded Stream")

for a in ax:
    a.set_ylim(-0.2, 1.2)
    a.set_yticks([0, 1])
    a.grid(True)

ax[1].set_xlabel("Bit Index")
plt.tight_layout()
plt.show()
