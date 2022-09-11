first_list = []
for i in range (1 , 11):
    number = int(input("please enter numbers:"))
    first_list.append(number)
    
for j in range(len(first_list)):
    for k in range(j+1 , len(first_list)):
        if first_list [j]>first_list[k]:
            first_list[j],first_list[k] = first_list[k],first_list[j]

print(first_list)

    



