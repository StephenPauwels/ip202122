import matplotlib.pyplot as plt
from math import sin,cos,sqrt,pi


def draw_line(x1,y1,x2,y2,color="b"):
    plt.plot([x1,x2], [y1,y2],color)

def display():
    plt.show()
    
class Turtle:
    def __init__(self):
        self._x=0
        self._y=0
        self._angle=0
        self._pendown=True
        
    def forward(self,length):
        nx = self._x + cos(2*pi*self._angle/360)*length
        ny = self._y + sin(2*pi*self._angle/360)*length
        self.goto(nx,ny)
        
    def right(self,angle):
        self._angle-=angle
        self._angle=self._angle%360
    
    def left(self,angle):
        self._angle+=angle
        self._angle=self._angle%360
    
    def goto(self,nx,ny):
        if self._pendown:
            draw_line(self._x,self._y,nx,ny)
        self._x = nx
        self._y = ny
    
    def pendown(self):
        self._pendown=True
    
    def penup(self):
        self._pendown=False
    

def forward(length):
    global default
    default.forward(length)    

def goto(x,y):
    global default
    default.goto(x,y)
    
def right(angle):
    global default
    default.right(angle)

def left(angle):
    global default
    default.left(angle)
    
def penup():
    global default
    default.penup()

def pendown():
    global default
    default.pendown()

def reset():
    global default
    global fig
    default=Turtle()
    fig = plt.figure()
    fig.clf()
    plt.axis("square")
    #plt.axis("off")
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    fig.set_size_inches(10, 10)

#default = Turtle()
#fig = plt.figure()
#reset()
