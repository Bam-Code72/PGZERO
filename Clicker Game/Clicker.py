import pgzrun,random
WIDTH=400
HEIGHT=400
#creating an actor
target=Actor("target.png")
def move():
    x=random.randint(45,355)
    y=random.randint(45,355)
    target.pos=x,y
def draw():
    screen.fill("light blue")
    screen.draw.text("Welcome to the Target Game!",(80,20),color="red")
    #drawing the actor
    target.draw()
move()
pgzrun.go()