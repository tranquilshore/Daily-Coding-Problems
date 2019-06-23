from collections import defaultdict 
from datetime import datetime

class item:
    def __init__(self,id,start_date,end_date,price):
        self.id = id 
        self.price = price 
        self.start_date = start_date
        self.end_date = end_date

class CRUD:
    format_str = "%d/%m/%Y"

    def __init__(self):
        self.db = defaultdict(list)
    
    def put(self,item):
        price = item.price 
        if item.id == "null" or item.price == "null":
            print "Item id or price can't be null, please check your input"
        else:
            if item.start_date != "null" and item.end_date != "null":
                start_date_formatted = datetime.strptime(item.start_date,CRUD.format_str)
                end_date_formatted = datetime.strptime(item.end_date,CRUD.format_str)
                self.db[item.id].append((price,start_date_formatted,end_date_formatted))
            else:
                self.db[item.id].append((item.price,item.start_date,item.end_date))
    
    def get(self,id,date):
        if id == "null" or date == "null":
            return "id or date can't be null"
        else:
            try:
                input_date = datetime.strptime(date,CRUD.format_str)
                range_flag = False 
                if self.db.has_key(id):
                    for row in self.db[id]:
                        if row[1] != "null":
                            if input_date >= row[1] and input_date <= row[2]:
                                price = row[0]
                                range_flag = True  
                            if range_flag is False:
                                price = self.db[id][0][0]
                        else:
                            price = self.db[id][0][0]

                    return price 
                else:
                    error = "Item with id: "+id+" doesn't exist!" 
                    return error
            except:
                return "Date Format is incorrect! Follow dd/mm/YYYY"

if __name__=="__main__":
    crud_instance = CRUD()
    while True:
        print "Select Following Options:\n1. Input\n2. Query"
        choice = raw_input()
        if choice:
            if choice == "1" or choice == "2":
                if choice == "1":
                    while True:
                        line = raw_input()
                        if line:
                            item_description = line.split(",")
                            crud_instance.put(item(item_description[0],item_description[1],item_description[2],item_description[3]))
                        else:
                            break
                if choice == "2":
                    while True:
                        line = raw_input()
                        if line:
                            query = line.split(",")
                            print crud_instance.get(query[0],query[1])
                        else:
                            break 

            else:
                print "Wrong Selection!"
                continue
        else:
            break 


# item1 = item("item1234","null","null",5.04)
# item2 = item("item2345","null","null",6.53)
# item3 = item("item1234","01/01/2019","31/03/2019",5.5)
# item4 = item("item1234","13/02/2019","28/02/2019",6)

# crud_instance = CRUD()
# crud_instance.put(item1)
# crud_instance.put(item2)
# crud_instance.put(item3)
# crud_instance.put(item4)

# print crud_instance.get("item2234","15/02/2019")
# print crud_instance.get("item2345","22/03/2019")

                