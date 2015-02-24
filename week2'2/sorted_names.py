n = input("Enter count of names: ")
n = int(n)

count = 1
imena = []

while count <= n:
    ime = input("Enter name: ")
    imena = imena + [ime]
    count += 1
print(sorted(imena))
