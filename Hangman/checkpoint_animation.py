# Imports
import os; import random; import turtle as t; import time;

class Main:
    def __init__(self):
        pass;
    def animation_stool(self):
        t.penup(); t.goto(-200, 0); t.pendown();
        t.left(90);
        t.fd(200);
        t.back(200);
        t.left(45);
        t.back(125);
        t.fd(125);
        t.right(90);
        t.back(125);
        t.penup(); t.goto(-200, 200); t.pendown();
        t.right(45);
        t.fd(150);
        t.right(90);
        t.fd(50);
    def animation_head(self):
        t.penup(); t.fd(28); t.left(90); t.fd(28); t.right(90); t.pendown();
        for i in range(450):
            t.right(1); t.fd(0.5);
        t.left(90);
    def animation_upperBody(self):
        t.fd(25);
    def animation_lowerBody(self):
        t.left(30);
        t.fd(75);
    def animation_arm1(self):
        t.left(30);
        t.fd(75);
        t.back(75);
    def animation_arm2(self):
        t.right(60);
        t.fd(75);
        t.back(75);
    def animation_leg1(self):
        t.left(30);
        t.fd(75);
        t.back(75);
    def animation_leg2(self):
        t.back(75);
        t.right(60);
        t.fd(75);
        t.back(75);
        t.left(30);
