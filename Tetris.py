from gameengine import GameEngine
from gameengine import pygame
if __name__ == "__main__":
    game = GameEngine()
    game.initialize()
    while True:
        for event in pygame.event.get():
            game.event_handler(event)
        game.game_loop()