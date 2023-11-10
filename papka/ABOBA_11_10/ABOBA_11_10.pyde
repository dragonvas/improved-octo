x=1
dirx=100
def setup():
    frameRate(120)
    size (1000 ,1000)
def draw():
    global x,dirx
    background (200 ,0 ,0)
    ellipse (500 ,x ,50 ,50)
    x=x+dirx
    if x > 990:
        background (200 ,0 ,0)
        ellipse (500 ,x ,50 ,50)
        dirx=-100
        x=x+dirx
    if x < 10:
        background (200 ,0 ,0)
        ellipse (500 ,x ,50 ,50)
        dirx=100
        x=x+dirx
