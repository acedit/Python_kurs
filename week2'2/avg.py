n = input("Enter count of numbers: ")
n = int(n)
suma=0
count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    suma+=number
    numbers = numbers + [number]
    count += 1
print(suma/len(numbers))
