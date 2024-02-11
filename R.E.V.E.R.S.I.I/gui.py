import pygame
import playsound
import time

class imageHandler:
    def __init__(self):
        self.pics = dict()
        
    def loadFromFile(self, filename, id=None):
        if id == None: id - filename
        self.pics[id] = pygame.image.load(filename).convert()
        
    def loadFromSurface(self, surface, id):
        self.pics[id] = surface.convert_alpha()
        
    def render(self, surface, id, position=None, clear=False, size=None):
        if clear == True:
            surface.fill((5,2,23))
            
        if position == None:
            picX = int(surface.get_width() / 2 - self.pics[id].get_width() / 2)
        else:
            picX = position[0]
            picY = position[1]
        
        if size == None:
            surface.blit(self.pics[id], (picX, picY))
        else:
            surface.blit(pygame.transform.smoothscale(self.pics[id], size), (picX, picY))
            
#Initializes the display----------------------------------------------------------------
pygame.display.init()
screen = pygame.display.set_mode((400,400), pygame.RESIZEABLE) #uncomment for smaller windows
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # comment out for smaller windows
handler = imageHandler()

def display():
    handler.loadFromFile("filepath") #add file location here. Can also copy and paste for more images
display()

def face():
    A = 30
    B = 300
    x = 1024
    y = 768
    
    handler.render(screen, "1", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768) 
        # or replace with this line for easier coding 
        #pygame.display.update(A,B,x,y) 
    time.sleep(.2)
    handler.render(screen, "2", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "3", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "4", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "5", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "6", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "7", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "8", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "9", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render(screen, "10", (A, B), True, (x, y))
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
face()    