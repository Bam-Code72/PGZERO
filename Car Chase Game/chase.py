import pgzrun,random
WIDTH=740
HEIGHT=518
score=0
lives=5
Go=False
target1=Actor("fuel image.png")
target1.pos=600,200
target2=Actor("car image.png")
target2.pos=100,260
target3=Actor("treeimage.png")
target3.pos=300,300
def draw():
    screen.blit("cityimage.jpg",(0,0))
    screen.draw.text("Score:"+str(score),(20,20),color="red")
    screen.draw.text("Lives:"+str(lives),(600,20),color="red")
    target1.draw()
    target2.draw()
    target3.draw()
    if Go:
        screen.fill("black")
        if score<100:
            screen.draw.text("GAME OVER:You have lost! with a score of:"+str(score),(200,200),color="red")
        else:
            screen.draw.text("GAME OVER:You have won! with a score of:"+str(score),(200,200),color="red")
def move():
    x=random.randint(50,700)
    y=random.randint(50,450)
    target1.pos=(x,y)
def move2():
    a=random.randint(50,700)
    b=random.randint(50,450)
    target3.pos=(a,b)
def go():
    global Go
    Go=True

def update():
    pass
    global score,lives
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
    if target2.colliderect(target3):
        move2()
        lives=lives-1
        if lives==0:
            go()
clock.schedule(go,30)
clock.schedule_interval(move2,2)
pgzrun.go()
