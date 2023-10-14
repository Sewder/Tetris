from gameengine import GameEngine
from gameengine import pygame
if __name__ == "__main__":
    game = GameEngine()
    game.initialize()
    game.add_blocks_on_map("L_shape")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            game.event_handler(event)
        game.game_loop()
        clock.tick(15)
        