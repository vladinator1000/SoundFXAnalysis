# TODO compare results between different files and find distance

import datetime
import scipy.stats
import json
from pprint import pprint

with open('maxPatchRecording_aggregated_analysis.json') as data_file:
    data = json.load(data_file)


# dateTimeNow = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

# Iterate through object
for key in data:
    print key + ": "

    for keyDeeper in data[key]:
        print keyDeeper
    print
