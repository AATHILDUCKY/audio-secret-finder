import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from scipy import signal

# Load the audio file
def load_audio(filename):
    audio_data, sample_rate = librosa.load(filename, sr=None)
    return audio_data, sample_rate

# Generate a spectrogram
def generate_spectrogram(audio_data, sample_rate):
    # Compute the Short-Time Fourier Transform (STFT) of the audio signal
    frequencies, times, spectrogram = signal.spectrogram(audio_data, sample_rate)
    
    # Display the spectrogram
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title('Spectrogram')
    plt.colorbar(label='Decibels (dB)')
    plt.show()

# Main function to process the audio and display the spectrogram
def main():
    audio_file = 'your_audio_file_with_hidden_message.wav'  # Replace with your file
    audio_data, sample_rate = load_audio(audio_file)
    generate_spectrogram(audio_data, sample_rate)

if __name__ == "__main__":
    main()
