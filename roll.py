import random
# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

def print_greeting():
    print("{:^50}".format("Welcome to Dice Roller v2.1.300 rev a.\n"))
    print("{:<50}".format("-Despite the name, you are allowed to roll only one die."))
    print("{:<50}".format("-Feel free to roll as many as you'd like!"))


def print_user_prompt():
    print("\nHow many times would you like to roll?\n")


def get_user_input():
    num_of_rolls = input(">> ")
    return num_of_rolls


def verify_user_input_is_int(input):
    try:
        if int(input) <= 0:
            print("Please use positive, whole numbers.")
            return False
        int(input)
        return True
    except ValueError:
        print("Let's make this easy and stick to just using numbers.")
        return False


def roll_die():
    return random.randint(1,6)

def roll_number_of_times(num):
    pass

print_greeting()
print_user_prompt()
num_rolls = get_user_input()
while verify_user_input_is_int(num_rolls) is False:
    print("\nHow many times would you like to roll?\n")
    num_rolls = get_user_input()
