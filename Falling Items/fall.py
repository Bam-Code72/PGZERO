import random,pgzrun
WIDTH=800
HEIGHT=600
#gaming variables
score=0
gam0=False
gamW=False
level=1
levtotal=7
speed=9
fruitlist=["apple1.png","banana1.png","blueberry1.png","orange1.png","pear1.png"]
fall=[]
targetitem=None
def draw():
    screen.blit("farmbg.webp",(0,0))
    if gam0==True:
        screen.fill("black")
        screen.draw.text("You Lose!,Your level:"+str(level),(240,280),fontsize=35,color="red")
    elif gamW==True:
        screen.fill("black")
        screen.draw.text("You Win!,You completed all levels!",(240,280),fontsize=35,color="green")
    else:

        for i in fall:
            i.draw()
        screen.draw.text("Level "+str(level)+":",(30,30),fontsize=35,color="red")
        screen.draw.text(f"Click the {targetitem.split('.')[0].capitalize()}!",(320,30),fontsize=40,color="blue")
def update():
    global fall,level,gam0,gamW
    if gam0 or gamW:
        return
    if len(fall)==0:
        fall=drop(level)
#functions for falling items
def drop(extra):
    global targetitem
    minilist=[]
    targetitem=random.choice(fruitlist)
    wrongitem=random.choices([i for i in fruitlist if i != targetitem],k=extra)
    complist=[targetitem]+wrongitem
    random.shuffle(complist)
    space=WIDTH/(len(complist)+1)
    for i,img in enumerate(complist):
        Actor1=Actor(img)
        Actor1.active=True
        Actor1.x=(i+1)*space
        Actor1.y=0
        minilist.append(Actor1)
        animate(Actor1,duration=max(1,speed-level),on_finished=groundcheck,y=HEIGHT)
    return minilist
def groundcheck(actor):
    global gam0,targetitem
    if not actor.active:
        return
    if actor.image==targetitem:
        gam0=True
def GO():
    global gam0
    gam0=True
def on_mouse_down(pos):
    global fall,level,gam0,gamW
    for i in fall:
        if i.collidepoint(pos):
            if i.image==targetitem:
                if level==levtotal:
                    gamW=True
                else:
                    level+=1
                    for a in fall:
                        a.active=False
                    fall=[]
            else:
                GO()
pgzrun.go()
