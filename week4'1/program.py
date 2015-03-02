rechnik={}
rechnik["first_name"]=input("Enter first name:")
rechnik["second_name"]=input("Enter second name:")
rechnik["third_name"]=input("Enter third name:")
rechnik["birth_year"]=input("Enter birth year:")

import datetime
now = datetime.datetime.now()
godina=now.year


rechnik["current_age"]=godina-int(rechnik["birth_year"])

print(rechnik)
