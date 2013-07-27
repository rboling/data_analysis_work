import json
import csv
import sys
import math
import csv, re, cStringIO, codecs, HTMLParser

input2 = csv.reader(open("EV to EBITDA Data.csv"))
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

output = open("ev_to_ebitda.csv", "wb")
writer = UnicodeWriter(output)

for line in input2:
    print len(line)
    list_to_append = []
    list_to_append.append(line[0])
    print line[0]
    line.pop(0)
    line.pop(0)
    line.pop(0)
    line.pop(0)
    line.pop(0)
    line.pop(0)
    line_to_analyze = list(map(lambda x: float(x), line))    
    average = sum(line_to_analyze)/len(line_to_analyze)
    list_to_append.append(average)
    square_list = list(map(lambda x: x*x, line_to_analyze))
    stdev = math.sqrt(sum(square_list)/len(square_list) - average*average)
    list_to_append.append(stdev)

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