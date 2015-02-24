duma=input("Enter word:")

n = input("Enter count of words: ")
n = int(n)
broi=0
count = 1
words = []

while count <= n:
    word = input("Enter word: ")
    words= [word] + words
    count += 1
for word in words:
    if duma in word:
        broi+=1
print(duma,"is found",broi,"times.")
