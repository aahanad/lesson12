#import pygame
#pygame.init()
#screen=pygame.display.set_mode((600,800))
#class Circle():
    #def __init__(self,color,size,x,y):
        #self.color=color
        #self.size=size
        #self.where=x,y
        #self.screen=screen
   # def draw (self):
        #pygame.draw.circle(self.screen,self.color,self.where,self.size)
#c1=Circle("pink",20,70,70)
#c3=Circle("pink",15,90,70)
#while True:
    #screen.fill("violet")
    #c1.draw()
    #c2.draw()
    #c3.draw()
    #pygame.draw.circle(screen,"pink",(40,70),20)
    #for event in pygame.event.get():
        #if event.type==pygame.QUIT:
            #pygame.quit()
    #pygame.display.update()
    #make a class rect
#class Rec
import pygame
pygame.init()
screen=pygame.display.set_mode((600,800))
class rect():
    def __init__(self,color,lenght,width,x,y):
        self.color=color
        self.width=width
        self.lenght=lenght
        self.x=x
        self.y=y
        self.screen=screen
    def draw (self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.lenght,self.width))
r1=rect("pink",20,70,70,20)
while True:
    screen.fill("violet")
    r1.draw()
    pygame.display.update()
