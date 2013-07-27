import json
import csv
import sys
import csv, re, cStringIO, codecs, HTMLParser

input2 = csv.reader(open("wacc.csv"))
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

output = open("wacc_sector_info.csv", "wb")
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

def find_placement(input_thing):
    if float(input_thing) < 7.647731:
        return 1
    if  7.647731 <= float(input_thing) and float(input_thing) < 8.927521:
        return 2
    if 8.927521 <= float(input_thing) and float(input_thing) < 10.078831:
        return 3
    if 10.078831 <= float(input_thing):
        return 4
#############################

industry_dict = {}

for line in input2:
    if line[1] in industry_dict:
        industry_dict[line[1]][find_placement(line[2])] += 1
      #  print line[3]
      #  print find_placement(line[3])
    else:
        industry_dict[line[1]] = [line[1],0,0,0,0]
        industry_dict[line[1]][find_placement(line[2])] += 1
      #  print line[3]
      #  print find_placement(line[3])        
#######################3

for key in industry_dict:
    writer.writerow(industry_dict[key])



#sys.stdout = saved
#print json.dumps(dict2)
#sys.stdout = saved
output.close()
#print "the file has been written\n"