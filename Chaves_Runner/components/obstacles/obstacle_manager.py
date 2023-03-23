import pygame
import random
from Chaves_Runner.components.obstacles.enemy import Enemy
from Chaves_Runner.components.obstacles.sandail import Sandail


class ObstacleManager:

    def init(self):
        self.obstacles = []

    def update(self, game):
        image_list = [Enemy(), Sandail()]
        if len(self.obstacles) == 0:
            self.obstacles.append(image_list[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.chaves_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
