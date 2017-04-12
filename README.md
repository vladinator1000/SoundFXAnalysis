# SoundFXAnalysis
Analyzing game sound effects with the Essentia library in Python. Only works on Mac OS

## Setup Guide

If you don't have Homebrew installed:
0. Go here https://brew.sh/ and install Homebrew

1. Install essentia:
Install homebrew tap:
```
brew tap MTG/essentia
```

Install compiling the code for the latest official release of Essentia
```
brew install essentia
```


2. Place two sets of files in the audio folder, each file from first group containing `A_` and from the second `B_` in their name
`A_1` and `B_1`, `A_2` and `B_2` etc. will be considered pairs

3. Cd to the project directory and run this shell script
```
sh runThis.sh
```
