import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def spectrogram(signal, n_fft, hop_length, win_length, sr):
    
    hop_length_duration = float(hop_length) / sr
    n_fft_duration = float(n_fft) / sr

    stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length, win_length=win_length)

    magnitude = np.abs(stft)

    log_spectrogram = librosa.amplitude_to_db(magnitude)

    plt.figure()
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram (dB)")
    

def show_signal(signal,signal2,signal_reconstructed,sr):
    plt.figure(figsize=(10,10))
    
    plt.subplot(3, 1, 1)
    librosa.display.waveshow(signal, sr=sr)
    plt.title('Clean Time Signal')

    plt.subplot(3, 1, 2)
    librosa.display.waveshow(signal2, sr=sr)
    plt.title('Noisy Time Signal')

    plt.subplot(3, 1, 3)
    librosa.display.waveshow(signal_reconstructed, sr=sr)
    plt.title('Reconstructed Clean Time Signal')
    
    
def show_spectrogram(signal,signal2,recnstrtSignal,sr, NFFT, hop_length):
    #Display power (energy-squared) spectrogram
    plt.figure(figsize=(10,10))
    
    plt.subplot(3, 1, 1)
    librosa.display.specshow(librosa.power_to_db(librosa.feature.melspectrogram(y=signal, sr=sr, n_fft=NFFT, hop_length=hop_length, win_length=NFFT),ref=np.max),sr=sr, x_axis='time', y_axis='linear')
    #librosa.display.specshow(librosa.amplitude_to_db(origianlSpectrogram, ref_power=np.max),sr=sr, x_axis='time',y_axis='linear')
    plt.title('Clean Spectrogram')
    plt.colorbar(format='%+02.0f dB')

    plt.subplot(3, 1, 2)
    librosa.display.specshow(librosa.power_to_db(librosa.feature.melspectrogram(y=signal2, sr=sr, n_fft=NFFT, hop_length=hop_length, win_length=NFFT),ref=np.max),sr=sr, x_axis='time', y_axis='linear')
    #librosa.display.specshow(librosa.amplitude_to_db(origianlSpectrogram, ref_power=np.max),sr=sr, x_axis='time',y_axis='linear')
    plt.title('Noisy Spectrogram')
    plt.colorbar(format='%+02.0f dB')
    
    plt.subplot(3, 1, 3)
    librosa.display.specshow(librosa.power_to_db(librosa.feature.melspectrogram(y=recnstrtSignal, sr=sr, n_fft=NFFT, hop_length=hop_length, win_length=NFFT),ref=np.max),sr=sr, x_axis='time', y_axis='linear')
    #librosa.display.specshow(librosa.amplitude_to_db(recnstrtSpectrogram, ref_power=np.max),sr=sr, x_axis='time', y_axis='linear')
    plt.title('Reconstructed Clean Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()