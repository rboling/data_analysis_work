import json
import csv
import sys
input2 = csv.reader(open("refined_master_data.csv"))
output = file('json_scatterplot_ultimate.json', 'wb')
list_of_tickers = []
#saved = sys.stdout
#sys.stdout = output
saved = sys.stdout
sys.stdout = output
dict2 = {}
dict2['points'] = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]

for line in input2:
#	print "this is the line\n"$
#	print line
#	print "line_as_zip\n"
#	print zip(fields, line)
	if line[0] != "Ticker":
		if float(line[8]) > -800:
			list_to_append = []
			list_to_append.append(line[0])
			list_to_append.append(float(line[1]))
			list_to_append.append(float(line[2]))
			list_to_append.append(float(line[3]))
			list_to_append.append(float(line[4]))
			list_to_append.append(float(line[5]))
			list_to_append.append(float(line[6]))
			list_to_append.append(float(line[7]))
			list_to_append.append(float(line[8]))
			list_to_append.append(int(line[9]))
			dict2['points'].append(list_to_append) 






	#print "the lines\n"
	#print list_to_append
	#dict2['points'].append(list_to_append) 

#sys.stdout = saved
print json.dumps(dict2)
sys.stdout = saved
output.close()
print "the file has been written\n"