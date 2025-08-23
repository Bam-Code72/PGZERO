import pgzrun,random
WIDTH=500
HEIGHT=500
def draw():
    radius=250
    r=255
    g=0
    b=random.randint(0,255)
    for i in range(30):
        screen.draw.circle((250,250),radius,(r,g,b))
        radius=radius-10
        r=r-5
        g=g+5
def update():
    pass
pgzrun.go()