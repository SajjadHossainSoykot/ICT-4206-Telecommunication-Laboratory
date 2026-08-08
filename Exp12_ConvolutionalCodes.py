import numpy as np
import matplotlib.pyplot as plt

# Original message from the lab experiment
message = np.array([1, 0, 1, 1])

# Two termination zeros for two memory elements
input_bits = np.append(message, [0, 0])

# Initial shift-register contents
d1 = 0
d2 = 0

c1 = []
c2 = []
states = []
encoded_pairs = []

# Convolutional encoding
for bit in input_bits:

    # Store current encoder state
    states.append(f"{d1}{d2}")

    # Generator g1 = 111
    out1 = bit ^ d1 ^ d2

    # Generator g2 = 101
    out2 = bit ^ d2

    c1.append(out1)
    c2.append(out2)

    encoded_pairs.append([out1, out2])

    # Shift register
    d2 = d1
    d1 = bit

c1 = np.array(c1)
c2 = np.array(c2)
encoded_pairs = np.array(encoded_pairs)

# Convert output pairs into serial encoded sequence
encoded_bits = encoded_pairs.flatten()

# Display results
print("Original Message :", message)
print("Encoder Input    :", input_bits)
print("Generator 1      : 111")
print("Generator 2      : 101")
print()

print("Input   State   Output")
print("----------------------")

for i in range(len(input_bits)):
    print(
        f"  {input_bits[i]}      "
        f"{states[i]}      "
        f"{encoded_pairs[i][0]}"
        f"{encoded_pairs[i][1]}"
    )

print()
print("Output Pairs :",
      " ".join("".join(map(str, pair))
               for pair in encoded_pairs))

print("Encoded Bits :",
      "".join(map(str, encoded_bits)))


# -----------------------
# Plotting
# -----------------------

plt.figure(figsize=(10, 8))

# Original message
plt.subplot(3, 1, 1)
plt.step(
    np.arange(len(message) + 1),
    np.append(message, message[-1]),
    where="post"
)
plt.title("Original Binary Message")
plt.ylabel("Amplitude")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.grid()

# Encoder input with termination bits
plt.subplot(3, 1, 2)
plt.step(
    np.arange(len(input_bits) + 1),
    np.append(input_bits, input_bits[-1]),
    where="post"
)
plt.title("Encoder Input with Termination Bits")
plt.ylabel("Amplitude")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.grid()

# Final convolutionally encoded sequence
plt.subplot(3, 1, 3)
plt.step(
    np.arange(len(encoded_bits) + 1),
    np.append(encoded_bits, encoded_bits[-1]),
    where="post"
)
plt.title("Convolutionally Encoded Signal")
plt.xlabel("Bit Number")
plt.ylabel("Amplitude")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.grid()

plt.tight_layout()
plt.show()