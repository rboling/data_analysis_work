import json
import csv
import sys
import csv, re, cStringIO, codecs, HTMLParser

input2 = csv.reader(open("Price Data.csv"))
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

output = open("variance_output_with_sector_info.csv", "wb")
writer = UnicodeWriter(output)

#writer.writerow(["Movie Title", "Time", "Genre", "Directors", "Writers", "Actors", "Rating","Number of Ratings"])

#output = file('price_data.json', 'wb')
#saved = sys.stdout
#sys.stdout = output
#fields = input2.next()
#print "these are the fields\n"
#print fields
#dict2 = {}
#dict2['points'] = []

for line in input2:
    if len(line) > 2 and line[0] != "Ticker" and line[0] != "" and line[0] != "PX LAST":
        variance_list = []
        line_to_analyze = filter(lambda x: len(x) > 0, line)
        variance_list.append(line[0])
        variance_list.append(line[2])
        variance_list.append(line[3])
        for i in range(len(line_to_analyze) - 7):		
            daily_difference = float(abs(((float(line[7+i]) - float(line[6+i]))/float(line[6+i]))*100))
            variance_list.append(daily_difference)
            print daily_difference
            csv.writer(output).writerow(variance_list)

#sys.stdout = saved
#print json.dumps(dict2)
#sys.stdout = saved
output.close()
#print "the file has been written\n"