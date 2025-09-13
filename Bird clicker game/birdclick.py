import pgzrun,random,time
WIDTH=700
HEIGHT=400
listb=[]
bnum=8
lista=[]
def birds():
    global bnum
    for i in range(bnum):
        bird=Actor("bird image.png")
        x=random.randint(20,680)
        y=random.randint(20,380)
        bird.pos=(x,y)
        listb.append(bird)
def draw():
    sqnum=1
    screen.blit("cartoon field.jpg",(0,0))
    for a in listb:
        a.draw()
        screen.draw.text(str(sqnum),(a.pos[0],a.pos[1]+20),color="blue")
        sqnum+=1
def mouse_down():

birds()
pgzrun.go()