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

def plotList(listOfNumbers, title = ''):
	figure = plt.figure()
	colors = list("rgbcmyk")

	for index, value in enumerate(listOfNumbers):
		plt.scatter(index, value, color = colors.pop())

	plt.xlabel('Sample pair number')
	plt.title(title)

	return figure



pdfName = 'euclidianDistancePlots.pdf'
plotsPath = resultsDirectoryPath + 'plots/'

# Make directory for plots if needed
try:
	os.makedirs(plotsPath)
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

# Open a PDF file
pdf = PdfPages(plotsPath + pdfName)



print 'Plotting in PDF in ./analysisResults...\n'
for descriptorName in descriptors:
	descriptorSet = globals()[descriptorName]
	setType = type(descriptorSet[0])

	if setType is dict:
		fig = plotDictionary(descriptorSet, title = descriptorName + ' distances')

		# Save to PNG
		fig.savefig(plotsPath + descriptorName + '.png')

		# Save to PDF
		pdf.savefig(fig)



	elif setType is float:
		fig = plotList(descriptorSet, title = descriptorName + ' distances')

		# Save PNG
		fig.savefig(plotsPath + descriptorName + '.png')

		# Save PDF
		pdf.savefig(fig)

pdf.close()
print 'Done.\n\n'
