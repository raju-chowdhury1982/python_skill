'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(file1, file2):
    with open(file1) as f:
        data = f.read()

    with open(file2, "w") as f_c_r:
        f_c_r.write(data[::-1])
