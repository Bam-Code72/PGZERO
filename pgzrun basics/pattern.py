import pgzrun
WIDTH=500
HEIGHT=500
def draw():
    wid=200
    hei=500
    for i in range(20):
        r1=Rect((0,0),(wid,hei))
        r1.center=250,250
        screen.draw.rect(r1,("yellow"))
        wid=wid+10
        hei=hei-10
def update():
    pass

pgzrun.go()
