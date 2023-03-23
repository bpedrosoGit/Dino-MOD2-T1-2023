from Chaves_Runner.utils.constants import SANDAIL
from Chaves_Runner.components.obstacles.obstacle import Obstacle


class Sandail(Obstacle):
    def __init__(self):
        super().__init__(SANDAIL, 0)
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0