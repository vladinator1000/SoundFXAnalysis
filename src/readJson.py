import json, os
from pprint import pprint


fileNames = []
filePaths = []
aggregateFileNames = []
aggregateFilePaths = []

# Get the names and paths of all files in the results folder
resultsDirectoryPath = os.path.dirname(os.path.realpath(__file__)) + '/../analysisResults/'

for file in os.listdir(resultsDirectoryPath):
	if file.endswith('.json'):
		if 'aggregate' in file:
			aggregateFileNames.append(file)
			aggregateFilePaths.append(os.path.join(resultsDirectoryPath, file))
		else:
			fileNames.append(file)
			filePaths.append(os.path.join(resultsDirectoryPath, file))


dataSets = []
aggregatedDataSets = []

for path in filePaths:
	with open(path) as openedJson:
		dataSets.append(json.load(openedJson))

for path in aggregatedFilePaths:
	with open(path) as openedJson:
		aggregatedDataSets.append(json.load(openedJson))


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


# Flatten the tree and load it into an array for all data sets
flatDataSets = []
for set in dataSets:
	flatDataSets.append([flatten(set, excludeKeys = ['essentia'])])

flatAggregatedDataSets = []
for aggregatedSet in aggregatedDataSets:
	flatAggregatedDataSets.append([flatten(aggregatedSet, excludeKeys = ['essentia'])])


for set in flatDataSets:
	for key in set:
		pprint(key)
