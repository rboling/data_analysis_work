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


input1 = csv.reader(open("master workbook.csv"))
points_to_check = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]
a = 0
output = open("dow_30_refined_list_take_eight.csv","wb")
writer = UnicodeWriter(output)
for line in input1:
    if line[0] != "Ticker" and line[0] != "EV TO T12M EBITDA" and line[0] != None and line[0] != "EV TO T12M EBIT":
        remove_empty_strings = filter(lambda x: len(x) > 0, line)
        if len(remove_empty_strings) > 0: 
            if remove_empty_strings[0] in points_to_check: 
                list_to_append = []
                list_to_append.append(remove_empty_strings[0])
                #print remove_empty_strings
                remove_empty_strings.pop(0)
                remove_empty_strings.pop(0)
                remove_empty_strings.pop(0)
                #print remove_empty_strings
                line_to_analyze = list(map(lambda x: float(x), remove_empty_strings))
                list_to_append.append(line_to_analyze[0])
                list_to_append.append(line_to_analyze[1])
                list_to_append.append(line_to_analyze[2])
                list_to_append.append(line_to_analyze[3])
                list_to_append.append(line_to_analyze[4])
                volume = float(line_to_analyze[5])/float(1000)
                list_to_append.append(volume)
                list_to_append.append(line_to_analyze[6])
                list_to_append.append(line_to_analyze[7])
                list_to_append.append(remove_empty_strings[8])
                list_to_append.append(line_to_analyze[9])
                list_to_append.append(line_to_analyze[10])
                list_to_append.append(line_to_analyze[11])
                list_to_append.append(line_to_analyze[12])
                list_to_append.append(float(line[15]))

                writer.writerow(list_to_append)

    #print len(line)
    #list_to_append = []
    #list_to_append.append(line[0])
    #list_to_append.append(float(line[1]));
    #dict2['points'].append(list_to_append) 

#sys.stdout = saved
#print json.dumps(dict2)
#sys.stdout = saved
output.close()
