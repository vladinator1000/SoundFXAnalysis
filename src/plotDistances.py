import matplotlib.pyplot as plt
import json, os, numpy

from pylab import plot, show, figure, imshow
from matplotlib.backends.backend_pdf import PdfPages


# Load analysis results
euclidianDistanceSets =[]

resultsDirectoryPath = os.path.dirname(os.path.realpath(__file__)) + '/../analysisResults/'
with open(resultsDirectoryPath + 'euclidianDistanceSets.json') as openedJson:
	euclidianDistanceSets = json.load(openedJson)


descriptors = euclidianDistanceSets[0].keys()

# Create variable for each descriptor
for descriptor in descriptors:
	if descriptor not in globals():
		globals()[descriptor] = []

for set in euclidianDistanceSets:
	for key, value in set.items():
		globals()[key].append(value)


# Define a couple of functions for plotting a dictionary and a list
def plotDictionary(descriptorSet, title = ''):
	figure = plt.figure()
	colors = list("rgbcmyk")

	for index, dictionary in enumerate(descriptorSet):
		x = range(len(dictionary.keys()))
		y = dictionary.values()

		plt.xticks(x, dictionary.keys())
		plt.scatter(x, y, color = colors.pop())

	# Prepare legend, e.g. 1, 2, 3, 4 ...
	legendList = range(len(descriptorSet) + 1)
	del legendList[0]

	plt.legend(legendList, title = 'Sample Pairs')
	plt.title(title)

	return figure
#
def plotList(listOfNumbers, title = ''):
	figure = plt.figure()
	colors = list("rgbcmyk")

	for index, value in enumerate(listOfNumbers):
		plt.scatter(index, value, color = colors.pop())

	plt.xlabel('Sample pair number')
	plt.title(title)

	return figure


# Open a PDF file
pdfName = 'euclidianDistancePlots.pdf'
pdfPath = resultsDirectoryPath + pdfName
pdf = PdfPages(pdfPath)

print 'Plotting in PDF in ./analysisResults...\n'
for descriptorName in descriptors:
	descriptorSet = globals()[descriptorName]
	setType = type(descriptorSet[0])

	if setType is dict:
		pdf.savefig(plotDictionary(descriptorSet, title = descriptorName + ' distances'))

	elif setType is float:
		pdf.savefig(plotList(descriptorSet, title = descriptorName + ' distances'))

pdf.close()
print 'Done.\n\n'
