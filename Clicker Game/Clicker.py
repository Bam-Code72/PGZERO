import pgzrun,random
WIDTH=400
HEIGHT=400
#creating an actor
target=Actor("target.png")
mesg1="Welcome to the Target Game!"
score=0
def move():
    x=random.randint(45,355)
    y=random.randint(45,355)
    target.pos=(x,y)
    clock.schedule_unique(miss,0.6)
def miss():
    global mesg1
    mesg1="You missed the target"
    move()
def draw():
    screen.fill("light blue")
    screen.draw.text(mesg1,(80,20),color="red")
    screen.draw.text("Score:"+str(score),(10,10),color="red")
    #drawing the actor
    target.draw()
#clicking of the mouse
def on_mouse_down(pos):
    global mesg1,score
    if target.collidepoint(pos):
        move()
        mesg1="You hit the target!"
        score=score+10
        clock.unschedule(miss)
    else:
        mesg1="You missed the target!"
move()
pgzrun.go()