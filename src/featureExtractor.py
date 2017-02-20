import essentia
from essentia.standard import *
import datetime

 # Load audio
fileName1 = 'A_ball_bounce_arcady_1.wav'
fileName2 = 'maxPatchRecording.wav'

# Load files using equal loudness loader
loader1 = EqloudLoader(filename = fileName1)
loader2 = EqloudLoader(filename = fileName2)

audio1 = loader1()
audio2 = loader2()

# Extract a bunch of descriptors
extractor = Extractor()
extractedData1 = extractor(audio1)
extractedData2 = extractor(audio2)

# dateTimeNow = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

# Write them to JSON files with a suitable name
YamlOutput(filename = fileName1.replace('.wav', '') + '_analysis.json', format = 'json')(extractedData1)
YamlOutput(filename = fileName2.replace('.wav', '') + '_analysis.json', format = 'json')(extractedData2)
