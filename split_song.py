import os
import subprocess
import sys

def chunk_wav(filepath):
    # Create a directory to store the chunks
    os.makedirs(out, exist_ok=True)
    # Get file and get filename set to variable
    filename = os.path.basename(filepath)
    # Use ffmpeg to split the song into 30 second chunks
    subprocess.run(["ffmpeg", "-i", filepath, "-f", "segment", "-segment_time", "30", "-c", "copy", out+"/out%03d-"+filename])

def create_txt_per_chunk(filepath, description):
    basename = os.path.basename(filepath)
    for filename in os.listdir(out):
        if filename.endswith(basename):
            f = open(out+"/" + filename[:-4] + ".txt", "w")
            f.write(description)
            f.close()



args = sys.argv[1:]
if len(args) > 2:
    print("Too many arguments.")
    print("Usage: python split_song.py <directory> <output directory>")
    print("Example: python split_song.py out model")
    exit()
if len(args) == 0:
    print("No directory given, please enter a directory to split")
    directory=input()
    print("No output directory given, please enter an output directory")
    out=input()
else:
    directory = args[0]
    out = args[1]



# get all .wav files in directory
for file in os.listdir(directory):
    if file.endswith(".wav"):
        # Get filepath of file
        filepath = os.path.join(directory, file)
        print("Found file", file)
        print("Splitting song into 30 second chunks", file)
        chunk_wav(filepath)
        # ask user for description about the song
        print("Please describe the song", file)
        description = input()
        create_txt_per_chunk(file, description)