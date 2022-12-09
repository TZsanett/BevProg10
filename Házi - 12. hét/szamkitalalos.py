import random

def main():

    print("Number Guessing Game")
    print("-" * 20)
    print("I thought of a numbur between 1 and 100.")

    rand = random.randint(1,100)
    inp = 0
    guess = 0
    while(True):
        inp = int(input("your guess> "))
        guess += 1
        if (inp > rand):
            print("my number is smaller")
        if (inp < rand):
            print("my number is larger")
        if (inp == rand):
            print("Good job! That's it!")
            break
    print("Number of guesses: {0}".format(guess))

if __name__ == "__main__":
    main()