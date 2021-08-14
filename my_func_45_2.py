# checking is there any number in a number list has even number then show Even list else return Odd list


def is_evenlist(mylist):
    for value in mylist:
        if (value % 2 == 0):
            return "Even List"
        else:
            pass
    return "Odd List"


mylist = [1, 2, 3, 4]

result = is_evenlist([1, 2, 3, 4])

print(result)



mylist2 = [1, 3, 5, 7, 9]

print(is_evenlist(mylist2))




# let write new function which will return only even numbers from a given list

def even_list(mylist):
    result = []
    for value in mylist:
        if value % 2 == 0:
            result.append(value)
        else:
            pass
    return result


mylist3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even_list(mylist3))




