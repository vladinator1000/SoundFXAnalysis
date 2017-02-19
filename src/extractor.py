import essentia
from essentia.standard import *

 # Load audio
fileName = 'A_ball_bounce_arcady_1.wav'

loader = MonoLoader(filename = fileName)
audio = loader()

# Extract a bunch of descriptors
extractor = Extractor()
extractedData = extractor(audio)

# Write them to a JSON file with a suitable name
YamlOutput(filename = fileName.replace('.wav', '') + '_analysis.json', format = 'json')(extractedData)
