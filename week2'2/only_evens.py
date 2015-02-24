n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1

broi=0
for number in numbers:
    if number%2==0:
        broi+=1
print("Count of evens:",broi)
print("Evens are:")
for number in numbers:
    if number%2==0:
       print(number)

