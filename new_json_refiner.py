import json
import csv
import sys
input2 = csv.reader(open("mean_output.csv"))
output = file('stock_mean_stdev_eight.json', 'wb')
#saved = sys.stdout
sys.stdout = output
saved = sys.stdout
#sys.stdout = output
#fields = input2.next()
#print "these are the fields\n"
#print fields
dict2 = {}
dict2["name"] = "industries"
#dict2['children'] = []
industry_dict = {}
industry_dict_check = {}
industry_dict_list = []

for line in input2:
#	print "this is the line\n"$
#	print line
#	print "line_as_zip\n"
#	print zip(fields, line)
	if line[0] != "Ticker":
		if line[1] in industry_dict_check:			
			new_dict = {}
			new_dict["ticker"] = line[0]
			new_dict["mean"] = line[3]
			new_dict["stdev"] = line[4]
			for sector in industry_dict_list:
				if sector["name"] == line[1]:
					sector["children"].append(new_dict)
		else:
			industry_dict_check[line[1]] = 1
			new_sector = {}
			new_sector["name"] = line[1]
			new_sector["children"] = []
			industry_dict_list.append(new_sector)
			new_dict = {}
			new_dict["ticker"] = line[0]
			new_dict["mean"] = line[3]
			new_dict["stdev"] = line[4]
			for sector in industry_dict_list:
				if sector["name"] == line[1]:
					sector["children"].append(new_dict)

dict2["children"] = industry_dict_list

#sys.stdout = saved
print json.dumps(dict2)
sys.stdout = saved
output.close()
#print len(dict2["points"])
#print "a"
#print a
#print "b"
#print b
#print "the file has been written\n"