'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(f1, f2):
    with open(f1, "r") as file1:
        data = file.read()

    with open(f2, "w") as file2:
        file2.write(data)
    
