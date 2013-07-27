import json
import csv
import sys
import math
import csv, re, cStringIO, codecs, HTMLParser

def split_string(source, separators): 
    string_to_split = '[' + separators + ']' + '+'
    split_with_re = re.split(string_to_split, source)
    remove_empty_strings = filter(lambda x: len(x) > 0, split_with_re)  
    return remove_empty_strings

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

output = open("price_2013.csv", "wb")
writer = UnicodeWriter(output)

for line in input2:
    if line[0] == "Ticker":
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line.pop(0)
        line_to_analyze = filter(lambda x: len(x) > 0, line)
        list_of_dates = []
        for i in line_to_analyze:
            revised_line = split_string(i, "/")
            #print revised_line
            list_of_dates.append(revised_line)
    if line[0] != '3/28/2013' and line[0] != "Ticker" and line[0] != "PX LAST" and line[0] != None and line[0] != "":
        remove_empty_strings = filter(lambda x: len(x) > 0, line)  
        list_to_append = []
        list_to_append.append(line[0])
        if len(remove_empty_strings) > 5:
            remove_empty_strings.pop(0)
            remove_empty_strings.pop(0)
            remove_empty_strings.pop(0)
            remove_empty_strings.pop(0)
            remove_empty_strings.pop(0)
            remove_empty_strings.pop(0)
            #print line[0]
            line_to_analyze = list(map(lambda x: float(x), remove_empty_strings))
            if len(line_to_analyze) > 0:    
                for i in range(len(line_to_analyze)):
                    if list_of_dates[i][2] == '2013':
                        list_to_append.append(line[i])
                #average = sum(line_to_analyze)/len(line_to_analyze)
            #square_list = list(map(lambda x: x*x, line_to_analyze))
            #stdev = math.sqrt(sum(square_list)/len(square_list) - average*average)
            #list_to_append.append(stdev)
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