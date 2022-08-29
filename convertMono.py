import os 
import librosa
import soundfile

dataset_path = "/home/n2202857e/Documents/Speaker_Embeddings-main/final_test_noisy"
newDataset_path = "/home/n2202857e/Documents/Speaker_Embeddings-main/final_test_noisy_mono"
sampling_rate = 16000

if not os.path.exists(newDataset_path):
    os.mkdir(newDataset_path)

for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)
    newCategory_path = os.path.join(newDataset_path, category)
    
    for audio_file in os.listdir(category_path):
        audiofile_path = os.path.join(category_path, audio_file)
        newAudiofile_path = os.path.join(newCategory_path, audio_file)

        audioData, samplerate = librosa.load(audiofile_path, mono = True, sr = sampling_rate)

        if not os.path.exists(newCategory_path):
            os.mkdir(newCategory_path)

        soundfile.write(newAudiofile_path, audioData, sampling_rate)