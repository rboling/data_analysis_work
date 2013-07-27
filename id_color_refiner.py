import json
import csv
import sys
points_to_check = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]
input2 = csv.reader(open("1998.csv"))
output = file('id_list_again.json', 'wb')
saved = sys.stdout
sys.stdout = output
dict2 = {}
dict2["points"] = []
for line in input2:
	if line[0] != "Ticker":
		list_to_use = []
		list_to_use.append(line[0])
		list_to_use.append(str(line[9]))
		dict2["points"].append(list_to_use)
print json.dumps(dict2)
sys.stdout = saved
output.close()
