import pygame
import sys
class GameEngine:
    def __init__(self):
        self.map= [[1] * 20 for _ in range(10)]
        self.window_size=(800,600)
        self.screen = None
        self.color = {1:(255,0,0),2:(0,255,0),3:(0,0,255)}
        
    def initialize(self): 
            pygame.init()
            pygame.font.init()
            self.screen = pygame.display.set_mode(self.window_size)

    def event_handler(self,event):
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    def game_draw(self):
        for i,row in enumerate(self.map):
            for j,block in enumerate(row):
                if block != 0:
                    pygame.draw.rect(self.screen,self.color[block],((i+10)*25,(j+1)*25,25,25))
    def game_loop(self):
        self.screen.fill((0, 0, 0))
        self.game_draw()
        pygame.display.update()


                

