import json
import csv
import sys
input2 = csv.reader(open("refined_master_data.csv"))
output = file('sector_json_four.json', 'wb')
#saved = sys.stdout
sys.stdout = output
saved = sys.stdout
#sys.stdout = output
#fields = input2.next()
#print "these are the fields\n"
#print fields
dict_id = 0
dict2 = {}
id_dict = {}
dict2["name"] = "all stocks"
dict2['children'] = []
dict2["id"] = dict_id
dict_id += 1
industry_dict = {}
price_dict_check = {}
price_to_earnings_dict_check = {}
wacc_dictionary_check = {}
beta_dictionary_check = {}
profit_margin_dictionary_check = {}
price_to_book_dictionary_check = {}
return_on_equity_dictionary_check = {}
volume_dictionary_check = {}

def price_verifier(price_to_check):
    if float(price_to_check) < 1.22579:
        return "under 1.22579"
    if 1.22579 <= float(price_to_check) and float(price_to_check) < 1.702604:
        return "between 1.22579 and 1.702604"
    if 1.702604 <= float(price_to_check) and float(price_to_check) < 2.179419:
        return "between 1.702604 and 2.179419"
    if 2.179419 <= float(price_to_check):
        return "greater than 2.179419"


for line in input2:
    if line[0] != "Ticker":
        if len(dict2["children"]) == 0:
            sector_dict = {}
            leaf_dict = {}
            sector_dict["name"] = line[10]
            sector_dict["children"] = []
            ticker_dict = {}
            ticker_dict["name"] = line[0]
            ticker_dict["average_price_return"] = float(line[1])
            ticker_dict["average_price_to_earnings"] = float(line[2])
            ticker_dict["average_beta"] = float(line[3])
            ticker_dict["average_profit_margin"] = float(line[4])
            ticker_dict["average_price_to_book"] = float(line[5])
            ticker_dict["average_volume"] = float(line[6])
            ticker_dict["average_wacc"] = float(line[7])
            ticker_dict["average_return_on_equity"] = float(line[8])
            ticker_dict["id"] = float(line[9])
            ticker_dict["sector"] = line[10]
            ticker_dict["size"] = line[1]
            sector_dict["children"].append(ticker_dict)
            dict2["children"].append(sector_dict)
        else:
            if any(super_sub_dict["name"] == line[10] for super_sub_dict in dict2["children"]):
                ticker_dict = {}
                for sub_dict in dict2["children"]:
					if sub_dict["name"] == line[10]:
						ticker_dict["name"] = line[0]
						ticker_dict["average_price_return"] = float(line[1])
						ticker_dict["average_price_to_earnings"] = float(line[2])
						ticker_dict["average_beta"] = float(line[3])
						ticker_dict["average_profit_margin"] = float(line[4])
						ticker_dict["average_price_to_book"] = float(line[5])
						ticker_dict["average_volume"] = float(line[6])
						ticker_dict["average_wacc"] = float(line[7])
						ticker_dict["average_return_on_equity"] = float(line[8])
						ticker_dict["id"] = float(line[9])
						ticker_dict["sector"] = line[10]
						ticker_dict["size"] = line[1]
						sub_dict["children"].append(ticker_dict)                    
            else:
                new_sector_dict = {}
                ticker_dict = {}
                new_sector_dict["name"] = line[10]
                new_sector_dict["children"] = []
                ticker_dict["name"] = line[0]
                ticker_dict["average_price_return"] = float(line[1])
                ticker_dict["average_price_to_earnings"] = float(line[2])
                ticker_dict["average_beta"] = float(line[3])
                ticker_dict["average_profit_margin"] = float(line[4])
                ticker_dict["average_price_to_book"] = float(line[5])
                ticker_dict["average_volume"] = float(line[6])
                ticker_dict["average_wacc"] = float(line[7])
                ticker_dict["average_return_on_equity"] = float(line[8])
                ticker_dict["id"] = float(line[9])
                ticker_dict["sector"] = line[10]
                ticker_dict["size"] = line[1]          
                new_sector_dict["children"].append(ticker_dict)
                dict2["children"].append(new_sector_dict)            


#def dict_id_builder(dict_to_test):
#    try:
#        id_dict[dict_to_test["id"]] = []
#        for child in dict_to_test["children"]:
#            print child
#            id_dict[dict_to_test["id"]].append(child["id"])
#            return dict_id_builder(child)
#    except:
#        return id_dict

#sys.stdout = saved
print json.dumps(dict2)
#print json.dumps(dict_id_builder(dict2))
sys.stdout = saved
output.close()
#print len(dict2["points"])