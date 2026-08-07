import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# EXPERIMENT PARAMETERS
# ============================================================

# Fixed seed makes the experiment reproducible.
random_seed = 7
rng = np.random.default_rng(random_seed)

# Number of binary information bits
number_of_bits = 20

# Number of samples used to represent one bit
samples_per_bit = 240

# Normalized bit duration
bit_duration = 1.0

# Base BPSK carrier frequency in cycles per bit
base_carrier_frequency = 1.0

# Seven normalized hopping frequencies.
#
# These values represent the seven carrier patterns used in
# the supplied MATLAB laboratory program.
hop_frequencies = np.array(
    [24, 12, 6, 4, 3, 2, 1],
    dtype=float
)

number_of_hop_frequencies = len(hop_frequencies)


# ============================================================
# GENERATE BINARY INFORMATION
# ============================================================

binary_data = rng.integers(
    low=0,
    high=2,
    size=number_of_bits
)

# Polar NRZ conversion:
# Binary 0 -> -1
# Binary 1 -> +1
polar_data = 2 * binary_data - 1


# ============================================================
# GENERATE A PSEUDO-RANDOM HOPPING SEQUENCE
# ============================================================

# Generate enough shuffled frequency-index blocks to cover
# the complete binary sequence.
number_of_blocks = int(
    np.ceil(number_of_bits / number_of_hop_frequencies)
)

pn_hop_indices = np.concatenate(
    [
        rng.permutation(number_of_hop_frequencies)
        for _ in range(number_of_blocks)
    ]
)[:number_of_bits]

# Frequency selected during every bit interval
selected_hop_frequencies = hop_frequencies[pn_hop_indices]

# Convert the hop indices to three-bit PN words.
pn_code_words = [
    format(index, "03b")
    for index in pn_hop_indices
]


# ============================================================
# TIME AXES
# ============================================================

# Local time axis for one bit interval
local_time = (
    np.arange(samples_per_bit)
    / samples_per_bit
    * bit_duration
)

# Complete time axis
total_samples = number_of_bits * samples_per_bit

time = (
    np.arange(total_samples)
    / samples_per_bit
    * bit_duration
)


# ============================================================
# CREATE BINARY AND POLAR WAVEFORMS
# ============================================================

binary_waveform = np.repeat(
    binary_data,
    samples_per_bit
)

polar_waveform = np.repeat(
    polar_data,
    samples_per_bit
)


# ============================================================
# BPSK MODULATION
# ============================================================

# Base carrier during one bit interval
base_carrier_one_bit = np.cos(
    2
    * np.pi
    * base_carrier_frequency
    * local_time
)

# Repeat the base carrier for every bit
base_carrier = np.tile(
    base_carrier_one_bit,
    number_of_bits
)

# BPSK signal
bpsk_signal = polar_waveform * base_carrier


# ============================================================
# GENERATE THE FREQUENCY-HOPPING CARRIER
# ============================================================

hopping_carrier = np.zeros(
    total_samples,
    dtype=float
)

for bit_index, hop_frequency in enumerate(
    selected_hop_frequencies
):
    start = bit_index * samples_per_bit
    stop = start + samples_per_bit

    hopping_carrier[start:stop] = np.cos(
        2
        * np.pi
        * hop_frequency
        * local_time
    )


# A waveform containing the selected frequency value
# during each bit interval
frequency_sequence_waveform = np.repeat(
    selected_hop_frequencies,
    samples_per_bit
)


# ============================================================
# FREQUENCY HOPPING SPREAD SPECTRUM TRANSMITTER
# ============================================================

# Mixer output:
# FHSS signal = BPSK signal x hopping carrier
fhss_signal = bpsk_signal * hopping_carrier


# ============================================================
# IDEAL SYNCHRONIZED FHSS RECEIVER
# ============================================================

# The receiver generates exactly the same hopping carrier.
receiver_hopping_carrier = hopping_carrier.copy()

# Dehopping operation
#
# The multiplication by 2 compensates for the 1/2 factor
# introduced by cosine multiplication.
dehopped_signal = (
    2
    * fhss_signal
    * receiver_hopping_carrier
)


# ============================================================
# BPSK CORRELATION DETECTOR
# ============================================================

decision_metric = np.zeros(
    number_of_bits,
    dtype=float
)

recovered_bits = np.zeros(
    number_of_bits,
    dtype=int
)

for bit_index in range(number_of_bits):
    start = bit_index * samples_per_bit
    stop = start + samples_per_bit

    # Correlate the dehopped signal with the BPSK carrier.
    decision_metric[bit_index] = np.mean(
        dehopped_signal[start:stop]
        * base_carrier[start:stop]
    )

    # Zero-threshold decision
    recovered_bits[bit_index] = int(
        decision_metric[bit_index] >= 0
    )


recovered_binary_waveform = np.repeat(
    recovered_bits,
    samples_per_bit
)


# ============================================================
# BIT ERROR RATE
# ============================================================

bit_errors = np.count_nonzero(
    binary_data != recovered_bits
)

bit_error_rate = (
    bit_errors / number_of_bits
)


# ============================================================
# DISPLAY NUMERICAL RESULTS
# ============================================================

print("=" * 75)
print("FREQUENCY HOPPING SPREAD SPECTRUM")
print("=" * 75)

print(
    "Input binary sequence     :",
    " ".join(binary_data.astype(str))
)

print(
    "PN hop indices            :",
    " ".join(
        (pn_hop_indices + 1).astype(str)
    )
)

print(
    "Three-bit PN code words   :",
    " ".join(pn_code_words)
)

print(
    "Selected hop frequencies  :",
    " ".join(
        selected_hop_frequencies.astype(int).astype(str)
    ),
    "cycles/bit"
)

print(
    "Recovered binary sequence :",
    " ".join(recovered_bits.astype(str))
)

print(
    "Decision metrics          :",
    np.round(decision_metric, 4)
)

print("Number of bit errors      :", bit_errors)
print("Bit Error Rate            :", bit_error_rate)

print("=" * 75)


# ============================================================
# PLOTTING
# ============================================================

# The high-frequency continuous waveforms are displayed for
# only the first few bits so that their changes remain visible.
display_bits = 6
display_samples = display_bits * samples_per_bit

plt.figure(figsize=(14, 19))


# ------------------------------------------------------------
# 1. Original binary sequence
# ------------------------------------------------------------

plt.subplot(7, 1, 1)

plt.step(
    time,
    binary_waveform,
    where="post"
)

plt.title("Original Binary Data Sequence")
plt.xlabel("Time in Bit Periods")
plt.ylabel("Binary Level")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.xlim(0, number_of_bits)
plt.grid()


# ------------------------------------------------------------
# 2. BPSK-modulated signal
# ------------------------------------------------------------

plt.subplot(7, 1, 2)

plt.plot(
    time[:display_samples],
    bpsk_signal[:display_samples]
)

plt.title(
    f"BPSK-Modulated Signal — First {display_bits} Bits"
)

plt.xlabel("Time in Bit Periods")
plt.ylabel("Amplitude")
plt.xlim(0, display_bits)
plt.grid()


# ------------------------------------------------------------
# 3. PN-selected hopping-frequency sequence
# ------------------------------------------------------------

plt.subplot(7, 1, 3)

plt.step(
    time,
    frequency_sequence_waveform,
    where="post"
)

plt.title("PN-Controlled Hopping-Frequency Sequence")
plt.xlabel("Time in Bit Periods")
plt.ylabel("Cycles per Bit")
plt.xlim(0, number_of_bits)
plt.grid()


# ------------------------------------------------------------
# 4. Seven-frequency spreading carrier
# ------------------------------------------------------------

plt.subplot(7, 1, 4)

plt.plot(
    time[:display_samples],
    hopping_carrier[:display_samples]
)

plt.title(
    f"Frequency-Hopping Carrier — First {display_bits} Bits"
)

plt.xlabel("Time in Bit Periods")
plt.ylabel("Amplitude")
plt.xlim(0, display_bits)
plt.grid()


# ------------------------------------------------------------
# 5. Frequency Hopping Spread Spectrum signal
# ------------------------------------------------------------

plt.subplot(7, 1, 5)

plt.plot(
    time[:display_samples],
    fhss_signal[:display_samples]
)

plt.title(
    f"FHSS Signal — First {display_bits} Bits"
)

plt.xlabel("Time in Bit Periods")
plt.ylabel("Amplitude")
plt.xlim(0, display_bits)
plt.grid()


# ------------------------------------------------------------
# 6. Dehopped signal
# ------------------------------------------------------------

plt.subplot(7, 1, 6)

plt.plot(
    time[:display_samples],
    dehopped_signal[:display_samples]
)

plt.title(
    f"Dehopped BPSK Signal — First {display_bits} Bits"
)

plt.xlabel("Time in Bit Periods")
plt.ylabel("Amplitude")
plt.xlim(0, display_bits)
plt.grid()


# ------------------------------------------------------------
# 7. Recovered binary sequence
# ------------------------------------------------------------

plt.subplot(7, 1, 7)

plt.step(
    time,
    recovered_binary_waveform,
    where="post"
)

plt.title(
    "Recovered Binary Data "
    f"(Bit Errors = {bit_errors}, BER = {bit_error_rate:.4f})"
)

plt.xlabel("Time in Bit Periods")
plt.ylabel("Binary Level")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.xlim(0, number_of_bits)
plt.grid()


plt.suptitle(
    "Frequency Hopping Spread Spectrum",
    fontsize=18,
    y=1.01
)

plt.tight_layout()
plt.show()