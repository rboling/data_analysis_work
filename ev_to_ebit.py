import json
import csv
import sys
import math
import csv, re, cStringIO, codecs, HTMLParser

#input2 = csv.reader(open("pb_2013.csv"))
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

#output = open("pb_2013_refined.csv", "wb")
#writer = UnicodeWriter(output)

#list of sequences:
#ev_to_ebitda
#ev_to_ebit
#pe
#return_on_eq
#wacc
#volume

year_list = ["1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013"]
sector_types = ["wacc","volume","return_on_eq","pe","ev_to_ebit","ev_to_ebitda", "beta", "price"]
points_to_check = ["MMM","AA","AXP","T","BAC","BA","CAT","CVX","CSCO","DD","XOM","GE","HPQ","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","PFE","PG","KO","TRV","UTX","UNH","VZ","WMT","DIS"]

#sector_types = ["price"]
for year in year_list:
    for sector in sector_types:
        if sector == "beta":
            input3 = sector + year
        else:
            input3 = sector + "_" + year 
        input4 = input3 + ".csv"
        input2 = csv.reader(open(input4))
        output2 = input3 + "_" + "refined_six" + ".csv"
        output = open(output2,"wb")
        writer = UnicodeWriter(output)
        index_ticker = 0 


        for line in input2:
            index_ticker += 1
            if line[0] != "Ticker" and line[0] != "EV TO T12M EBITDA" and line[0] != None and line[0] != "EV TO T12M EBIT":
                remove_empty_strings = filter(lambda x: len(x) > 0, line)
                if len(remove_empty_strings) > 0: 
                    if remove_empty_strings[0] in points_to_check: 
                        list_to_append = []
                        list_to_append.append(remove_empty_strings[0])
                        #print remove_empty_strings
                        remove_empty_strings.pop(0)
                        #print remove_empty_strings
                        line_to_analyze = list(map(lambda x: float(x), remove_empty_strings))
                        if sector == "price":
                            if len(line_to_analyze) > 1:
                                changes = []
                                for i in (range(len(remove_empty_strings) - 1)):
                                    change = abs(line_to_analyze[i + 1] - line_to_analyze[i])
                                    percentage_change = (float(change)/line_to_analyze[i])*100.0
                                    changes.append(percentage_change)    
                                average = sum(changes)/len(changes)
                                list_to_append.append(average)
                            else:
                                average = 0
                                list_to_append.append(average)
                            list_to_append.append(index_ticker)
                            #square_list = list(map(lambda x: x*x, line_to_analyze))
                            #stdev = math.sqrt(sum(square_list)/len(square_list) - average*average)
                            #list_to_append.append(stdev)
                            writer.writerow(list_to_append)
                        else:
                            if len(line_to_analyze) > 1:
                                average = sum(line_to_analyze)/len(line_to_analyze)
                                list_to_append.append(average)
                            else:
                                average = 0
                                list_to_append.append(average)
                            list_to_append.append(index_ticker)
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