import pygame
import sys
class GameEngine:
    def __init__(self):
        self.map= [[0] * 20 for _ in range(10)]
        self.window_size=(800,600)
        self.screen = None
        self.color = {1:(255,0,0),2:(0,255,0),3:(0,0,255)}
        self.blocks = { "L_shape":[
    [0, 1],
    [0, 1],
    [1, 1]
] ,"T_shape":[[0,1],[1,1],[0,1]]}
        
    def initialize(self): 
            pygame.init()
            pygame.font.init()
            self.screen = pygame.display.set_mode(self.window_size)

    def event_handler(self,event):
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    def map_(self):
        return self.map

    def game_draw(self):
        for i,column in enumerate(self.map):
            for j,block in enumerate(column):
                if block != 0:
                    pygame.draw.rect(self.screen,self.color[block],((i+10)*25,(j+1)*25,25,25))
    def add_blocks_on_map(self,block_shape):
        block=self.blocks[block_shape]
        for i in range(len(block)):
            for j in range(len(block[i])):
                self.add_block( 4+i ,j, block[i][j])
    def add_block(self,column,row,block_type):
        if 0<= column<10 and 0 <=row <20:
            self.map[column][row] = block_type
    def move_map(self):

        temp_map = [column[:] for column in self.map]

        for i in range(len(self.map)):
            for j in range(len(self.map[i]) - 1, 0, -1):
                if self.map[i][j] == 0:
                    self.map[i][j] = self.map[i][j-1]
                    self.map[i][j-1] = 0

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] != 0 and temp_map[i][j] == 0:
                    pass


    def game_loop(self):
        self.screen.fill((0, 0, 0))
        self.move_map()
        self.game_draw()
        pygame.display.update()


                

