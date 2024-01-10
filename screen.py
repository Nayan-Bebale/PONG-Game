from turtle import Turtle

class Screen:
    def __init__(self, states=2):
        timmy = Turtle()
        self.window = timmy.Screen()
        # self.window.screensize(1920,1080)
        self.window.title('States')
        self.turtles = []