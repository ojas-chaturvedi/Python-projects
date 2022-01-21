from os import system
from random import choice
from random import randint
from turtle import Screen
from turtle import Turtle
from time import sleep
system("clear")


def get_word():
    word_banks = ["fruits", "vegetables", "colors", "school_items", "clothes", "candy_brands",
                  "dessert_items", "ice_cream_flavors", "meals", "peppers_types", "sports", "english_dictionary"]
    print("Choose a word from a category or input your own word. \nWords may include spaces but not case sensitive.")
    print("1-Fruits\n2-Vegetables\n3-Colors\n4-School items\n5-Cloths\n6-Candy brands\n7-Dessert items\n8-Ice Cream flavors\n9-Meals\n10-Pepper types\n11-Sports\n12-Entire English Dictionary\n13-Input your own word")
    group_choice = int(input("Choose a group: "))
    if group_choice == 13:
        word = input("Enter a word: ")
    else:
        lines = (open(word_banks[group_choice-1] + ".txt", "r")).readlines()
        word_choices = [line.strip() for line in lines]
        word = choice(word_choices)
    return word


def stats(word, wrong, guesses):
    print("Your word is: " + " ".join(word))
    print("Your wrong guesses are: " + " ".join(wrong))
    print("Your guesses are: " + " ".join(guesses))
    print("")


def animation_stool(turtle):
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(200)
    turtle.back(200)
    turtle.left(45)
    turtle.back(125)
    turtle.fd(125)
    turtle.right(90)
    turtle.back(125)
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.right(45)
    turtle.fd(150)
    turtle.right(90)
    turtle.fd(50)


def animation_head(turtle):
    turtle.penup()
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(30)
    turtle.right(90)
    turtle.pendown()


def animation_upperBody(turtle):
    turtle.fd(25)


def animation_lowerBody(turtle):
    turtle.left(30)
    turtle.fd(75)


def animation_arm1(turtle):
    turtle.left(30)
    turtle.fd(75)
    turtle.back(75)


def animation_arm2(turtle):
    turtle.right(60)
    turtle.fd(75)
    turtle.back(75)


def animation_leg1(turtle):
    turtle.left(30)
    turtle.fd(75)
    turtle.back(75)


def animation_leg2(turtle):
    turtle.right(60)
    turtle.fd(75)
    turtle.back(75)
    turtle.left(30)


animation_list = [animation_head, animation_upperBody, animation_arm1,
                  animation_arm2, animation_lowerBody, animation_leg1, animation_leg2]


def game():

    wrong_attempts = 0
    loop = True
    word = get_word()
    word_list = list(word)
    print("There are " + str(len(word_list)) + " letters in this word")
    wrong_guesses = []
    user_guesses = []
    replace_list = ["_"] * len(word)
    animation_stool()
    print("You can have 6 wrong guesses! One more and you lose!!")
    stats(replace_list, wrong_guesses, user_guesses)
    while loop:
        letter = input("Guess a letter, or the word: ")
        letter = letter.lower()
        if letter in user_guesses:
            print("You already guessed this letter!")
        else:
            user_guesses.append(letter)
            if letter in word_list:
                print("Nice Guess")
                if wrong_attempts < 8:
                    print("You have " + str(wrong_attempts) + " wrong guesses.")
                for count, enum in enumerate(word_list):
                    if letter == enum:
                        replace_list[count] = letter
            elif letter == word:
                print("You won!")
                loop = False
            else:
                wrong_attempts += 1
                wrong_guesses.append(letter)
                print("Oops! Try again.")
                animation_list[wrong_attempts-1]()
                print("You have " + str(wrong_attempts) + " wrong guesses!")
        stats()
        replace_word = "".join(replace_list)
        if replace_word.lower() == word.lower():
            print("You won!")
            loop = False
        if wrong_attempts == 7:
            print("Too many wrong guesses!")
            animation_list[wrong_attempts-1]()
            print("Do you want to keep playing?")
            keep = input("Y OR N: ")
            keep = keep.lower()
            if keep == "y":
                wrong_attempts = 0
            elif keep == "n":
                print("The word was " + word.lower())
                loop = False


def main():
    print("Welcome to Hangman!")
    wn = Screen()
    wn.colormode(255)
    turtle = Turtle()
    turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.shape("turtle")
    turtle.speed(0)
    name = input("What is your name: ")
    print("Hello " + name + ", I hope your day has been going well.")
    game()
    print("Thx for playing Hangman!!")
    sleep(5)
    wn.clearscreen()


if __name__ == "__main__":
    main()
