import json
import csv
import sys
input2 = csv.reader(open("dow_30_refined_list_take_eight.csv"))
output = file('project_3_dow_30_take_eleven.json', 'wb')
list_of_tickers = []
#saved = sys.stdout
#sys.stdout = output
saved = sys.stdout
sys.stdout = output
dict2 = {}
#dict2["points"] = []
points_to_check = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]

for line in input2:
#	print "this is the line\n"$
#	print line
#	print "line_as_zip\n"
#	print zip(fields, line)
	if line[0] != "Ticker":
		if line[0] in points_to_check:
			list_to_append = []
			list_to_append.append(line[0])
			list_to_append.append(float(line[1]))
			list_to_append.append(float(line[2]))
			list_to_append.append(float(line[3]))
			list_to_append.append(float(line[4]))
			list_to_append.append(float(line[5]))
			volume = float(line[6])
			list_to_append.append(volume)
			list_to_append.append(float(line[7]))
			list_to_append.append(float(line[8]))
			list_to_append.append(int(line[9]))
			list_to_append.append(float(line[10]))
			list_to_append.append(float(line[11]))
			list_to_append.append(float(line[12]))
			list_to_append.append(float(line[13]))
			#list_to_append.append(float(line[14]))


			dict2[str(line[9])] = list_to_append

	#print "the lines\n"
	#print list_to_append
	#dict2['points'].append(list_to_append) 

#sys.stdout = saved
print json.dumps(dict2)
sys.stdout = saved
output.close()
print "the file has been written\n"