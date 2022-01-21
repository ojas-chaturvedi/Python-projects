# Imports
import os; import random; import turtle; import time;

class Main:
    def __init__(self, turtle):
        wn = turtle.Screen(); wn.colormode(255);
        self.turtle = turtle.Turtle(); turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255)); turtle.shape('turtle'); turtle.speed(0);
        self.word_banks = ["fruits", "vegetables", "colors", "school_items", "clothes", "candy_brands", "dessert_items", "ice_cream_flavors", "meals", "peppers_types", "sports", "english_dictionary"];
        #self.animation_list = [self.animation_head(), self.animation_upperBody(), self.animation_arm1(), self.animation_arm2(), self.animation_lowerBody(), self.animation_leg1(), self.animation_leg2()]
        self.wrong_attempts = 0;
        self.wrong_guesses = [];
        self.guesses = [];
        self.get_word();
        self.animation_stool();
        playing = True;
        while playing:
            letter = input("Guess a letter, or the whole word: ").lower();
            if letter in self.guesses:
                print("You already guessed this letter!");
            elif letter == self.word:
                print("You won!"); playing = False;
            else:
                self.guesses.append(letter);
                if letter in self.word_list:
                    print("Nice guess!");
                    print("You have " + self.wrong_attempts + " wrong guesses left.");
                    for count, enum in enumerate(self.word_list):
                        if letter == enum:
                            self.replace_list[count] = letter;
                else:
                    self.wrong_attempts += 1; self.wrong_guesses.append(letter);
                    if self.wrong_attempts != 7:
                        print("Oops! Try again.");
                    self.animation_list[self.wrong_attempts-1];
            self.get_stats();
            self.replace_word = "".join(self.replace_list);
            if self.replace_word.lower() == self.word.lower():
                print("You won!"); playing = False;
            if self.wrong_attempts == 7:
                print('Too many wrong guesses!');
                print('Do you want to keep playing?');
                choice = input('Y OR N:').upper();
                if choice == 'Y':
                    self.wrong_attempts = 0;
                elif choice == 'N':
                    print("The word was "+ self.word.lower());
                    playing = False;
        print("Thanks for playing Hangman!");
        print("Hangman game made by OJ Chaturvedi.");



    def animation_stool(self):
        self.turtle.penup(); self.turtle.goto(-200, 0); self.turtle.pendown();
        self.turtle.left(90);
        self.turtle.fd(200);
        self.turtle.back(200);
        self.turtle.left(45);
        self.turtle.back(125);
        self.turtle.fd(125);
        self.turtle.right(90);
        self.turtle.back(125);
        self.turtle.penup(); self.turtle.goto(-200, 200); self.turtle.pendown();
        self.turtle.right(45);
        self.turtle.fd(150);
        self.turtle.right(90);
        self.turtle.fd(50);
    def animation_head(self):
        self.turtle.penup(); self.turtle.fd(28); self.turtle.left(90); self.turtle.fd(28); self.turtle.right(90); self.turtle.pendown();
        for _ in range(450):
            self.turtle.right(1); self.turtle.fd(0.5);
        self.turtle.left(90);
    def animation_upperBody(self):
        self.turtle.fd(25);
    def animation_lowerBody(self):
        self.turtle.left(30);
        self.turtle.fd(75);
    def animation_arm1(self):
        self.turtle.left(30);
        self.turtle.fd(75);
        self.turtle.back(75);
    def animation_arm2(self):
        self.turtle.right(60);
        self.turtle.fd(75);
        self.turtle.back(75);
    def animation_leg1(self):
        self.turtle.left(30);
        self.turtle.fd(75);
        self.turtle.back(75);
    def animation_leg2(self):
        self.turtle.back(75);
        self.turtle.right(60);
        self.turtle.fd(75);
        self.turtle.back(75);
        self.turtle.left(30);

    def get_word(self):
        print("Choose a word from a category or input your own word. /nWords may include spaces but not case sensitive.");
        print("1-Fruits/n2-Vegetables/n3-Colors/n4-School items/n5-Cloths/n6-Candy brands/n7-Dessert items/n8-Ice Cream flavors/n9-Meals/n10-Pepper types/n11-Sports/n12-Entire English Dictionary/n13-Input your own word");
        choice = int(input("Choose a group: "));
        if choice == 13:
            self.word = input("Enter a word: ");
        else:
            lines = open(self.word_banks[choice-1] + ".txt", "r").readlines;
            word_choices = [];
            for line in lines:
                word_choices.append(line.strip());
            self.word = random.choice(word_choices);
        self.word_list = list(self.word);
        self.replace_list = ["_"] * len(self.word);

    def get_stats(self):
        print("Your word is: " + " ".join(self.replace));
        print("Your wrong guesses are: " + " ".join(self.wrong_guesses));
        print("Your guesses are: " + " ".join(self.guesses));


main = Main(turtle);