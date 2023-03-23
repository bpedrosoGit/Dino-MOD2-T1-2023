import pygame
import os

# Global Constants
TITLE = "Chrome chaves Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))


TNT = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/TNT1.png")),(80, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/TNT2.png")),(80, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/TNT3.png")),(80, 100)),
]
MADRUGA = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Madruga1.png")),(100,150)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Madruga2.png")),(100,150)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Madruga3.png")),(100,150)),
]

SANDAIL = [
    pygame.image.load(os.path.join(IMG_DIR, "Sandail/Sandail1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sandail/Sandail2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

IMG0DEATH = pygame.transform.scale(pygame.image.load(
    "Chaves_Runner/assets/background/gameBGStart.png"
), (SCREEN_WIDTH, SCREEN_HEIGHT))
IMGDEATH = pygame.transform.scale(pygame.image.load(
    f"Chaves_Runner/assets/Xtras/cemiterio.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
lapide = pygame.transform.scale(pygame.image.load(
    f"Chaves_Runner/assets/Xtras/lapide.png"
), (550, 400))
