#dice_n_more
from random import randint
N= input("Enter sides:")
N=int(N)
choice1= randint(1, N)
print("First roll:")
print(choice1)
choice2= randint(1, N)
print("Second roll:")
print(choice2)
choice3= randint(1, N)
print("Third roll:")
print(choice3)
choice4= randint(1, N)
print("Fourth roll:")
print(choice4)
print("Sum is:")
print(choice1 + choice2 + choice3 + choice4)
      
