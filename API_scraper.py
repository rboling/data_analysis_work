import os, sys; sys.path.insert(0, os.path.join("..", ".."))
import codecs
import HTMLParser
import re
import calendar

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint\


# Welcome to Twitter data exercise! 
# To help you get started, you should look at the 03-twitter.py example that comes with pattern-2.5.
# Much of the code is written there for you. You just have to understand it!

# INSTRUCTIONS

# 1) Using Pattern stream API for Twitter, write output to twitter_output.csv
# 2) Search for 100 tweets with "visualization" in them 
# 3) Make sure they are unique (HINT: look at 03-twitter.py and the example with index)
# 4) Each row should have:
		# 	Author_of_tweet		
		#   Date (in format of 01/25/2013)
		#	Time (in format of 00:25:29)	
		#	Text_of_tweet (as a string)	
		#	Hashtag1 (if any) with first hashtag word without hashtag symbol in front of it
		#	Hashtag2 (if ang)
		
# Output should be in the same style as the following 

	#		christina98		01/25/2013		00:24:59	visualization rocks! #viz #visual #fun			viz		visual		fun
	#		spencer88		01/25/2013		00:25:29	visualization of food. #food					food
	#		george100		01/25/2013		00:23:27	d3.js visualization	struggz			
	
# 5) Make sure we can read your code!


try: 
    # We store tweets in a Datasheet that can be saved as a text file (comma-separated).
    # In the first column, we'll store a unique ID for each tweet.
    # We only want to add the latest tweets, i.e., those we haven't previously encountered.
    # With an index on the first column we can quickly check if an ID already exists.
    # The index becomes important once more and more rows are added to the table (speed).
    table = Datasheet.load("twitter_output.csv")
    index = dict.fromkeys(table.columns[0], True)
except:
    table = Datasheet()
    index = {}

engine = Twitter(language="en")

dictionary = dict((v,k) for k,v in enumerate(calendar.month_abbr))

for tweet in engine.search("visualization", count=100, cached=False):
    hashtag_list = []
    sanitized_text = HTMLParser.HTMLParser().unescape(tweet.text).encode('ascii', 'ignore')	
    sanitized_author = HTMLParser.HTMLParser().unescape(tweet.text).encode('ascii', 'ignore')
    sanitized_time =  HTMLParser.HTMLParser().unescape(tweet.date).encode('ascii', 'ignore')	
    split_time = re.split(" ", sanitized_time)
    date_number = dictionary[split_time[2]]
    real_date = str(date_number) + '/' + str(split_time[1]) + '/' + str(split_time[3])	
    real_date_string  = str(real_date)	
    time = split_time[4]
    hashtagsa = hashtags(sanitized_text)
    for hashtag in hashtagsa:
	    new_string = ""
	    for c in hashtag:
		    if c != '#':
			    new_string += c
	    hashtag_list.append(new_string)
	
    # Create a unique ID based on the tweet content and author.
    id = str(hash(tweet.author + tweet.text))
    # Only add the tweet to the table if it doesn't already contain this ID.
    if len(table) == 0 or id not in index:
        list_to_merge = filter(lambda x: len(x) > 0, [sanitized_author, real_date_string, time, sanitized_text] + hashtag_list)			
        if len(hashtag_list) > 0:
            table.append(list_to_merge)
            index[id] = True
        else:
            table.append([sanitized_author, real_date_string, time, sanitized_text])
            index[id] = True

table.save("twitter_output.csv")
