# reading a file

with open("July21_Inv_Report.csv") as f:
    data = f.read()


# print(type(data))

data_lst = data.split("\n")

# print(type(data_lst))
# print(data_lst[1:11])
# print(type(data_lst[1]))

data1 = [item.split(",") for item in data_lst]

# print(data1)
# print(data1[2:11])
print(data1[2][1])
print (type(data1[2][1]))
val = int(float(data1[2][1]))
print (val)
# total = 0
# for item in data1[1:]:
#     total += int(item[1])
#


# print(total)
