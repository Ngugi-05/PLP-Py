# create empty list and perform various operations
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
extended_list = [50, 60, 70]
my_list.extend(extended_list)
print("Extended list: ", my_list)
my_list.sort()
if 30 in my_list:
    i = my_list.index(30)
    print(f"Index of 30 is: {i}")
else:
    print("30 is not in the list")
