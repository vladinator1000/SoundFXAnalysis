import essentia, os, errno
from essentia.standard import *
from pprint import pprint


fileNames = []
filePaths = []
fileExtension = '.wav'

# Get the audio directory path
audioDirectoryPath = os.path.dirname(os.path.realpath(__file__)) + '/../audio/'

# Get the names and paths of all .wav files in the audio folder
for file in os.listdir(audioDirectoryPath):
	if file.endswith(fileExtension):
		fileNames.append(file)
		filePaths.append(os.path.join(audioDirectoryPath, file))

# Load them with equal loudness
loadedAudioFiles = []
for filePath in filePaths:
	# Using audio loader of choice http://essentia.upf.edu/documentation/algorithms_overview.html#audio-input-output
	loader = EqloudLoader(filename = filePath)
	loadedAudioFiles.append(loader())


dataPools = []
dataPoolsAggregated = []
extractor = Extractor()
#
# Extract a bunch of features http://essentia.upf.edu/documentation/reference/std_Extractor.html
for audioFile in loadedAudioFiles:
	currentExtractor = extractor(audioFile)
	dataPools.append(currentExtractor)

	# Perform statistical aggregation http://essentia.upf.edu/documentation/reference/std_PoolAggregator.html
	# TODO add 'stdev' to defaultStats, currently getting error https://github.com/MTG/essentia/issues/570
	# A low standard deviation indicates that the data points tend to be close to the mean value
	dataPoolsAggregated.append(PoolAggregator(defaultStats = ["mean", "min", "max", "median"])(currentExtractor))



# Create results directory if necessary
resultsDirectoryPath = os.path.dirname(os.path.realpath(__file__)) + '/../analysisResults/'

try:
	os.makedirs(resultsDirectoryPath)
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

# Map file names to result names using anonymous function
resultNames = map(lambda name: name.replace(fileExtension, '') + '_analysis.json', fileNames)
resultNamesAggregated = map(lambda name: name.replace(fileExtension, '') + '_analysis_aggregated.json', fileNames)

# Output JSON
for index, dataPool in enumerate(dataPools):
	YamlOutput(filename = resultsDirectoryPath + resultNames[index], format = 'json')(dataPool)

# Output aggregated JSON (mean values)
for index, aggregatedPool in enumerate(dataPoolsAggregated):
	YamlOutput(filename = resultsDirectoryPath + resultNamesAggregated[index], format = 'json')(aggregatedPool)
