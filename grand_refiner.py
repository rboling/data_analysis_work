import json
import csv
import sys
input2 = csv.reader(open("master workbook.csv"))
output = file('master_json_three.json', 'wb')
#saved = sys.stdout
#sys.stdout = output
#saved = sys.stdout
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


industry_dict_list = []

def price_verifier(price_to_check):
    if float(price_to_check) < 1.22579:
        return "under 1.22579"
    if 1.22579 <= float(price_to_check) and float(price_to_check) < 1.702604:
        return "between 1.22579 and 1.702604"
    if 1.702604 <= float(price_to_check) and float(price_to_check) < 2.179419:
        return "between 1.702604 and 2.179419"
    if 2.179419 <= float(price_to_check):
        return "greater than 2.179419"

def price_to_earnings_verifier(price_to_earnings):
    if float(price_to_earnings) < 13.66865:
        return "under 13.66865"
    if  13.66865 <= float(price_to_earnings) and float(price_to_earnings) < 18.43279:
        return "between 13.66865 and 18.43279"
    if 18.43279 <= float(price_to_earnings) and float(price_to_earnings) < 26.41796:
        return "between 18.43279 and 26.41796"
    if 26.41796 <= float(price_to_earnings):
        return "greater than 26.41796"

def wacc_verifier(wacc_to_check):
    if float(wacc_to_check) < 7.647731:
        return "under 7.647731"
    if  7.647731 <= float(wacc_to_check) and float(wacc_to_check) < 8.927521:
        return "between 7.647731 and 8.927521"
    if 8.927521 <= float(wacc_to_check) and float(wacc_to_check) < 10.078831:
        return "between 8.927521 and 10.078831"
    if 10.078831 <= float(wacc_to_check):
        return "greater than 10.078831"

def beta_verifier(beta_to_check):
    if float(beta_to_check) < .764889:
        return "under .764889"
    if .764889 <= float(beta_to_check) and float(beta_to_check) < .970589:
        return "between .764889 and .970589"
    if .970589 <= float(beta_to_check) and float(beta_to_check) < 1.169315:
        return "between .970589 and 1.169315"
    if 1.169315 <= float(beta_to_check):
        return "greater than 1.169315"

def profit_margin_verifier(profit_margin_to_check):
    if float(profit_margin_to_check) < 3.911188:
        return "under 3.911188"
    if 3.911188 <= float(profit_margin_to_check) and float(profit_margin_to_check) < 7.484077:
        return "between 3.911188 and 7.484077"
    if 7.484077 <= float(profit_margin_to_check) and float(profit_margin_to_check) < 11.99575:
        return "between 7.484077 and 11.99575"
    if 11.99575 <= float(profit_margin_to_check):
        return "greater than 11.99575"

def price_to_book_verifier(price_to_book_to_check):
    if float(price_to_book_to_check) < 1.710943:
        return "under 1.710943"
    if 1.710943 <= float(price_to_book_to_check) and float(price_to_book_to_check) < 2.790624:
        return "between 1.710943 and 2.790624"
    if 2.790624 <= float(price_to_book_to_check) and float(price_to_book_to_check) < 4.622886:
        return "between 2.790624 and 4.622886"
    if 4.622886 <= float(price_to_book_to_check):
        return "greater than 4.622886"

def return_on_equity_verifier(return_on_equity_to_check):
    if float(return_on_equity_to_check) < 9.176368:
        return "under 9.176368"
    if 9.176368 <= float(return_on_equity_to_check) and float(return_on_equity_to_check) < 13.69248:
        return "between 9.176368 and 13.69248"
    if 13.69248 <= float(return_on_equity_to_check) and float(return_on_equity_to_check) < 20.19714:
        return "between 13.69248 and 20.19714"
    if 20.19714 <= float(return_on_equity_to_check):
        return "greater than 20.19714"

def volume_verifier(volume_to_check):
    if float(volume_to_check) < 1449349:
        return "under 1449349"
    if 1449349 <= float(volume_to_check) and float(volume_to_check) < 2597665:
        return "between 1449349 and 2597665"
    if 2597665 <= float(volume_to_check) and float(volume_to_check) < 4627885:
        return "between 2597665 and 4627885"
    if 4627885 <= float(volume_to_check):
        return "greater than 4627885"






for line in input2:
    if line[0] != "Ticker":
        if len(dict2["children"]) == 0:
            price_dict = {}
            pe_dict = {}
            wacc_dict = {}
            beta_dict = {}
            profit_margin_dict = {}
            price_to_book_dict = {}
            volume_dict = {}
            return_on_equity_dict = {}
            leaf_dict = {}
            price_dict["name"] = price_verifier(line[3])
            price_dict["children"] = []
            price_dict["id"] = dict_id
            dict_id += 1
            pe_dict["name"] = price_to_earnings_verifier(line[4])
            pe_dict["children"] = []
            pe_dict["id"] = dict_id
            dict_id += 1
            wacc_dict["name"] = wacc_verifier(line[9])
            wacc_dict["children"] = []
            wacc_dict["id"] = dict_id
            dict_id += 1
            beta_dict["name"] = beta_verifier(line[5])
            beta_dict["children"] = []
            beta_dict["id"] = dict_id
            dict_id += 1
            profit_margin_dict["name"] = profit_margin_verifier(line[6])
            profit_margin_dict["children"] = []
            profit_margin_dict["id"] = dict_id
            dict_id += 1
            price_to_book_dict["name"] = price_to_book_verifier(line[7])
            price_to_book_dict["children"] = []
            price_to_book_dict["id"] = dict_id
            dict_id += 1
            volume_dict["name"] = volume_verifier(line[8])
            volume_dict["children"] = []
            volume_dict["id"] = dict_id
            dict_id += 1
            return_on_equity_dict["name"] = return_on_equity_verifier(line[10])
            return_on_equity_dict["children"] = []
            return_on_equity_dict["id"] = dict_id
            dict_id += 1
            leaf_dict["name"] = line[0]
            leaf_dict["size"] = line[3]
            leaf_dict["id"] = dict_id
            dict_id += 1
            return_on_equity_dict["children"].append(leaf_dict)
            volume_dict["children"].append(return_on_equity_dict)
            profit_margin_dict["children"].append(volume_dict)
            beta_dict["children"].append(profit_margin_dict)
            wacc_dict["children"].append(beta_dict)
            pe_dict["children"].append(wacc_dict)
            price_dict["children"].append(pe_dict)
            dict2["children"].append(price_dict)
        else:
            if any(super_sub_dict["name"] == price_verifier(line[3]) for super_sub_dict in dict2["children"]):
                leaf_dict = {}
                for sub_dict in dict2["children"]:
                    if sub_dict["name"] == price_verifier(line[3]):
                        if any(super_pe_sub_dict["name"] == price_to_earnings_verifier(line[4]) for super_pe_sub_dict in sub_dict["children"]):
                            for pe_sub_dict in sub_dict["children"]:
                                if pe_sub_dict["name"] == price_to_earnings_verifier(line[4]):
                                    if any(super_wacc_sub_dict["name"] == wacc_verifier(line[9]) for super_wacc_sub_dict in pe_sub_dict["children"]):
                                        for wacc_sub_dict in pe_sub_dict["children"]:
                                            if wacc_sub_dict["name"] == wacc_verifier(line[9]):
                                                if any(super_beta_sub_dict["name"] == beta_verifier(line[5]) for super_beta_sub_dict in wacc_sub_dict["children"]):
                                                    for beta_sub_dict in wacc_sub_dict["children"]:
                                                        if beta_sub_dict["name"] == beta_verifier(line[5]):
                                                            if any(super_profit_margin_sub_dict["name"] == profit_margin_verifier(line[6]) for super_profit_margin_sub_dict in beta_sub_dict["children"]):
                                                                for profit_margin_sub_dict in beta_sub_dict["children"]:
                                                                    if profit_margin_sub_dict["name"] == profit_margin_verifier(line[6]):
                                                                        if any(super_price_book_sub_dict["name"] == price_to_book_verifier(line[7]) for super_price_book_sub_dict in profit_margin_sub_dict["children"]):
                                                                            for price_to_book_sub_dict in profit_margin_sub_dict["children"]:
                                                                                if price_to_book_sub_dict["name"] == price_to_book_verifier(line[7]):
                                                                                    if any(super_volume_sub_dict["name"] == volume_verifier(line[8]) for super_volume_sub_dict in price_to_book_sub_dict["children"]):
                                                                                        for volume_sub_dict in price_to_book_sub_dict["children"]:
                                                                                            if volume_sub_dict["name"] == volume_verifier(line[8]):
                                                                                                if any(super_return_on_eq_sub_dict["name"] == return_on_equity_verifier(line[10]) for super_return_on_eq_sub_dict in volume_sub_dict["children"]):
                                                                                                    for return_on_equity_sub_dict in volume_sub_dict["children"]:
                                                                                                        if return_on_equity_sub_dict["name"] == return_on_equity_verifier(line[10]):
                                                                                                            leaf_dict["name"] = line[0]
                                                                                                            leaf_dict["size"] = line[3]
                                                                                                            leaf_dict["id"] = dict_id
                                                                                                            dict_id += 1
                                                                                                            return_on_equity_sub_dict["children"].append(leaf_dict)
                                                                                                else:
                                                                                                    new_return_on_eq_dict = {}
                                                                                                    new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                                                                                                    new_return_on_eq_dict["children"] = []
                                                                                                    new_return_on_eq_dict["id"] = dict_id
                                                                                                    dict_id += 1                                                                                                
                                                                                                    leaf_dict["name"] = line[0]
                                                                                                    leaf_dict["size"] = line[3]
                                                                                                    leaf_dict["id"] = dict_id
                                                                                                    dict_id += 1                                                                                                    
                                                                                                    new_return_on_eq_dict["children"].append(leaf_dict)
                                                                                                    volume_sub_dict["children"].append(new_return_on_eq_dict)
                                                                                    else:
                                                                                        new_volume_dict = {}
                                                                                        new_volume_dict["name"] = volume_verifier(line[8])
                                                                                        new_volume_dict["children"] = []
                                                                                        new_volume_dict["id"] = dict_id
                                                                                        dict_id += 1                                                                                        
                                                                                        new_return_on_eq_dict = {}
                                                                                        new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                                                                                        new_return_on_eq_dict["children"] = []
                                                                                        new_return_on_eq_dict["id"] = dict_id
                                                                                        dict_id += 1                                                                                        
                                                                                        leaf_dict["name"] = line[0]
                                                                                        leaf_dict["size"] = line[3]
                                                                                        leaf_dict["id"] = dict_id
                                                                                        dict_id += 1                                                                                        
                                                                                        new_return_on_eq_dict["children"].append(leaf_dict)
                                                                                        new_volume_dict["children"].append(new_return_on_eq_dict)  
                                                                                        price_to_book_sub_dict["children"].append(new_volume_dict)
                                                                        else:
                                                                            new_price_book_dict = {}
                                                                            new_price_book_dict["name"] = price_to_book_verifier(line[7])
                                                                            new_price_book_dict["children"] = []
                                                                            new_price_book_dict["id"] = dict_id
                                                                            dict_id += 1                                                                            
                                                                            new_volume_dict = {}
                                                                            new_volume_dict["name"] = volume_verifier(line[8])
                                                                            new_volume_dict["children"] = []
                                                                            new_volume_dict["id"] = dict_id
                                                                            dict_id += 1                                                                            
                                                                            new_return_on_eq_dict = {}
                                                                            new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                                                                            new_return_on_eq_dict["children"] = []
                                                                            new_return_on_eq_dict["id"] = dict_id
                                                                            dict_id += 1                                                                            
                                                                            leaf_dict["name"] = line[0]
                                                                            leaf_dict["size"] = line[3]
                                                                            leaf_dict["id"] = dict_id
                                                                            dict_id += 1                                                                            
                                                                            new_return_on_eq_dict["children"].append(leaf_dict)
                                                                            new_volume_dict["children"].append(new_return_on_eq_dict)  
                                                                            new_price_book_dict["children"].append(new_volume_dict)
                                                                            profit_margin_sub_dict["children"].append(new_price_book_dict)
                                                            else:
                                                                new_profit_margin_dict = {}
                                                                new_profit_margin_dict["name"] = profit_margin_verifier(line[6])
                                                                new_profit_margin_dict["children"] = []
                                                                new_profit_margin_dict["id"] = dict_id
                                                                dict_id += 1                                                                
                                                                new_price_book_dict = {}
                                                                new_price_book_dict["name"] = price_to_book_verifier(line[7])
                                                                new_price_book_dict["children"] = []
                                                                new_price_book_dict["id"] = dict_id
                                                                dict_id += 1                                                                
                                                                new_volume_dict = {}
                                                                new_volume_dict["name"] = volume_verifier(line[8])
                                                                new_volume_dict["children"] = []
                                                                new_volume_dict["id"] = dict_id
                                                                dict_id += 1                                                                
                                                                new_return_on_eq_dict = {}
                                                                new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                                                                new_return_on_eq_dict["children"] = []
                                                                new_return_on_eq_dict["id"] = dict_id
                                                                dict_id += 1                                                                
                                                                leaf_dict["name"] = line[0]
                                                                leaf_dict["size"] = line[3]
                                                                leaf_dict["id"] = dict_id
                                                                dict_id += 1                                                                
                                                                new_return_on_eq_dict["children"].append(leaf_dict)
                                                                new_volume_dict["children"].append(new_return_on_eq_dict)  
                                                                new_price_book_dict["children"].append(new_volume_dict)
                                                                new_profit_margin_dict["children"].append(new_price_book_dict)
                                                                beta_sub_dict["children"].append(new_profit_margin_dict)
                                                else:
                                                    new_beta_dict = {}
                                                    new_beta_dict["name"] = beta_verifier(line[5])
                                                    new_beta_dict["children"] = []
                                                    new_profit_margin_dict = {}
                                                    new_profit_margin_dict["name"] = profit_margin_verifier(line[6])
                                                    new_profit_margin_dict["children"] = []
                                                    new_price_book_dict = {}
                                                    new_price_book_dict["name"] = price_to_book_verifier(line[7])
                                                    new_price_book_dict["children"] = []
                                                    new_volume_dict = {}
                                                    new_volume_dict["name"] = volume_verifier(line[8])
                                                    new_volume_dict["children"] = []
                                                    new_return_on_eq_dict = {}
                                                    new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                                                    new_return_on_eq_dict["children"] = []
                                                    leaf_dict["name"] = line[0]
                                                    leaf_dict["size"] = line[3]
                                                    new_return_on_eq_dict["children"].append(leaf_dict)
                                                    new_volume_dict["children"].append(new_return_on_eq_dict)  
                                                    new_price_book_dict["children"].append(new_volume_dict)
                                                    new_profit_margin_dict["children"].append(new_price_book_dict)
                                                    new_beta_dict["children"].append(new_profit_margin_dict)
                                                    wacc_sub_dict["children"].append(new_beta_dict)
                                    else:
                                        new_wacc_dict = {}
                                        new_wacc_dict["name"] = wacc_verifier(line[9])
                                        new_wacc_dict["children"] = []
                                        new_wacc_dict["id"] = dict_id
                                        dict_id += 1                                        
                                        new_beta_dict = {}
                                        new_beta_dict["name"] = beta_verifier(line[5])
                                        new_beta_dict["children"] = []
                                        new_beta_dict["id"] = dict_id
                                        dict_id += 1                                        
                                        new_profit_margin_dict = {}
                                        new_profit_margin_dict["name"] = profit_margin_verifier(line[6])
                                        new_profit_margin_dict["children"] = []
                                        new_profit_margin_dict["id"] = dict_id
                                        dict_id += 1                                        
                                        new_price_book_dict = {}
                                        new_price_book_dict["name"] = price_to_book_verifier(line[7])
                                        new_price_book_dict["children"] = []
                                        new_price_book_dict["id"] = dict_id
                                        dict_id += 1                                        
                                        new_volume_dict = {}
                                        new_volume_dict["name"] = volume_verifier(line[8])
                                        new_volume_dict["children"] = []
                                        new_volume_dict["id"] = dict_id
                                        dict_id += 1
                                        new_return_on_eq_dict = {}
                                        new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                                        new_return_on_eq_dict["children"] = []
                                        new_return_on_eq_dict["id"] = dict_id
                                        dict_id += 1
                                        leaf_dict["name"] = line[0]
                                        leaf_dict["size"] = line[3]
                                        leaf_dict["id"] = dict_id
                                        dict_id += 1                                        
                                        new_return_on_eq_dict["children"].append(leaf_dict)
                                        new_volume_dict["children"].append(new_return_on_eq_dict)  
                                        new_price_book_dict["children"].append(new_volume_dict)
                                        new_profit_margin_dict["children"].append(new_price_book_dict)
                                        new_beta_dict["children"].append(new_profit_margin_dict)
                                        new_wacc_dict["children"].append(new_beta_dict) 
                                        pe_sub_dict["children"].append(new_wacc_dict)     
                        else:
                            new_pe_dict = {}
                            new_pe_dict["name"] = price_to_earnings_verifier(line[4])
                            new_pe_dict["children"] = []
                            new_pe_dict["id"] = dict_id
                            dict_id += 1
                            new_wacc_dict = {}
                            new_wacc_dict["name"] = wacc_verifier(line[9])
                            new_wacc_dict["children"] = []
                            new_wacc_dict["id"] = dict_id
                            dict_id += 1                            
                            new_beta_dict = {}
                            new_beta_dict["name"] = beta_verifier(line[5])
                            new_beta_dict["children"] = []
                            new_beta_dict["id"] = dict_id
                            dict_id += 1                            
                            new_profit_margin_dict = {}
                            new_profit_margin_dict["name"] = profit_margin_verifier(line[6])
                            new_profit_margin_dict["children"] = []
                            new_profit_margin_dict["id"] = dict_id
                            dict_id += 1                            
                            new_price_book_dict = {}
                            new_price_book_dict["name"] = price_to_book_verifier(line[7])
                            new_price_book_dict["children"] = []
                            new_price_book_dict["id"] = dict_id
                            dict_id += 1                            
                            new_volume_dict = {}
                            new_volume_dict["name"] = volume_verifier(line[8])
                            new_volume_dict["children"] = []
                            new_volume_dict["id"] = dict_id
                            dict_id += 1                            
                            new_return_on_eq_dict = {}
                            new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                            new_return_on_eq_dict["children"] = []
                            new_return_on_eq_dict["id"] = dict_id
                            dict_id += 1                            
                            leaf_dict["name"] = line[0]
                            leaf_dict["size"] = line[3]
                            leaf_dict["id"] = dict_id
                            dict_id += 1                            
                            new_return_on_eq_dict["children"].append(leaf_dict)
                            new_volume_dict["children"].append(new_return_on_eq_dict)  
                            new_price_book_dict["children"].append(new_volume_dict)
                            new_profit_margin_dict["children"].append(new_price_book_dict)
                            new_beta_dict["children"].append(new_profit_margin_dict)
                            new_wacc_dict["children"].append(new_beta_dict) 
                            new_pe_dict["children"].append(new_wacc_dict)
                            sub_dict["children"].append(new_pe_dict)
            else:
                new_price_dict = {}
                new_price_dict["name"] = price_verifier(line[3])
                new_price_dict["children"] = []
                new_price_dict["id"] = dict_id
                dict_id += 1                
                new_pe_dict = {}
                new_pe_dict["name"] = price_to_earnings_verifier(line[4])
                new_pe_dict["children"] = []
                new_pe_dict["id"] = dict_id
                dict_id += 1
                new_wacc_dict = {}
                new_wacc_dict["name"] = wacc_verifier(line[9])
                new_wacc_dict["children"] = []
                new_wacc_dict["id"] = dict_id
                dict_id += 1
                new_beta_dict = {}
                new_beta_dict["name"] = beta_verifier(line[5])
                new_beta_dict["children"] = []
                new_beta_dict["id"] = dict_id
                dict_id += 1
                new_profit_margin_dict = {}
                new_profit_margin_dict["name"] = profit_margin_verifier(line[6])
                new_profit_margin_dict["children"] = []
                new_profit_margin_dict["id"] = dict_id
                dict_id += 1
                new_price_book_dict = {}
                new_price_book_dict["name"] = price_to_book_verifier(line[7])
                new_price_book_dict["children"] = []
                new_price_book_dict["id"] = dict_id
                dict_id += 1
                new_volume_dict = {}
                new_volume_dict["name"] = volume_verifier(line[8])
                new_volume_dict["children"] = []
                new_volume_dict["id"] = dict_id
                dict_id += 1
                new_return_on_eq_dict = {}
                new_return_on_eq_dict["name"] = return_on_equity_verifier(line[10])
                new_return_on_eq_dict["children"] = []
                new_return_on_eq_dict["id"] = dict_id
                dict_id += 1
                leaf_dict["name"] = line[0]
                leaf_dict["size"] = line[3]
                leaf_dict["id"] = dict_id
                dict_id += 1
                new_return_on_eq_dict["children"].append(leaf_dict)
                new_volume_dict["children"].append(new_return_on_eq_dict)  
                new_price_book_dict["children"].append(new_volume_dict)
                new_profit_margin_dict["children"].append(new_price_book_dict)
                new_beta_dict["children"].append(new_profit_margin_dict)
                new_wacc_dict["children"].append(new_beta_dict) 
                new_pe_dict["children"].append(new_wacc_dict)
                new_price_dict["children"].append(new_pe_dict)
                dict2["children"].append(new_price_dict)            


#def dict_id_builder(dict_to_test):
#    try:
#        id_dict[dict_to_test["id"]] = []
#        for child in dict_to_test["children"]:
#            print child
#            id_dict[dict_to_test["id"]].append(child["id"])
#            return dict_id_builder(child)
#    except:
#        return id_dict

a = 500

def dict_id_builder(dict_to_test):
    a = 500
    while(a > 0):
        if "children" in dict_to_test:
            id_dict[dict_to_test["id"]] = []
            for child in dict_to_test["children"]:
                print child["id"]
                id_dict[dict_to_test["id"]].append(child["id"])
                dict_to_test = child
        else:
            a -= 1

dict_id_builder(dict2)
print id_dict
#sys.stdout = saved
#print json.dumps(dict2)
#print json.dumps(dict_id_builder(dict2))
#sys.stdout = saved
output.close()
#print len(dict2["points"])
#print "a"
#print a
#print "b"
#print b
#print "the file has been written\n"