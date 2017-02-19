import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt
import numpy

 # Load audio
fileName = 'A_ball_bounce_arcady_1.wav'
loader = MonoLoader(filename = fileName)
audio = loader()

#
windowing = Windowing()
spectrum = Spectrum()

frames = []

# Get frames from audio and do something to each frame
for frame in FrameGenerator(audio, frameSize = 1024, hopSize = 512, startFromZero = True):
	frames.append(frame)

# Get spectrogram for each frame
spectrogram = numpy.array([spectrum(windowing(frame)) for frame in frames])

# Transpose and plot the spectrogram (otherwise it would appear flipped)
plt.imshow(spectrogram.T, origin='lower', aspect='auto', interpolation='nearest')
plt.ylabel('Spectral Bin Index')
plt.xlabel('Frame Index')

# Limit axis for easier readability
axes = plt.gca()
# axes.set_xlim([xmin, xmax])
axes.set_ylim([0, 100])

show()
