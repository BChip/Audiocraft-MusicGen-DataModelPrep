# Description

This repo helps prepare your data model set for generating a custom model for Audiocraft/Music Gen.

I recommended using these helpful scripts and then heading over to https://github.com/chavinlo/musicgen_trainer and using those scripts to build your model to import into AudioCraft/MusicGen.

# Download Song Script

This script allows you to download a song from YouTube and convert it to .wav format. 

## Requirements

Install FFmpeg. The installation process varies depending on your operating system. You can find instructions for your specific OS on the [official FFmpeg website](https://ffmpeg.org/download.html).

Also run:

```bash
pip install -r requirements.txt
```

## Usage

You can use the script from the command line by providing the YouTube URL and the output directory as arguments:

```bash
python download_song.py <youtube url> <output directory>
```

For example:

```bash
python download_song.py https://www.youtube.com/watch?v=k4jDpkAWrdA out
```

If you run the script without any arguments, it will prompt you to enter the YouTube URL and the output directory:

```bash
python download_song.py
```

You should now have a directory with .wav file/s

### After downloading the .wav/s, you can now use split_song.py

```bash
python split_song.py <directory with .wav/s> <output directory>
```

For example:

```bash
python split_song.py out data_model
```

If you run the script without any arguments, it will prompt you to enter the directory with the .wavs and the output data_model directory:

```bash
python split_song.py
```

### You can now use https://github.com/chavinlo/musicgen_trainer to finish building the model
