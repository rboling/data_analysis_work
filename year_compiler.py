#year compiler
#order
#0 - ticker
#1 - price
#2 - pe
#13 - div yield
#pb - 11
#ev to ebit - 12
#ev to ebitda - 10
#volume - 6
#wacc - 7
#return_on_eq = 8
# beta - 3
#id = 9
#4,5 - filler
import json
import csv
import sys
import math
import csv, re, cStringIO, codecs, HTMLParser

#input2 = csv.reader(open("pb_2013.csv"))
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
       # self.writer.writerow([s.encode("utf-8") for s in row])
        self.writer.writerow([s for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
input011 = []
input22 = []
input33 = []
input66 = []
input77 = []
input88 = []
input1010 = []
input1111 = []
input1212 = []
input1313 = []
input1414 = []
year = "2013"
input14 = csv.reader(open("id_list.csv"))
for line in input14:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input1414.append(line_append)
input1a = "price_" + year + "_refined_six.csv"
input1 = csv.reader(open(input1a))
for line in input1:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input011.append(line_append)
input2a = "pe_" + year + "_refined_six.csv"
input2 = csv.reader(open(input2a))
for line in input2:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input22.append(line_append)
input3a = "beta" + year + "_refined_six.csv"
input3 = csv.reader(open(input3a))
for line in input3:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input33.append(line_append)
input6a = "volume_" + year + "_refined_six.csv"
input6 = csv.reader(open(input6a))
for line in input6:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input66.append(line_append)
input7a = "wacc_" + year + "_refined_six.csv"
input7 = csv.reader(open(input7a))
for line in input7:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input77.append(line_append)
input8a = "return_on_eq_" + year + "_refined_six.csv"
input8 = csv.reader(open(input8a))
for line in input8:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input88.append(line_append)
#input10 = csv.reader(open("ev_to_ebitda_1998_refined.csv"))
#for line in input10:
#	line_append = []
#	for i in range(len(line)):
#		line_append.append(line[i])
#	input1010.append(line_append)
input11a = "pb_" + year + "_refined.csv"
input11 = csv.reader(open(input11a))
for line in input11:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input1111.append(line_append)
#input12 = csv.reader(open("ev_to_ebit_1998_refined.csv"))
#for line in input12:
#	line_append = []
#	for i in range(len(line)):
#		line_append.append(line[i])
#	input1212.append(line_append)
input13a = "div_yield_" + year + "_refined.csv"
input13 = csv.reader(open(input13a))
for line in input13:
	line_append = []
	for i in range(len(line)):
		line_append.append(line[i])
	input1313.append(line_append)
output1a = year + ".csv"
output = open(output1a,"wb")
writer = UnicodeWriter(output)
index_ticker = 0
points_to_check = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]
a = 0
for number in range(30):
	id_string = float(input1414[number][1])
	the_id = int(id_string)
	if input011[number][0] in points_to_check:
		print the_id
		a += 1
		list_to_append = []
		list_to_append.append(input011[number][0])
		list_to_append.append(input011[number][1])
		list_to_append.append(input22[number][1])
		list_to_append.append(input33[number][1])
		list_to_append.append(the_id)
		list_to_append.append(the_id)
		volume_fixed = float(input66[number][1])/float(1000)
		list_to_append.append(volume_fixed)
		list_to_append.append(input77[number][1])
		list_to_append.append(input88[number][1])
		list_to_append.append(the_id)
		#list_to_append.append(input1010[number][1])
		list_to_append.append(the_id)
		list_to_append.append(input1111[number][1])
		#list_to_append.append(input1212[number][1])
		list_to_append.append(the_id)
		list_to_append.append(input1313[number][1])
		writer.writerow(list_to_append)
    
print a
    #print len(line)
    #list_to_append = []
    #list_to_append.append(line[0])
    #list_to_append.append(float(line[1]));
    #dict2['points'].append(list_to_append) 

#sys.stdout = saved
#print json.dumps(dict2)
#sys.stdout = saved
output.close()
