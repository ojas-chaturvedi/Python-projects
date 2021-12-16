#import modules needed
import os
import random
# import pygame
import tkinter as tkr
import turtle
import time
import winsound
#clean file junk
os.system('cls')
#define terminal graphics
def hangman_stool():
    print('______')
    print('|     |')
    print('|')
    print('|')
    print('|')
    print('|____')
def hangman_head():
    print('_______')
    print('|      |')
    print('|      O')
    print('|')
    print('|')
    print('|____')
def hangman_body():
    print('_______')
    print('|      |')
    print('|      O')
    print('|      |')
    print('|')
    print('|____')
def hangman_arms1():
    print('_______')
    print('|      |')
    print('|      O')
    print('|    --|')
    print('|')
    print('|____')
def hangman_arms2():
    print('_______')
    print('|      |')
    print('|      O')
    print('|    --|--')
    print('|')
    print('|____')
def hangman_leg1():
    print('_______')
    print('|      |')
    print('|      O')
    print('|    --|--')
    print("|      /")
    print('|____')
def hangman_leg2():
    print('_______')
    print('|      |')
    print('|      O')
    print('|    --|--')
    print("|      /\\")
    print('|____')
#terminal game
def hangman_game_boring():
    attempt = 0
    letter = '?'
    playing = True
    options = True
    game = True
    while game == True:
        while options == True:
            print('You will have to choose a category or you can input your own word.')
            print('**Words may include spaces')
            print('**not case sensitive')
            print('1 = Fruits')
            print('2 = Vegetables')
            print('3 = Colors')
            print('4 = School items')
            print('5 = Clothes')
            print('6 = Candy Brands')
            print('7 = Dessert items')
            print('8 = Flavors of Ice Cream')
            print('9 = Meals')
            print('10 = Types of peppers')
            print('11 = Sports')
            print ('ENG = Entire English dictionary')
            print('I = Input your own word')
            choice_word = '?'
            choice_word = input('Choose a group: ')
            choice_word=choice_word.upper()
            if choice_word == '1':
                with open("Fruits.txt",'r')as f:
                    lines = f.readlines()
                clean_fruits = []
                for one_line in lines:
                    clean_fruits.append(one_line.strip())
                word = random.choice(clean_fruits)
                options = False
            elif choice_word == '2':
                with open("vegetables.txt",'r')as f:
                    lines = f.readlines()
                clean_vegetables = []
                for one_line in lines:
                    clean_vegetables.append(one_line.strip())
                word = random.choice(clean_vegetables)
                options = False
            elif choice_word == '3':
                with open("Colors.txt",'r')as f:
                    lines = f.readlines()
                clean_colors = []
                for one_line in lines:
                    clean_colors.append(one_line.strip())
                word = random.choice(clean_colors)
                options = False
            elif choice_word == '4':
                with open("School items.txt",'r')as f:
                    lines = f.readlines()
                clean_school = []
                for one_line in lines:
                    clean_school.append(one_line.strip())
                word = random.choice(clean_school)
                options = False
            elif choice_word == '5':
                with open("Clothes.txt",'r')as f:
                    lines = f.readlines()
                clean_clothes = []
                for one_line in lines:
                    clean_clothes.append(one_line.strip())
                word = random.choice(clean_clothes)
                options = False
            elif choice_word == '6':
                with open("candy.txt",'r')as f:
                    lines = f.readlines()
                clean_candy = []
                for one_line in lines:
                    clean_candy.append(one_line.strip())
                word = random.choice(clean_candy)
                options = False
            elif choice_word == '7':
                with open("dessert.txt",'r')as f:
                    lines = f.readlines()
                clean_dessert = []
                for one_line in lines:
                    clean_dessert.append(one_line.strip())
                word = random.choice(clean_dessert)
                options = False
            elif choice_word == '8':
                with open("flavors of icecream.txt",'r')as f:
                    lines = f.readlines()
                clean_ice_cream = []
                for one_line in lines:
                    clean_ice_cream.append(one_line.strip())
                word = random.choice(clean_ice_cream)
                options = False
            elif choice_word == '9':
                with open("Meals.txt",'r')as f:
                    lines = f.readlines()
                clean_meals = []
                for one_line in lines:
                    clean_meals.append(one_line.strip())
                word = random.choice(clean_meals)
                options = False
            elif choice_word == '10':
                with open("peppers.txt",'r')as f:
                    lines = f.readlines()
                clean_peppers = []
                for one_line in lines:
                    clean_peppers.append(one_line.strip())
                word = random.choice(clean_peppers)
                print("**Words may include the word pepper")
                options = False
            elif choice_word == '11':
                with open("Sports.txt",'r')as f:
                    lines = f.readlines()
                clean_sports = []
                for one_line in lines:
                    clean_sports.append(one_line.strip())
                word = random.choice(clean_sports)
                options = False
            elif choice_word == 'ENG':
                with open("english_dictionary.txt",'r')as f:
                    lines = f.readlines()
                clean_dictionary = []
                for one_line in lines:
                    clean_dictionary.append(one_line.strip())
                word = random.choice(clean_dictionary)
                options = False
            elif choice_word == 'I':
                word = input('Input your own word: ')
                options = False
            else:
                print('You must have typed something wrong! Make sure everything is the exact same.')
        word_list = list(word)
        cool_list_word = " ".join(word_list)
        playGame = True
        def printreplace(replace):
            print("Your word is: " + ' '.join(replace))
        def printWrong():
            print('Your wrong guesses are: ' + ' '.join(wrong_guesses))
        def printGuesses():
            print('Your guesses are: ' + ' '.join(user_guesses))
        def all_guesses():
            printreplace(replace)
            printWrong()
            printGuesses()
        print('There are ' + str(len(word_list)) + ' letters in this word')
        wrong_guesses = []
        user_guesses = []
        user_guesses_list = []
        replace = ['_'] * len(word)
        print('You can have 5 wrong guesses! One more and you lose!!')
        if playGame == True:
            hangman_stool()
            while playing == True:
                letter = input('Guess a letter, or the word: ')
                letter = letter.lower()
                if letter in user_guesses:
                    print('You already guessed this letter!')
                    all_guesses()
                else:
                    user_guesses.append(letter)
                    if letter in word_list:
                        print('Nice Guess')
                        if attempt < 4:
                            print('You have '+ str(attempt)+ ' wrong guesses.')
                        for count,enum in enumerate(word_list):
                            if letter == enum:
                                replace[count] = letter
                        all_guesses()
                    elif letter == word:
                        print('You won!!')
                        playing = False
                    else:
                        attempt += 1
                        wrong_guesses.append(letter)
                        print("Oops! Try again.")
                        if attempt == 1:
                            hangman_head()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 2:
                            hangman_body()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 3:
                            hangman_arms1()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 4:
                            hangman_arms2()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 5:
                            hangman_leg1()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        all_guesses()
                joinedlist = ''.join(replace)
                if joinedlist.lower() == word.lower():
                    print('You won!')
                    playing = False
                if attempt == 6:
                        print('Too many wrong guesses!')
                        hangman_leg2()
                        print('Do you want to keep playing?')
                        keep = input('Y OR N?')
                        keep = keep.upper()
                        if keep == 'Y':
                            attempt = 0
                        if keep == 'N':
                            print('The word was '+word.lower())
                        playing = False
            ns = (name, attempt)
            scoreboard.append(ns)
            continuegame = input('Would you like to play again? Y to continue, any other key to quit: ')
            continuegame = continuegame.upper()
            if continuegame == 'Y':
                playGame = True
                options = True
                playing = True
                wrong_guesses = []
                user_guesses = []
                user_guesses_list = []
                attempt = 0
            else:
                print('Thx for playing Hangman!!')
                game = False
def hangman_game_cool():
    def hangman_turtle_stool():
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
    def hangman_turtle_head():
        turtle.penup()
        turtle.fd(28)
        turtle.left(90)
        turtle.fd(28)
        turtle.right(90)
        turtle.pendown()
        for i in range(450):
            turtle.right(1)
            turtle.fd(0.5)
        turtle.left(90)
    def hangman_turtle_body1():
        turtle.fd(25)
        
    def hangman_turtle_arm1():
        turtle.left(30)
        turtle.fd(75)
        turtle.back(75)
        
    def hangman_turtle_arm2():
        turtle.right(60)
        turtle.fd(75)
        turtle.back(75)
        
    def hangman_turtle_body2():
        turtle.left(30)
        turtle.fd(75)
        
    def hangman_turtle_leg1():
        turtle.left(30)
        turtle.fd(75)
        turtle.back(75)
    
    def hangman_turtle_leg2():
        turtle.back(75)
        turtle.right(60)
        turtle.fd(75)
        turtle.back(75)
        turtle.left(30)
        
    attempt = 0
    letter = '?'
    playing = True
    options = True
    game = True
    while game == True:
        while options == True:
            print('You will have to choose a category or you can input your own word.')
            print('**Words may include spaces')
            print('**not case sensitive')
            print('1 = Fruits')
            print('2 = Vegetables')
            print('3 = Colors')
            print('4 = School items')
            print('5 = Clothes')
            print('6 = Candy Brands')
            print('7 = Dessert items')
            print('8 = Flavors of Ice Cream')
            print('9 = Meals')
            print('10 = Types of peppers')
            print('11 = Sports')
            print ('ENG = Entire English dictionary')
            print('I = Input your own word')
            choice_word = '?'
            choice_word = input('Choose a group: ')
            choice_word=choice_word.upper()
            if choice_word == '1':
                with open("Fruits.txt",'r')as f:
                    lines = f.readlines()
                clean_fruits = []
                for one_line in lines:
                    clean_fruits.append(one_line.strip())
                word = random.choice(clean_fruits)
                options = False
            elif choice_word == '2':
                with open("vegetables.txt",'r')as f:
                    lines = f.readlines()
                clean_vegetables = []
                for one_line in lines:
                    clean_vegetables.append(one_line.strip())
                word = random.choice(clean_vegetables)
                options = False
            elif choice_word == '3':
                with open("Colors.txt",'r')as f:
                    lines = f.readlines()
                clean_colors = []
                for one_line in lines:
                    clean_colors.append(one_line.strip())
                word = random.choice(clean_colors)
                options = False
            elif choice_word == '4':
                with open("School items.txt",'r')as f:
                    lines = f.readlines()
                clean_school = []
                for one_line in lines:
                    clean_school.append(one_line.strip())
                word = random.choice(clean_school)
                options = False
            elif choice_word == '5':
                with open("Clothes.txt",'r')as f:
                    lines = f.readlines()
                clean_clothes = []
                for one_line in lines:
                    clean_clothes.append(one_line.strip())
                word = random.choice(clean_clothes)
                options = False
            elif choice_word == '6':
                with open("candy.txt",'r')as f:
                    lines = f.readlines()
                clean_candy = []
                for one_line in lines:
                    clean_candy.append(one_line.strip())
                word = random.choice(clean_candy)
                options = False
            elif choice_word == '7':
                with open("dessert.txt",'r')as f:
                    lines = f.readlines()
                clean_dessert = []
                for one_line in lines:
                    clean_dessert.append(one_line.strip())
                word = random.choice(clean_dessert)
                options = False
            elif choice_word == '8':
                with open("flavors of icecream.txt",'r')as f:
                    lines = f.readlines()
                clean_ice_cream = []
                for one_line in lines:
                    clean_ice_cream.append(one_line.strip())
                word = random.choice(clean_ice_cream)
                options = False
            elif choice_word == '9':
                with open("Meals.txt",'r')as f:
                    lines = f.readlines()
                clean_meals = []
                for one_line in lines:
                    clean_meals.append(one_line.strip())
                word = random.choice(clean_meals)
                options = False
            elif choice_word == '10':
                with open("peppers.txt",'r')as f:
                    lines = f.readlines()
                clean_peppers = []
                for one_line in lines:
                    clean_peppers.append(one_line.strip())
                word = random.choice(clean_peppers)
                print("**Words may include the word pepper")
                options = False
            elif choice_word == '11':
                with open("Sports.txt",'r')as f:
                    lines = f.readlines()
                clean_sports = []
                for one_line in lines:
                    clean_sports.append(one_line.strip())
                word = random.choice(clean_sports)
                options = False
            elif choice_word == 'ENG':
                with open("english_dictionary.txt",'r')as f:
                    lines = f.readlines()
                clean_dictionary = []
                for one_line in lines:
                    clean_dictionary.append(one_line.strip())
                word = random.choice(clean_dictionary)
                options = False
            elif choice_word == 'I':
                word = input('Input your own word: ')
                options = False
            else:
                print('You must have typed something wrong! Make sure everything is the exact same.')
        word_list = list(word)
        cool_list_word = " ".join(word_list)
        playGame = True
        print('There are ' + str(len(word_list)) + ' letters in this word')
        wrong_guesses = []
        user_guesses = []
        user_guesses_list = []
        replace = ['_'] * len(word)
        hangman_turtle_stool()
        print('You can have 6 wrong guesses! One more and you lose!!')
        def printreplace(replace):
            print("Your word is: " + ' '.join(replace))
        def printWrong():
            print('Your wrong guesses are: ' + ' '.join(wrong_guesses))
        def printGuesses():
            print('Your guesses are: ' + ' '.join(user_guesses))
        def all_guesses():
            printreplace(replace)
            printWrong()
            printGuesses()
        printreplace(replace)
        if playGame == True:
            while playing == True:
                letter = input('Guess a letter, or the word: ')
                letter = letter.lower()
                if letter in user_guesses:
                    print('You already guessed this letter!')
                    all_guesses()
                else:
                    user_guesses.append(letter)
                    if letter in word_list:
                        print('Nice Guess')
                        if attempt < 8:
                            print('You have '+ str(attempt)+ ' wrong guesses.')
                        for count,enum in enumerate(word_list):
                            if letter == enum:
                                replace[count] = letter
                        all_guesses()
                    elif letter == word:
                        print('You won!')
                        playing = False
                    else:
                        attempt += 1
                        wrong_guesses.append(letter)
                        print("Oops! Try again.")
                        if attempt == 1:
                            hangman_turtle_head()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 2:
                            hangman_turtle_body1()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 3:
                            hangman_turtle_arm1()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 4:
                            hangman_turtle_arm2()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 5:
                            hangman_turtle_body2()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        elif attempt == 6:
                            hangman_turtle_leg1()
                            print("You have " + str(attempt) + ' wrong guesses!')
                        all_guesses()
                joinedlist = ''.join(replace)
                if joinedlist.lower() == word.lower():
                    print('You won!')
                    playing = False
                if attempt == 7:
                        print('Too many wrong guesses!')
                        hangman_turtle_leg2()
                        print('Do you want to keep playing?')
                        keep = input('Y OR N?')
                        keep = keep.upper()
                        if keep == 'Y':
                            attempt = 0
                        if keep == 'N':
                            print('The word was '+word.lower())
                        playing = False
            ns = (name,attempt)
            scoreboard.append(ns)
            continuegame = input('Would you like to play again? Y to continue, any other key to quit: ')
            continuegame = continuegame.upper()
            if continuegame == 'Y':
                playGame = True
                options = True
                playing = True
                wrong_guesses = []
                user_guesses = []
                user_guesses_list = []
                attempt = 0
            else:
                print('Thx for playing Hangman!!')
                game = False
print('WELCOME TO HANGMAN!!')
print('How many ppl will be playing?')
ppl = '?'
ppl = input('Amount of ppl: ')
turn = 0
wn = turtle.Screen()
turtle = turtle.Turtle()
scoreboard = []
while str(turn) != ppl:
    name = input('What is your name: ')
    print('Hello ' + name + ', I hope your day has been going well.')
    print('In this game, there are 2 types of graphics')
    print('1 = Turtle (much cooler)')
    print('**will need to enlarge the window when it opens and plz dont close the window')
    print('**after each wrong letter, will have to wait for the turtle to draw the body part')
    print('2 = Terminal (boring)')
    graphics = '?'
    graphics = input('Which one do you choose: ')
    if graphics == '1':
        turn = turn + 1
        wn.colormode(255)
        turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        turtle.shape('turtle')
        turtle.speed(0)
        hangman_game_cool()
        time.sleep(5)
        wn.clearscreen()
    elif graphics == '2':
        turn = turn + 1
        hangman_game_boring()
    else:
        print('You must have typed something wrong! Make sure you typed a number and not the whole word!')
print('Scoreboard: ')
scoreboard.sort()
print(scoreboard)
print('The number represents how many letters you got wrong, so person with lowest number wins')
