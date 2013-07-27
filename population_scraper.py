import csv, re, cStringIO, codecs, HTMLParser

from pattern.web import abs, URL, DOM, plaintext, strip_between
from pattern.web import NODE, TEXT, COMMENT, ELEMENT, DOCUMENT

#unicode writer
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

# Creating the csv output file for writing into as well as defining the writer
output = open("literacy_rates.csv", "wb")
writer = UnicodeWriter(output)

# add header row
writer.writerow(["country", "literacy rate"])


# Get the DOM object to scrape for movie links. [Hint: Use absolute URL's.
# Documentation can be found here: http://www.clips.ua.ac.be/pages/pattern-web] 
url = URL("http://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate")
dom = DOM(url.download(cached=True))
countries = dom.by_tag("table")[1].by_tag("tr")
for country in countries:
    if  country.by_tag("td"):
        if country.by_tag("td")[0].by_tag("a"):
            country_to_write = country.by_tag("td")[0].by_tag("a")[0].content
            rate_to_write = country.by_tag("td")[1].content
            writer.writerow([HTMLParser.HTMLParser().unescape(country_to_write).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(rate_to_write).encode('ascii', 'ignore')])

output.close()



