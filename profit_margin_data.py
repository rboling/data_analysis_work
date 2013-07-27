import json
import csv
import sys
import math
import csv, re, cStringIO, codecs, HTMLParser

input2 = csv.reader(open("Profit Margin Data.csv"))
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

output = open("profit_margin_output.csv", "wb")
writer = UnicodeWriter(output)

for line in input2:
    if line[0] != "Ticker" and line[0] != "PROF MARGIN" and len(line) > 0 and line[0] != "": 
        #line_to_analyze = filter(lambda x: len(x) > 0, line)
        list_to_append = []
        list_to_append.append(line[0])
        list_to_append.append(line[2])
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line.pop(0)
        #print line
        line_to_analyze = filter(lambda x: x != "", line)          
        line_to_analyze = list(map(lambda x: float(x), line_to_analyze))  
        #print line_to_analyze
        if len(line_to_analyze) > 0:
            average = sum(line_to_analyze)/len(line_to_analyze)
            list_to_append.append(average)
        else:
            average = 0
            list_to_append.append(average)
        writer.writerow(list_to_append)

output.close()