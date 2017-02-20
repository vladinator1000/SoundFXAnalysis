import json
from pprint import pprint

with open('A_ball_bounce_arcady_1_analysis.json') as openedJson:
	data = json.load(openedJson)

pprint(data["sfx"])
