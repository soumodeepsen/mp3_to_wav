#!pip install librosa
#!pip install soundfile

import librosa
import soundfile as sf
import os
import warnings
warnings.simplefilter("ignore")


def mp3_to_wav(mp3_dir, wav_dir):
    
    # checks whether output dir exists
    # if not then creates one
    if not os.path.exists(wav_dir):
        os.mkdir(wav_dir)
    
    # iterates over list of files in mp3_dir
    for file in os.listdir(mp3_dir):
        
        # if filename consists of .mp3 extension
        if file.endswith(".mp3"):
            
            # loads mp3 file
            audio, sr = librosa.load(os.path.join(mp3_dir, file))
            
            # creates path for exporting .wav file
            wav_path = os.path.join(wav_dir, file[:-3]+"wav")
            
            # saves the .wav file
            sf.write(wav_path, audio_data, sr)
            print(f"Status: Successfully converted {file} to {file[:-3]}wav")
    
    return 

if __name__ == "__main__":
    
    # ENTER YOUR MP3 FILE'S FOLDER DIRECTORY
    mp3_dir = r"C:\Users\ACER\Desktop\Soumodeep\Learning\soundfolder" 
    
    # ENTER YOUR WAVE FILE'S FOLDER DIRECTORY
    wav_dir = r"C:\Users\ACER\Desktop\Soumodeep\Learning\soundfolder1"
    
    mp3_to_wav(mp3_dir, wav_dir)