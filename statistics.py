'''
statistics('story.txt')
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(file):
    with open(file) as f:
        data = f.read()

    #     data1 = data.split("\n")
    #     data2 = data.split(" ")
    #     res ={}
    #     res["lines"] = len(data1)
    #     res["words"] = len(data2)
    #     res["characters"] = len(data)
    #
    # print(res)
    return {"lines":len(data), "words": sum(len(d.split(" ")) for d in data), "characters":sum(char) for cahr in data}
