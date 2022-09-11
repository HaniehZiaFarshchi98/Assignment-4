import random
list = []
length = int(input("enter length:"))
for i in range(length):
    numbers = random.randint(0 , 200)
    list.append(numbers)
    print("list=" , list)
