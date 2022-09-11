number = int(input("enter the number:"))

for i in range(1 , number-1):
    number = number/i
    if number == 1:
        answer = True
        break
    else:
        answer = False
if answer == True:
    print("the number is factorial of another number")
else:
    print("the number isn't factorial of another number")