import pgzrun
TITLE="Country Quiz Game"
WIDTH=700
HEIGHT=580
marbox=Rect(0,0,700,80)
quesbox=Rect(10,100,500,120)
timebox=Rect(520,100,160,120)
ansbox1=Rect(10,240,250,150)
ansbox2=Rect(270,240,250,150)
ansbox3=Rect(10,400,250,150)
ansbox4=Rect(270,400,250,150)
skipbox=Rect(540,240,140,320)
def draw():
    screen.fill("black")
    screen.draw.filled_rect(marbox,"light blue")
    screen.draw.filled_rect(quesbox,"green")
    screen.draw.filled_rect(timebox,"orange")
    screen.draw.filled_rect(ansbox1,"orange")
    screen.draw.filled_rect(ansbox2,"red")
    screen.draw.filled_rect(ansbox3,"purple")
    screen.draw.filled_rect(ansbox4,"blue")
    screen.draw.filled_rect(skipbox,"green")
    #text boxes
    message="Welcome to the Country Quiz Game!"
    screen.draw.textbox(message,marbox,color="red")
    screen.draw.textbox("Skip",skipbox,color="black",angle=-90)
def movebox():
    marbox.x-=3
    if marbox.right<0:
        marbox.left=700
def update():
    pass
    movebox()
pgzrun.go()