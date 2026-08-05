# 📡 Telecommunication Laboratory

This repository contains practical implementations, simulations, and laboratory experiments developed as part of the course:

**ICT-4206 – Telecommunication Laboratory**

---

# 📘 Course Overview

The **Telecommunication Laboratory** focuses on the practical implementation and analysis of analog and digital communication systems. The experiments are designed to strengthen theoretical concepts through simulation, signal processing, modulation techniques, and communication system analysis.

The course bridges communication theory with practical programming and simulation tools, enabling students to understand how information is generated, transmitted, received, and reconstructed in modern telecommunication systems.

## Key Topics Covered

- Signal generation and analysis
- Analog modulation techniques
- Digital modulation techniques
- Pulse modulation
- Sampling theorem
- PCM encoding and decoding
- Delta Modulation (DM)
- Adaptive Delta Modulation (ADM)
- Noise analysis in communication systems
- Time and frequency domain analysis
- Communication system simulation

---

# 🧪 Laboratory Experiments & Roadmap

Below is the status of the experiments mapped to this course. You can access completed implementations directly using the file links below, or use the [How to Add a New Experiment](#-how-to-add-a-new-experiment) guide to add new experiments.

| Exp No. | Experiment Title | Status | Python Code | Jupyter Notebook |
| :---: | :--- | :---: | :---: | :---: |
| **1** | **Pulse Code Modulation (PCM)** | 🟢 Completed | [Exp1_PCM.py](file:///Users/macbookair/Desktop/Disk%20Sajjad/IU%20ICT%202020-21/Academic%20Files/4th%20Year%202nd%20Semester/ICT-4206%20Telecommunication%20Laboratory/LabCodes/Exp1_PCM.py) | [Exp1_PCM.ipynb](file:///Users/macbookair/Desktop/Disk%20Sajjad/IU%20ICT%202020-21/Academic%20Files/4th%20Year%202nd%20Semester/ICT-4206%20Telecommunication%20Laboratory/LabCodes/Exp1_PCM.ipynb) |
| **2** | **Signal Generation and Analysis** | ⚪ Planned | — | — |
| **3** | **Sampling and Reconstruction** | ⚪ Planned | — | — |
| **4** | **Delta Modulation (DM)** | ⚪ Planned | — | — |
| **5** | **Adaptive Delta Modulation (ADM)** | ⚪ Planned | — | — |
| **6** | **Analog Modulation Techniques** | ⚪ Planned | — | — |
| **7** | **Digital Communication Experiments** | ⚪ Planned | — | — |
| **8** | **Communication System Performance Analysis** | ⚪ Planned | — | — |

---

# 📂 Repository Structure

```
LabCodes/
├── .gitignore
├── LICENSE
├── NOTICE
├── README.md
├── Exp1_PCM.py          # Python implementation of Pulse Code Modulation
├── Exp1_PCM.ipynb       # Jupyter Notebook for Pulse Code Modulation simulation
└── Exp1_PCM.png         # Waveform visualization plot for PCM
```

---

# ➕ How to Add a New Experiment

Follow these structured steps to add a new laboratory experiment to this repository:

### 1️⃣ File Naming Convention
Save your new code files in the root directory using the following names:
* **Python Script:** `Exp[Number]_[ShortName].py` (e.g., `Exp2_Sampling.py`)
* **Jupyter Notebook:** `Exp[Number]_[ShortName].ipynb` (e.g., `Exp2_Sampling.ipynb`)

### 2️⃣ Recommended Code Template
To keep the codebase uniform, use this standard structure for Python experiment scripts:

```python
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Signal Parameters ---
a = 4          # Amplitude
fm = 2         # Message Frequency (Hz)
fs = 100 * fm  # Sampling Frequency (Hz)

# --- 2. Signal Generation ---
t = np.arange(0, 1 + 1/fs, 1/fs)
x = a * np.sin(2 * np.pi * fm * t)

# --- 3. Processing / Simulation Logic ---
# (Implement modulation, filtering, or transmission simulation here)

# --- 4. Plotting Results ---
plt.figure(figsize=(10, 6))
plt.plot(t, x)
plt.title("Message Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
```

### 3️⃣ Update the Roadmap Table
After committing your new files, update the **[Laboratory Experiments & Roadmap](#-laboratory-experiments--roadmap)** section of this README:
1. Change the Status of the experiment from `⚪ Planned` to `🟢 Completed`.
2. Link the Python and Jupyter files in the table using Markdown:
   ```markdown
   [Exp2_Sampling.py](file:///Users/macbookair/Desktop/Disk%20Sajjad/IU%20ICT%202020-21/Academic%20Files/4th%20Year%202nd%20Semester/ICT-4206%20Telecommunication%20Laboratory/LabCodes/Exp2_Sampling.py)
   ```

---

# ⚙️ Tools & Technologies

- **Python 3**
- **Jupyter Notebook**
- **MATLAB**
- **NumPy**
- **Matplotlib**
- **SciPy** (optional)

---

# 🚀 How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/SajjadHossainSoykot/ICT-4206-Telecommunication-Laboratory.git
cd ICT-4206-Telecommunication-Laboratory
```

---

## ▶️ Run Python Code

### (Optional) Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Required Libraries

```bash
pip install numpy matplotlib scipy
```

### Run Python Scripts

```bash
python filename.py
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

---

## ▶️ Run MATLAB Code

1. Open MATLAB
2. Navigate to the project directory
3. Open any `.m` file
4. Click **Run** or execute the script from the command window

---

# ⚖️ License

This project is licensed under the **Apache License 2.0**.

You are free to use, modify, and distribute this project under the terms of the license.

You **must**:

- Retain the [LICENSE](file:///Users/macbookair/Desktop/Disk%20Sajjad/IU%20ICT%202020-21/Academic%20Files/4th%20Year%202nd%20Semester/ICT-4206%20Telecommunication%20Laboratory/LabCodes/LICENSE) file
- Retain the [NOTICE](file:///Users/macbookair/Desktop/Disk%20Sajjad/IU%20ICT%202020-21/Academic%20Files/4th%20Year%202nd%20Semester/ICT-4206%20Telecommunication%20Laboratory/LabCodes/NOTICE) file
- Provide proper attribution to the original author

Failure to comply with these terms violates the license.

If you use this project, please provide visible attribution to the original repository.

> https://github.com/SajjadHossainSoykot/ICT-4206-Telecommunication-Laboratory

---

# ⚠️ Academic Disclaimer

This repository has been created **strictly for educational and academic purposes**.

- All implementations follow standard telecommunication engineering principles.
- The simulations are intended to support laboratory learning and experimentation.
- The project was developed with the assistance of AI tools (including ChatGPT) for learning, implementation, debugging, and documentation.
- Theoretical concepts are based on:
  - Course lecture materials
  - Standard telecommunication textbooks
  - Official laboratory manuals

> All external resources remain the intellectual property of their respective authors.

---

# 🚫 Usage Notice

This repository is intended for:

- Academic learning
- Laboratory experiments
- Research and self-study
- Conceptual understanding of telecommunication systems

It is **not intended for production or commercial communication system deployment**, and simulation results may differ from real-world hardware implementations.

---

# 🤝 Acknowledgment

Special thanks to:

- Course instructors
- Department of Information and Communication Technology
- Islamic University, Bangladesh
- Standard telecommunication textbooks and laboratory manuals
- The open-source Python and MATLAB communities
- AI tools for assisting with implementation, debugging, and documentation

---

# 📌 Note

Telecommunication technologies form the backbone of modern digital communication systems. Understanding signal processing, modulation, transmission, and system analysis is essential for designing reliable and efficient communication networks.

Use this repository responsibly for learning, experimentation, and academic development.