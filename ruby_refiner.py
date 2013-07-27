from pattern.web import Wikipedia
import codecs
import HTMLParser
import csv, re, cStringIO, codecs, HTMLParser
import json
import re
from pattern.web import abs, URL, DOM, plaintext, strip_between
from pattern.web import NODE, TEXT, COMMENT, ELEMENT, DOCUMENT

import urllib2

def split_string(source, separators): 
	string_to_split = '[' + separators + ']' + '+'
	split_with_re = re.split(string_to_split, source)
	remove_empty_strings = filter(lambda x: len(x) > 0, split_with_re)	
	return remove_empty_strings

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
			
output = open("even_ruby_newer_scraping_output.csv", "wb")
writer = UnicodeWriter(output)		
writer.writerow(["Article Title", "Year", "Bytes of Edit","latitude", "longitude", "latitude_2012", "longitude_2012"])
with open('better_ruby_scraping_output.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    print "foober\n"
    print "the row"
    print row[1]	
    check_date = row[1].split()[0]	
    if check_date != 'Date':
      split_row = row[1].split()[3]
      print "the split row"
      print row[1].split()  
      split_even_more = split_string(split_row, '/')	
      print "split even more\n"
      print split_even_more	
      print split_row
    #  year = split_even_more[2]
      bytes_prelim = split_string(row[3], '( )')
      print "bytes_prelim"
      print bytes_prelim	
      real_bytes = bytes_prelim[0]	  
      if split_row == '2012':	  
        writer.writerow(["Ruby Programming Language", split_row, real_bytes, row[5], row[6], row[5], row[6]])
      else:
        writer.writerow(["Ruby Programming Language", split_row, real_bytes, row[5], row[6], "", ""])
      	
output.close()
