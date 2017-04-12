# SoundFXAnalysis
Compares two sets of sound effects samples with the [Essentia](http://essentia.upf.edu/documentation/) library in Python 2.7. Only works on Mac OS

## Setup Guide

If you don't have Homebrew installed, go here https://brew.sh/ and install it.

###1. Install essentia:
Install homebrew tap:
```
brew tap MTG/essentia
```

Install compiling the code for the latest official release of Essentia
```
brew install essentia
```

###Add audio files
2. Place two sets of `.aif` audio files in the audio folder, each file from first group containing `A_` and from the second `B_` in their name
`A_1` and `B_1`, `A_2` and `B_2` etc. will be considered pairs. If you want another format, edit the file extension in `./src/analyseAudioFiles`.

###Run the scripts
3. Cd to the project directory and run this shell script
```
sh runThis.sh
```



Samples A_ were made with the granular HonoursMaxPatch, samples B_ were made in a DAW with the Serum synth.
