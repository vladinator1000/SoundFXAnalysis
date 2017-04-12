#
#
# Compares each A/B pair in ../analysisResults
# and writes a json file ../analysisResults/euclidianDistanceSets
# containing an array with euclidian distances for each pair in the order they were named
#
# e.g. [distance(A_1, B_1), distance(A_2, B_2), ...]
#

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
		if 'A_' in file:
			if 'aggregate' in file:
				aggregateFileNamesA.append(file)
				aggregateFilePathsA.append(os.path.join(resultsDirectoryPath, file))
			else:
				fileNamesA.append(file)
				filePathsA.append(os.path.join(resultsDirectoryPath, file))

		if 'B_' in file:
			if 'aggregate' in file:
				aggregateFileNamesB.append(file)
				aggregateFilePathsB.append(os.path.join(resultsDirectoryPath, file))
			else:
				fileNamesB.append(file)
				filePathsB.append(os.path.join(resultsDirectoryPath, file))


descriptorSetsA = []
aggregateDataSetsA = []

descriptorSetsB = []
aggregateDataSetsB = []


# Load descriptors from JSON files
for path in filePathsA:
	with open(path) as openedJson:
		descriptorSetsA.append(json.load(openedJson))

for path in aggregateFilePathsA:
	with open(path) as openedJson:
		aggregateDataSetsA.append(json.load(openedJson))

for path in filePathsB:
	with open(path) as openedJson:
		descriptorSetsB.append(json.load(openedJson))

for path in aggregateFilePathsB:
	with open(path) as openedJson:
		aggregateDataSetsB.append(json.load(openedJson))



# Only use SFX descriptors
sfxAggregateDescriptorSetsA = []
sfxAggregateDescriptorSetsB = []
euclidianDistanceSets = []

for set in aggregateDataSetsA:
	sfxAggregateDescriptorSetsA.append(set['sfx'])

for set in aggregateDataSetsB:
	sfxAggregateDescriptorSetsB.append(set['sfx'])


# Calculate euclidian distance for each aggregated descriptor set per pair
# https://en.wikipedia.org/wiki/Euclidean_distance
# http://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
print 'Getting Euclidian distance for each parameter...\n'
for index, set in enumerate(sfxAggregateDescriptorSetsA):
	distanceSet = dict()
	for (tupleA, tupleB) in zip(sfxAggregateDescriptorSetsA[index].iteritems(), sfxAggregateDescriptorSetsB[index].iteritems()):
		propertyName = tupleA[0]

		if type(tupleA[1]) is dict:
			# print propertyName + ' Euclidian distances:'

			# Create nested dictionary for mean, max, min, etc...
			distanceSet[propertyName] = dict()
			for key in tupleA[1]:
				distance = numpy.linalg.norm(numpy.array(tupleA[1][key]) - numpy.array(tupleB[1][key]))
				distanceSet[propertyName][key] = distance
				# print key, distance

		else:
			distanceSet[propertyName] = distance
			# print propertyName, numpy.linalg.norm(tupleA[1] - tupleB[1])

		# print '\n'
	# # Append set to big one for
	euclidianDistanceSets.append(distanceSet)


# Write distances to json in the ../analysisResults folder
with open(resultsDirectoryPath + 'euclidianDistanceSets.json', 'w') as outFile:
	json.dump(euclidianDistanceSets, outFile, sort_keys = True, indent = 4)




# This was hard to learn but didn't use it at all...


# Flatten an dictionary recursively (retun only furthest nodes),
# like this: http://i.imgur.com/8XpvXMw.jpg
# doesn't work on aggregate sets, found that the hard way :(

def flatten(dictionary, accumulator = [], excludeKeys = []):
	for key, value in dictionary.iteritems():
		if isinstance(value, dict):
			flatten(value, accumulator, excludeKeys)
		elif key not in excludeKeys:
			accumulator.append({ key: value })
			# print '{0} : {1}'.format(key, value)

	return accumulator;
