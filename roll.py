import random
# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

def print_greeting():
    print("\n\n{:^50}".format("Welcome to Dice Roller v2.1.300 rev a.\n"))
    print("{:<50}".format("-Despite the name, you are allowed to roll only one die."))
    print("{:<50}".format("-Feel free to roll as many as you'd like!"))


def print_user_prompt():
    print("\nHow many dice would you like to roll?\n")


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
    result = ""
    result_list = []
    for roll in range(num):
        if roll < num - 1:
            number = roll_die()
            result += str(number) + ", "
            result_list.append(number)
        else:
            number = roll_die()
            result += str(number)
            result_list.append(number)
    return [result, result_list]


def print_sum_of_rolls(rolls_to_sum: list):
    print("The total of your rolled dice is: {}".format(sum(rolls_to_sum)))


def print_roll_again_prompt():
    print("Would you like to play again?")
    print("[1] Yes\n[2] No\n")


def roll_again_input_verification(user_choice):
    try:
        if int(user_choice) == 1 or 2:
            return int(user_choice)
        else:
            print("Please choose a valid option.")
            return False
    except ValueError:
        print("Please enter: \n[1] To Play Again\n[2] To Quit")
        return False


def on_or_off(choice):
    if int(choice) == 1:
        return True
    elif int(choice) == 2:
        return False


on = True
print_greeting()
while on:
    print_user_prompt()
    num_rolls = get_user_input()
    while verify_user_input_is_int(num_rolls) is False:
        print("\nHow many times would you like to roll?\n")
        num_rolls = get_user_input()
    num_rolls = int(num_rolls)
    results = roll_number_of_times(num_rolls)
    results_string, results_list = results
    print("\n" + results_string + "\n")
    print_sum_of_rolls(results_list)
    print_roll_again_prompt()
    again_choice = get_user_input()
    while roll_again_input_verification(again_choice) is False:
        again_choice = get_user_input()
    on = on_or_off(again_choice)
print("Goodbye!")

