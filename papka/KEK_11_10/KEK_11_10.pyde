x=1
dirx=12
def setup():
     size (1000 ,1000)
     frameRate(3)
def draw():
    global x,dirx
    background (200 ,0 ,0)
    rect (500 ,500 ,x ,x)
    x=x+10
    if x > 120:
        background (200 ,0 ,0)
        rect (500 ,500 ,x ,x)
        dirx=-12
        x=x+dirx
    if x < 110:
        background (200 ,0 ,0)
        rect (500 ,500 ,x ,x)
        dirx=12
        x=x+dirx
