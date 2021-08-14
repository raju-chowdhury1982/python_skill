# approach to functional programming
# import shuffle
from random import shuffle

my_list = [" ", "O", " "]

# shuffle my_list
# shuffle(my_list)
# print(my_list)

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
# end shuffle_list function


# print(shuffle_list(my_list))

# want a player to guess the item

def player_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Enter Your Guess 0, 1 0r 2:")

    return int(guess)

#my_index = player_guess()

#print(my_index)

#check the Guess
def check_guess(my_list, guess):
    if my_list[guess] == "O":
        print("Correct! You Win")
    else:
        print("Wrong!")
        print(my_list)

#function end here
# call stack
#initial list
my_list = [" ", "O", " "]
# shuffle list
shuffle_mylist = shuffle_list(my_list)
# user guess
user_guess = player_guess()

# check guess
check_guess(shuffle_mylist, user_guess)
