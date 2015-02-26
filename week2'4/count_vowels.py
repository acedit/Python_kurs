string=input("Enter string:")
glasni="aeoyiuAEOYIU"
broi=0

for znak in string:
    if znak in glasni:
        broi+=1
print(broi,"vowels")
