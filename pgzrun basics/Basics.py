import pgzrun
#size of the screen
WIDTH=400
HEIGHT=400
def draw():
    screen.fill("blue")
    screen.draw.text("Hello World",center=(200,200),color="orange")
    r1=Rect((300,300),(60,90))
    screen.draw.filled_rect(r1,("green"))
    #circle
    screen.draw.filled_circle((150,80),70,"pink")
#hold the output
pgzrun.go()