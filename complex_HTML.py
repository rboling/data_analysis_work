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
output = open("complex_output.csv", "wb")
writer = UnicodeWriter(output)

# add header row
writer.writerow(["Movie Title", "Time", "Genre", "Directors", "Writers", "Actors", "Rating","Number of Ratings"])


# Get the DOM object to scrape for movie links. [Hint: Use absolute URL's.
# Documentation can be found here: http://www.clips.ua.ac.be/pages/pattern-web] 
url = URL("http://www.imdb.com/chart/top")
dom = DOM(url.download(cached=True))
Titles = dom.by_tag("table")[1].by_tag("tr")
for title in Titles:
    if len(title.by_tag("a")):
        genre_release_array = []
        release_array = []
        actor_array = []
        righter_array = []
        director_array = []
        new_righter_array = []
        title_to_row = title.by_tag("a")[0].content
        rating = title.by_tag("td")[1].by_tag("font")[0].content
        amount_of_ratings = title.by_tag("td")[3].by_tag("font")[0].content
        url_string = "http://www.imdb.com" + title.by_tag("a")[0].href
        sub_url = URL(url_string)
        sub_dom = DOM(sub_url.download(cached=True))
        for director in sub_dom.by_class("txt-block")[0].by_tag("a"):
			director_array.append(director.content)
        for genre_release in sub_dom.by_class("infobar")[0].by_tag("a"):
		    genre_release_array.append(genre_release.content)
        for release in sub_dom.by_class("infobar")[0].by_class("nobr")[0].by_tag("a"):
	        release_array.append(release.content)
		director_string = "; ".join(director_array)				
		genre_array = list(set(genre_release_array) - set(release_array))
 		genre_string = "; ".join(genre_array)		
		film_time = sub_dom.by_class("infobar")[0].by_tag("time")[0].content
		for righter in sub_dom.by_class("txt-block")[1].by_tag("a"):
		    righter_array.append(righter.content)
		if len(righter_array) > 2:
		    for i in [0,1]:
			    new_righter_array.append(righter_array[i])
		for actor in sub_dom.by_class("txt-block")[2].by_tag("a"):
		    if actor.content != "See full cast and crew":
			    actor_array.append(actor.content)      
		
		split_film_time = re.split(" ", film_time)
		split_parser_time = HTMLParser.HTMLParser().unescape(film_time).encode('ascii', 'ignore')		
		parse_split_unicode_time = re.split(" ", split_parser_time)
		filtered_unicode = filter(lambda x: len(x) > 0, parse_split_unicode_time)
		real_film_time = filtered_unicode[1]
		righter_string = "; ".join(righter_array)
		righter_string_sanitized = HTMLParser.HTMLParser().unescape(righter_string).encode('ascii', 'ignore')
		actor_string = "; ".join(actor_array)
		actor_string_sanitized = HTMLParser.HTMLParser().unescape(actor_string).encode('ascii', 'ignore')
		if len(righter_array) < 3:
		    writer.writerow([HTMLParser.HTMLParser().unescape(title_to_row).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(real_film_time).encode('ascii', 'ignore'), 
		    HTMLParser.HTMLParser().unescape(genre_string).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(director_string).encode('ascii', 'ignore'), righter_string_sanitized, actor_string_sanitized, 
		    HTMLParser.HTMLParser().unescape(rating).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(amount_of_ratings).encode('ascii', 'ignore')])
		else:
		    new_righter_string = "; ".join(new_righter_array)
		    new_righter_string_sanitized = HTMLParser.HTMLParser().unescape(new_righter_string).encode('ascii', 'ignore')
		    writer.writerow([HTMLParser.HTMLParser().unescape(title_to_row).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(real_film_time).encode('ascii', 'ignore'), 
		    HTMLParser.HTMLParser().unescape(genre_string).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(director_string).encode('ascii', 'ignore'), new_righter_string_sanitized, actor_string_sanitized, 
		    HTMLParser.HTMLParser().unescape(rating).encode('ascii', 'ignore'), HTMLParser.HTMLParser().unescape(amount_of_ratings).encode('ascii', 'ignore')])			

#With the movie links, scrape each entry
#You will get the the following items:
#Produce a comma-separated text file (use semicolons to separate the entries) with a header row and the fields: 
#        Title of movie
#        Runtime
#        Genre (separated by semicolons if multiple)
#        Director(s)
#        Writer(s)
#        Actors (listed on the page directly only or first three, separated by semicolons)
#        Ratings
#        Number of Ratings


output.close()
