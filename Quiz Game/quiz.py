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
options=[ansbox1,ansbox2,ansbox3,ansbox4]
#variables
timer=15
score=0
over=False
quest=[]
index=0
count=0
def draw():
    screen.fill("black")
    screen.draw.filled_rect(marbox,"black")
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
    screen.draw.textbox(str(timer),timebox,color="black")
    screen.draw.textbox(question[0].strip(),quesbox,color="red")
    count2=1
    for i in options:
        screen.draw.textbox(question[count2].strip(),i,color="black")
        count2=count2+1
def movebox():
    marbox.x-=3
    if marbox.right<0:
        marbox.left=700
def correct():
    global timer,question,score,quest
    score=score+50
    if len(quest)>0:
        question=readquest()
        timer=15
def on_mouse_down(pos):
    ind=1
    for i in options:
        if i.collidepoint(pos):
            if ind==int(question[5]):
                correct()
        ind+=1
def timechange():
    global timer
    if timer!=0:
        timer=timer-1
#function to read the file
def fileread():
    global count,quest
    file=open("question.txt","r")
    for i in file:
        quest.append(i)
        count=count+1
    file.close()
#reading next question
def readquest():
    global index
    index=index+1
    return quest.pop(0).split(",")
def update():
    pass
    movebox()
#scheduling timer function call
clock.schedule_interval(timechange,1)
fileread()
question=readquest()
pgzrun.go()
