number = int(input("enter number of names:"))
name_list = []
for i in range(number):
    names = input("enter list of names:")
    name_list.append(names)
    number = name_list.count(name_list[i])
    print(number , name_list[i])
