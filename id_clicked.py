import json
import csv
import sys
input2 = csv.reader(open("master workbook.csv"))
output = file('id_clicked.json', 'wb')
saved = sys.stdout
sys.stdout = output
dict2 = {}
for line in input2:
	if line[0] != "Ticker":
		dict2[line[11]] = "false"
print json.dumps(dict2)
sys.stdout = saved
output.close()
