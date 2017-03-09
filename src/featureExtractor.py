# Gets all audio files in the root directory and outputs .json files with analysis data

import essentia
from essentia.standard import *
from pprint import pprint
import glob

# Get all file names with extension
fileExtension = '.wav'
fileNames = glob.glob('./*' + fileExtension)

# Load them
loadedAudioFiles = []

for fileName in fileNames:
	# Using audio loader of choice http://essentia.upf.edu/documentation/algorithms_overview.html#audio-input-output
	loader = EqloudLoader(filename = fileName)
	loadedAudioFiles.append(loader())


dataPools = []
dataPoolsAggregated = []
extractor = Extractor()

# Extract a bunch of features http://essentia.upf.edu/documentation/reference/std_Extractor.html
for audioFile in loadedAudioFiles:
	currentExtractor = extractor(audioFile)
	dataPools.append(currentExtractor)

	# Perform statistical aggregation http://essentia.upf.edu/documentation/reference/std_PoolAggregator.html
	# TODO add 'stdev' to defaultStats, currently getting error https://github.com/MTG/essentia/issues/570
	# A low standard deviation indicates that the data points tend to be close to the mean value
	dataPoolsAggregated.append(PoolAggregator(defaultStats = ["mean", "min", "max", "median", "stdev"])(currentExtractor))


# Output JSON
for index, dataPool in enumerate(dataPools):
	YamlOutput(filename = fileNames[index].replace('.wav', '') + '_analysis.json', format = 'json')(dataPool)

# Output aggregated JSON (mean values)
for index, aggregatedPool in enumerate(dataPoolsAggregated):
	YamlOutput(filename = fileNames[index].replace('.wav', '') + '_aggregated_analysis.json', format = 'json')(aggregatedPool)
