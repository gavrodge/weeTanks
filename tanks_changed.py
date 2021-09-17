import turtle
#import pygame
# asdfsafas

print('swag on these tanks')

tnks = turtle.Screen()
tnks.title("wee tanks - gavchanger")
tnks.bgcolor('Wheat')
#add different arenas and themes
#classic wood, space and lasers, futuristic 3d grid
#PeachPuff, Moccasin, PapayaWhip, Bisque, NavajoWhite, BurlyWood

#tank
#class?
#pick colour, multi tanks
tank = turtle.Turtle()
tank.speed(0)
tank.shape('square')
colour_prompt = input("pick a colour, if you don't know any please type 'blet'")
if colour_prompt == 'blet':
    colour_prompt = random_colour()
tank.color(colour_prompt)
tank.penup()    #actually want this activated so moving tanks leave a trace

#bullet
bullet=turtle.Turtle()
bullet.speed(0)

bullet.shape('classic')
#bomb

#enemy tanks
#gold, brown, turquoise, yellow, red, green, purple, None
# https://nintendo.fandom.com/wiki/Tanks!#Tank_attributes


while True:
        tnks.update()



# to add:
# music!
# multiplatform? (iphone & android)
