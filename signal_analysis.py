import numpy as np
import matplotlib.pyplot as plt

# Generate time axis
t = np.linspace(0, 1, 1000)

# Generate a digital signal (square wave)
digital_signal = np.sign(np.sin(2 * np.pi * 5 * t))

# Add noise
noise = np.random.normal(0, 0.3, t.shape)
noisy_signal = digital_signal + noise

# Plot signals
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, digital_signal)
plt.title("Original Digital Signal")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, noise)
plt.title("Noise Signal")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, noisy_signal)
plt.title("Noisy Digital Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()