numbers = []
for i in range(10):
    user_number = int(input())
    numbers.append(user_number)
for i in range(1, len(numbers)):
    if numbers[i-1] <= numbers[i]:
        flag= True
        continue
    else:
        flag= False
        break
if flag == False:
    print("no")
else:
    print("yes")