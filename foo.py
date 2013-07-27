import json
import csv
import sys
input2 = csv.reader(open("appl_data.csv"))
output = file('appl_data2.json', 'wb')
#saved = sys.stdout
#sys.stdout = output
saved = sys.stdout
sys.stdout = output
fields = input2.next()
print "these are the fields\n"
print fields
dict2 = {}
dict2['points'] = []

for line in input2:
#	print "this is the line\n"$
#	print line
#	print "line_as_zip\n"
#	print zip(fields, line)
	list_to_append = []
	list_to_append.append(line[0])
	list_to_append.append(float(line[1]));
	#print "the lines\n"
	#print list_to_append
	dict2['points'].append(list_to_append) 

#sys.stdout = saved
print json.dumps(dict2)
sys.stdout = saved
output.close()
print "the file has been written\n"