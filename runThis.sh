#!/usr/bin/env bash
python2.7 ./src/analyseAudioFiles.py &&
python2.7 ./src/getDistances.py &&
python2.7 ./src/plotDistances.py
