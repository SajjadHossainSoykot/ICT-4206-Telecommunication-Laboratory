import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# BPSK PARAMETERS
# ============================================================

# Binary sequence from the laboratory experiment
data = np.array([1, 0, 0, 1, 1, 1, 0])

samples_per_bit = 200
carrier_frequency = 2


# ============================================================
# POLAR CONVERSION
# ============================================================

# Binary:
# 1 -> +1
# 0 -> -1

polar_data = 2 * data - 1

message_signal = np.repeat(
    polar_data,
    samples_per_bit
)


# ============================================================
# TIME AXIS AND CARRIER
# ============================================================

time = np.arange(
    len(message_signal)
) / samples_per_bit

carrier = np.cos(
    2 * np.pi *
    carrier_frequency *
    time
)


# ============================================================
# BPSK MODULATION
# ============================================================

bpsk_signal = (
    message_signal * carrier
)


# ============================================================
# BPSK DEMODULATION
# ============================================================

demodulated = (
    bpsk_signal * carrier
)

recovered_data = []

for i in range(len(data)):

    start = i * samples_per_bit
    stop = start + samples_per_bit

    # Integrate over one bit interval
    value = np.sum(
        demodulated[start:stop]
    )

    if value >= 0:
        recovered_data.append(1)
    else:
        recovered_data.append(0)

recovered_data = np.array(
    recovered_data
)


# ============================================================
# BIT ERROR RATE
# ============================================================

bit_errors = np.count_nonzero(
    data != recovered_data
)

ber = bit_errors / len(data)


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("Original Data  :", data)
print("Polar Data     :", polar_data)
print("Recovered Data :", recovered_data)
print("Bit Errors     :", bit_errors)
print("Bit Error Rate :", ber)


# ============================================================
# PLOTTING
# ============================================================

plt.figure(figsize=(11, 11))


# 1. Polar message signal
plt.subplot(4, 1, 1)

plt.step(
    time,
    message_signal,
    where="post"
)

plt.title("Message Signal - Polar Form")
plt.ylabel("Amplitude")
plt.yticks([-1, 1])
plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data))
plt.grid()


# 2. Carrier signal
plt.subplot(4, 1, 2)

plt.plot(
    time,
    carrier
)

plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.xlim(0, len(data))
plt.grid()


# 3. BPSK signal
plt.subplot(4, 1, 3)

plt.plot(
    time,
    bpsk_signal
)

plt.title("BPSK Signal")
plt.ylabel("Amplitude")
plt.xlim(0, len(data))
plt.grid()


# 4. Recovered data
recovered_waveform = np.repeat(
    recovered_data,
    samples_per_bit
)

plt.subplot(4, 1, 4)

plt.step(
    time,
    recovered_waveform,
    where="post"
)

plt.title(
    f"Recovered Binary Data (BER = {ber:.3f})"
)

plt.xlabel("Time")
plt.ylabel("Binary Level")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.xlim(0, len(data))
plt.grid()


plt.tight_layout()
plt.show()