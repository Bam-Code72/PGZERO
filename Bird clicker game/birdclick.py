import pgzrun,random,time
WIDTH=700
HEIGHT=400
listb=[]
bnum=8
lista=[]
birdcount=0
startime=0
totaltime=0
def birds():
    global bnum,startime
    for i in range(bnum):
        bird=Actor("bird image.png")
        x=random.randint(30,680)
        y=random.randint(30,380)
        bird.pos=(x,y)
        listb.append(bird)
    #starting the timer
    startime=time.time()
def draw():
    global birdcount,bnum,totaltime,startime
    sqnum=1
    screen.blit("cartoon field.jpg",(0,0))
    for a in listb:
        a.draw()
        screen.draw.text(str(sqnum),(a.pos[0],a.pos[1]+20),color="blue")
        sqnum+=1
    for b in lista:
        screen.draw.line(b[0],b[1],"red")
    #showing timer on the screen
    if birdcount<bnum:
        totaltime=time.time()-startime
        totaltime=round(totaltime,1)
        screen.draw.text("Time:"+str(totaltime),(20,20),color="red")
    else:
        screen.fill("black")
        screen.draw.text("Your total time was:"+str(totaltime),(120,160),color="red",fontsize=60)
def on_mouse_down(pos):
    global birdcount,bnum,lista,listb
    if birdcount<bnum:
        if listb[birdcount].collidepoint(pos):
            if birdcount!=0:
                lista.append((listb[birdcount-1].pos,listb[birdcount].pos))
            birdcount=birdcount+1
        else:
            lista=[]
            birdcount=0
def update():
    pass
birds()
pgzrun.go()
