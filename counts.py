# creat a file and find the number:
str1 = '''Jack and Jill
went up the hill
to fetch a pile of water
Jack fell down
and broke his crown
Jill come trobling after'''
with open("Jack.txt", "w") as f:
    f.write(str1)


with open("Jack.txt") as new_file:
    lines = new_file.readlines()


ls = len(lines)
wrds = sum(len(line.split(" ")) for line in lines)
chs = sum(len(line) for line in lines)
res = {}
res["lines"], res["words"], res["characters"] = ls, wrds, chs
# print(res)


def statistics(file):
    with open(file) as f:
        lines = f.readlines()

        return { "lines": len(lines),
                 "words": sum(len(line.split(" ")) for line in lines),
                 "characters": sum(len(line) for line in lines) }


print(statistics("Jack.txt"))
