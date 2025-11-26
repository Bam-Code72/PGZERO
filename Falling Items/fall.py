import random,pgzrun
WIDTH=800
HEIGHT=600
#gaming variables
score=0
gam0=False
level=1
levtotal=7
speed=3
fruitlist=["apple1.png","banana1.png","blueberry1.png","orange.png","pear1.png"]
fall=[]
targetitem=None
def draw():
    screen.blit("farmbg.webp",(0,0))
def update():
    pass
#functions for falling items
def drop(extra):
    global targetitem
    minilist=[]
    targetitem=random.choice(fruitlist)
    wrongitem=random.choices([i for i in fruitlist if i != targetitem],k=extra)
    complist=[targetitem]+[wrongitem]
    random.shuffle(complist)
    space=WIDTH/(len(complist)+1)
    for i,img in enumerate(complist):
        Actor1=Actor(img)
        Actor1.active=True
        Actor1.x=(i+1)*space
        Actor1.y=0
        minilist.append(Actor1)
        animate(Actor1,duration=max(1,speed-level),on_finished=lambda a=Actor1:groundcheck(a),y=HEIGHT)
def groundcheck(actor):
    global gam0,targetitem
    if not actor.active:
        return
    if actor.image==targetitem:
        gam0=True

pgzrun.go()