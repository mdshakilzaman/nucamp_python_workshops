import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    while tries > 0:
        print("Number of tries left: ", tries)
        print("Guess a number between", start, "and", stop)
        guess = int(input())
        if guess == random_number:
            print("You guessed the correct number")
            return True
        if guess < random_number:
            print("Guess higher!")
        if guess > random_number:
            print("Guess lower!")

        tries -= 1
    print("You have failed to guess the number:", random_number)
    return False


# guess_random_number(5, 0, 10)

def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is: ", random_number)
    for i in range(0, tries):
        print("Number of tries left:", tries-i)
        print("The program is guessing", i+start)
        if (i+start) == random_number:
            print("You guessed the correct number")
            return True
    print("You have failed to guess the number:", random_number)
    return False


# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is: ", random_number)
    lower_bound = start
    upper_bound = stop
    while tries > 0:
        pivot = (lower_bound+upper_bound)//2
        pivot_value = pivot
        if pivot_value == random_number:
            print("Found it", random_number)
            return True
        if pivot_value > random_number:
            print("Guessing lower!")
            upper_bound = pivot-1
        else:
            print("Guessing higher!")
            lower_bound = pivot+1
        tries -= 1
    print("You have failed to guess the number:")
    return False


guess_random_num_binary(5, 0, 100)
