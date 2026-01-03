import pgzrun,random,itertools
WIDTH=600
HEIGHT=650
Actor1=Actor("block1.png")
Actor2=Actor("rocket1.png")
Actor2.pos=(300,325)
#positions for the block
listpos=[(530,70),(530,580),(70,580),(70,70)]
blockpos=itertools.cycle(listpos)
def draw():
    screen.clear()
    Actor1.draw()
    Actor2.draw()
#function for block animation
def animate1():
    animate(Actor1,"bounce_end",duration=1,pos=next(blockpos))
animate1()
clock.schedule_interval(animate1,1.5)
def direction1():
    x=random.randint(240,360)
    y=random.randint(240,410)
    Actor2.target=x,y
    targetangle=Actor2.angle_to(Actor2.target)
    targetangle+=360*((Actor2.angle-targetangle+180)//360)
    animate(Actor2,angle=targetangle,duration=0.5,on_finished=move1)
def move1():
    storanimate=animate(Actor2,tween='accel_decel',pos=Actor2.target,duration=Actor2.distance_to(Actor2.target)/200,on_finished=direction1,)
direction1()
pgzrun.go()