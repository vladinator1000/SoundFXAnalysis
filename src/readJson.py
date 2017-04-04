import json, os, numpy

from pprint import pprint

# Compare pairs of sounds, each pair must have an A and B sample
fileNamesA = []
filePathsA = []
aggregateFileNamesA = []
aggregateFilePathsA = []

fileNamesB = []
filePathsB = []
aggregateFileNamesB = []
aggregateFilePathsB = []

# Get the names and paths of all files in the results folder
resultsDirectoryPath = os.path.dirname(os.path.realpath(__file__)) + '/../analysisResults/'

for file in os.listdir(resultsDirectoryPath):
	if file.endswith('.json'):
		if 'A' in file:
			if 'aggregate' in file:
				aggregateFileNamesA.append(file)
				aggregateFilePathsA.append(os.path.join(resultsDirectoryPath, file))
			else:
				fileNamesA.append(file)
				filePathsA.append(os.path.join(resultsDirectoryPath, file))

		if 'B' in file:
			if 'aggregate' in file:
				aggregateFileNamesB.append(file)
				aggregateFilePathsB.append(os.path.join(resultsDirectoryPath, file))
			else:
				fileNamesB.append(file)
				filePathsB.append(os.path.join(resultsDirectoryPath, file))



dataSetsA = []
aggregateDataSetsA = []

dataSetsB = []
aggregateDataSetsB = []

for path in filePathsA:
	with open(path) as openedJson:
		dataSetsA.append(json.load(openedJson))

for path in aggregateFilePathsA:
	with open(path) as openedJson:
		aggregateDataSetsA.append(json.load(openedJson))

for path in filePathsB:
	with open(path) as openedJson:
		dataSetsB.append(json.load(openedJson))

for path in aggregateFilePathsB:
	with open(path) as openedJson:
		aggregateDataSetsB.append(json.load(openedJson))



# Only use SFX descriptors
sfxDescriptorSetsA = []
sfxDescriptorSetsB = []
results = []

for dict in dataSetsA:
	sfxDescriptorSetsA.append(dict['sfx'])

for dict in dataSetsB:
	sfxDescriptorSetsB.append(dict['sfx'])

for index, dict in enumerate(sfxDescriptorSetsA):
	for (tupleA, tupleB) in zip(sfxDescriptorSetsA[index].iteritems(), sfxDescriptorSetsB[index].iteritems()):
		print tupleA, tupleB






# Flatten an dictionary recursively (retun only furthest nodes)
# like this: http://i.imgur.com/8XpvXMw.jpg
def flatten(dictionary, accumulator = [], excludeKeys = []):
	for key, value in dictionary.iteritems():
		if isinstance(value, dict):
			flatten(value, accumulator, excludeKeys)
		elif key not in excludeKeys:
			accumulator.append({ key: value })
			# print '{0} : {1}'.format(key, value)

	return accumulator;
