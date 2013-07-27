from pattern.web import Wikipedia
import codecs
import HTMLParser
import csv, re, cStringIO, codecs, HTMLParser
import json
import re
from pattern.web import abs, URL, DOM, plaintext, strip_between
from pattern.web import NODE, TEXT, COMMENT, ELEMENT, DOCUMENT
import urllib2
input2 = csv.reader(open("goog_data1.csv"))
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
        self.writer.writerow([s.encode("utf-8") for s in row])
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
output = open("better_goog_data.csv", "wb")
writer = UnicodeWriter(output)		
writer.writerow(["Date", "Share Price"])
months = {'1':'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
def split_string(source, separators): 
	string_to_split = '[' + separators + ']' + '+'
	split_with_re = re.split(string_to_split, source)
	remove_empty_strings = filter(lambda x: len(x) > 0, split_with_re)	
	return remove_empty_strings

for line in input2:
	date_string = ""
	date_array = split_string(line[0],"/")
	print date_array
	if (len(date_array) == 3):

		date_string = date_string + date_array[1]
		date_string = date_string + '-' + months[date_array[0]] + '-' + date_array[2]
		writer.writerow([date_string, line[1]])

output.close()
