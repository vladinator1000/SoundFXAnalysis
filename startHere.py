import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt

 # Load audio
loader = MonoLoader(filename='/Users/vlady/Music/Logic/bombBall/Bounces/A_bomb_blow_B_3.wav')
audio = loader()

windowing = Windowing(type = 'hann')
spectrum = Spectrum()
mfcc = MFCC()

pool = essentia.Pool()
mfccs = []
melbands = []

# Get frames from audio and do something to each frame
for frame in FrameGenerator(audio, frameSize = 1024, hopSize = 512, startFromZero = True):
	mfcc_bands, mfcc_coeffs = mfcc(spectrum(windowing(frame)))
	pool.add('lowlevel.mfcc', mfcc_coeffs)
	pool.add('lowlevel.mfcc_bands', mfcc_bands)

# Write JSON file
YamlOutput(filename = 'mfcc.json', format = 'json')(pool)
