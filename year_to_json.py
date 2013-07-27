import json
import csv
import sys
#input2 = csv.reader(open("pb_1998_refined.csv"))
#output = file('pb_1998_json.json', 'wb')
points_to_check = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]
year_list = ["1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013"]
sector_types = ["div_yield"]
#saved = sys.stdout
#sys.stdout = output
year_fitter = ["Test",0,0,0,0,0,0,0,0,700,0,0,0,0]
max_year = ["test1", 6, 50, 3, 0,0,100000, 15, 100, 800, 0, 15, 0, 15]
min_year = ["test2", 0, 0, 0, 0,0,0, 0, -10, 900, 0, 0, 0, 0]
for year in year_list:
	input3 = year
	input4 = input3 + ".csv" 
	input2 = csv.reader(open(input4))
	output2 = input3 + "_" + "json_twelve" + ".json"
	output = file(output2,'wb')
	saved = sys.stdout
	sys.stdout = output
	dict2 = {}
	dict2["points"] = []
	dict2["points"].append(year_fitter)
	dict2["points"].append(max_year)
	dict2["points"].append(min_year)
	for line in input2:
		list_to_append = []
		for i in range(14):			
			list_to_append.append(line[i])
		dict2["points"].append(list_to_append)
	print json.dumps(dict2)
	sys.stdout = saved
	output.close()
	print "the file has been written\n"