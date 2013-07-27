import json
import csv
import sys
input2 = csv.reader(open("refined_master_data.csv"))
output = file('sector_json_five.json', 'wb')
#saved = sys.stdout
#sys.stdout = output
saved = sys.stdout
sys.stdout = output
#fields = input2.next()
#print "these are the fields\n"
#print fields
dict2 = {}
dict2["name"] = "industries"
dict2['children'] = []
industry_dict = {}
a = 0
b = 0

for line in input2:
	b += 1
#	print "this is the line\n"$
#	print line
#	print "line_as_zip\n"
#	print zip(fields, line)
	if line[0] != "Ticker":
		if line[10] in industry_dict:
			industry_dict[line[10]].append(line[9])
		else:
			a += 1
			industry_dict[line[10]] = []
			industry_dict[line[10]].append(line[9])

#dict2['children'].append(industry_dict) 

#sys.stdout = saved
print json.dumps(industry_dict)
sys.stdout = saved
output.close()
print "a"
print a
print "b"
print b
print "the file has been written\n"