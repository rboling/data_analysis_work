import codecs
import HTMLParser
import csv, re, cStringIO, codecs, HTMLParser
import json
import re
import urllib2
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

    def non_utf_writerow(self, row):
      self.writer.writerow(row)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
			
output = open("student_to_country.csv", "wb")
writer = UnicodeWriter(output)    
writer.writerow(["Student ID", "Country"])
courses_output = open("students_to_courses.csv", "wb")
courses_writer = UnicodeWriter(courses_output)		
courses_writer.writerow(["Student ID", "Courses"])


with open('randGeoLocEx.csv', 'rb') as EdxCsvFile:
  bad_count = 0
  reader = csv.reader(EdxCsvFile, delimiter=',')
  people_country_dictionary = {}
  people_courses_dictionary = {}
  for row in reader:
    try:
      people_country_dictionary[row[2]].append(row[1])
    except:
      people_country_dictionary[row[2]] = []
      people_country_dictionary[row[2]].append(row[1])
    try:
      people_courses_dictionary[row[2]].append(row[0])
    except:
      people_courses_dictionary[row[2]] = []
      people_courses_dictionary[row[2]].append(row[0])
  for key in people_country_dictionary:
    row_to_write = []
    row_to_write.append(key)
    row_to_write += people_country_dictionary[key]
    #if len(people_country_dictionary[key]) > 1: 
      #print "Too Many Countries"
      #print key
      #print people_country_dictionary[key]
    try:
      writer.writerow(row_to_write)
    except:
      bad_count += 1
      writer.non_utf_writerow(row_to_write)
  print "bad_count"
  print bad_count
  for key in people_courses_dictionary:
    row_to_write = []
    row_to_write.append(key)
    row_to_write += people_courses_dictionary[key]
    try:
      courses_writer.writerow(row_to_write)
    except:
      bad_count += 1
      courses_writer.non_utf_writerow(row_to_write)

output.close()

courses_output.close()

"""
while (len(dom.by_class("mw-nextlink")) > 0):
  page_history_links = dom.by_tag("ul")[0].by_tag("li")
  for link in page_history_links:
    date = HTMLParser.HTMLParser().unescape(link.by_class("mw-changeslist-date")[0].content).encode('ascii','ignore') 
    ip = HTMLParser.HTMLParser().unescape(link.by_class("history-user")[0].by_tag("a")[0].content).encode('ascii','ignore')  
    bytes = HTMLParser.HTMLParser().unescape(link.by_class("history-size")[0].content).encode('ascii','ignore')  
    ip_url = 'http://api.hostip.info/get_json.php?ip=' + ip + '&position=true'
    req = urllib2.urlopen(ip_url)
    req_request = urllib2.Request(ip_url)
    #handler = urllib2.urlopen(req)
#    print "this must be the code in bytes\n"	
#    print req.read()
    read_ip_data = HTMLParser.HTMLParser().unescape(req.read()).encode('ascii', 'ignore')	
    if read_ip_data.split()[0] != '<html>':	
      print "the date\n"
      print date	  
      read_ip_data_json = json.loads(read_ip_data)
      latitude = read_ip_data_json["lat"]
      longitude = read_ip_data_json["lng"]
 #   read_ip_data = req.read()	

      if read_ip_data == "":
	    print "empty string\n\n"
      if latitude is None:
        latitude = ""
      if longitude is None:
        longitude = ""		
      writer.writerow([article.title, date, ip, bytes, read_ip_data, latitude, longitude])  
    
  print "im in here\n"
  new_url = 'http://en.wikipedia.org' + dom.by_class("mw-nextlink")[0].href
  new_real_url = URL(new_url)
  dom = DOM(new_real_url.download(cached=True))
  a += 1
  #####
####
print a
"""
