import pgzrun,random
WIDTH=612
HEIGHT=382
Alien=Actor("alien1.png")
Astro=Actor("astronaut1.png")
Astro.pos=(300,362)
x=random.randint(30,580)
Alien.pos=(x,40)
Bullets=[]
def draw():
    screen.blit("space bg.jpg",(0,0))
    Alien.draw()
    Astro.draw()
    for i in Bullets:
        i.draw()
def update():
    global Astro
    if keyboard.a:
        Astro.x-=3.5
        if Astro.x<10:
            Astro.x=10
    if keyboard.d:
        Astro.x+=3.5
        if Astro.x>600:
            Astro.x=600
    Alien.y+=2.5
    if Alien.y==370:
        x=random.randint(30,580)
        Alien.pos=(x,40)
    for i in Bullets:
        i.y-=2
def on_mouse_down(pos,button):
    if button==mouse.LEFT:
        Laser=Actor("laser1.png")
        Bullets.append(Laser)
        Laser.x=Astro.x
        Laser.y=Astro.y-70
pgzrun.go()