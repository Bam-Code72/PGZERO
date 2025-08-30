import pgzrun,random
WIDTH=740
HEIGHT=518
score=0
Go=False
target1=Actor("fuel image.png")
target1.pos=600,200
target2=Actor("car image.png")
target2.pos=100,260
def draw():
    screen.blit("cityimage.jpg",(0,0))
    screen.draw.text("Score:"+str(score),(20,20),color="red")
    target1.draw()
    target2.draw()
def move():
    x=random.randint(50,700)
    y=random.randint(50,450)
    target1.pos=(x,y)
def update():
    pass
    global score
    #keyboard events
    if keyboard.left:
        target2.x-=4
    if keyboard.right:
        target2.x+=4
    if keyboard.up:
        target2.y-=4
    if keyboard.down:
        target2.y+=4
    if target2.colliderect(target1):
        move()
        score=score+10
pgzrun.go()