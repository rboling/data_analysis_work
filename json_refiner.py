import json
import csv
import sys
input2 = csv.reader(open("literacy_rates.csv"))
output = file('real_literacy_rates.json', 'wb')
#saved = sys.stdout
#sys.stdout = output
saved = sys.stdout
sys.stdout = output
dict2 = {}
dict2['data'] = 'literacy rates'
dict2['points'] = []

for line in input2:
	list_to_append = []
	list_to_append.append(line[0])
	list_to_append.append(line[1])
	dict2['points'].append(list_to_append) 
print json.dumps(dict2)
sys.stdout = saved
output.close()
