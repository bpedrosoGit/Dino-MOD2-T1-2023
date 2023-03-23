import random

from Chaves_Runner.utils.constants import MADRUGA, TNT
from Chaves_Runner.components.obstacles.obstacle import Obstacle


class Enemy(Obstacle):

    ENEMY = [
        (MADRUGA, 300),
        (TNT, 325),
    ]

    def __init__(self):
        image, enemy_pos = self.ENEMY[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = enemy_pos
