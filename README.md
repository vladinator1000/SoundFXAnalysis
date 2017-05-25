# SoundFXAnalysis
Compares two sets of sound effects samples with the [Essentia](http://essentia.upf.edu/documentation/) library in Python 2.7. Only works on Mac OS

Thesis: https://www.academia.edu/33058454/Bridging_the_Gap_Between_Procedural_and_Hand-Made_Sound_Effects

## Setup Guide

If you don't have Homebrew installed, go here https://brew.sh/ and install it.

### 1. Install essentia:
Install homebrew tap:
```
brew tap MTG/essentia
```

Install compiling the code for the latest official release of Essentia
```
brew install essentia
```

### 2. Add audio files
Place two sets of `.aif` audio files in the audio folder, each file from first group containing `A_` and from the second `B_` in their name
`A_1` and `B_1`, `A_2` and `B_2` etc. will be considered pairs. If you want another format, edit the file extension in `./src/analyseAudioFiles`.

### 3. Run the scripts
Cd to the project directory and run this shell script
```
sh runThis.sh
```
### 4. Look at results in `./analysisResults`
You will see data sets with extractor information and a plot folder with distances between each pair for each descriptor.
