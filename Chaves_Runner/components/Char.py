import pygame
from pygame.sprite import Sprite
from Chaves_Runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5


class Char(Sprite):
    def __init__(self, name):
        self.type = DEFAULT_TYPE
        self.animation_list = self.imgChar(name)
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]
        self.chaves_rect = self.image.get_rect()
        self.chaves_rect.x = X_POS
        self.chaves_rect.y = Y_POS
        self.step_index = 0
        self.chaves_run = True
        self.chaves_jump = False
        self.chaves_duck = False
        self.jump_vel = JUMP_VEL
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        
        if self.chaves_run:
            self.run()
        elif self.chaves_jump:
            self.jump()
        elif self.chaves_duck:
            self.duck()
        if user_input[pygame.K_UP] and not self.chaves_jump or user_input[pygame.K_w] and not self.chaves_jump:
            self.chaves_run = False
            self.chaves_jump = True
            self.chaves_duck = False
        elif user_input[pygame.K_DOWN] and not self.chaves_jump or user_input[pygame.K_s] and not self.chaves_jump:
            self.chaves_run = False
            self.chaves_jump = False
            self.chaves_duck = True
        elif not self.chaves_jump and not self.chaves_duck:
            self.chaves_run = True
            self.chaves_jump = False
            self.chaves_duck = False
        if self.step_index >= 9:
            self.step_index = 0

    def imgChar(self, name):
        lista_imagens = []
        temp_list = []
        for i in range(2):
            img = pygame.transform.scale(pygame.image.load(
                f"Chaves_Runner/assets/chars/{name}/{i}.png"),(40, 80))
            temp_list.append(img)
        lista_imagens.append(temp_list)
        temp_list = []
        for i in range(4):
            img = pygame.transform.scale(pygame.image.load(
                f"Chaves_Runner/assets/chars/{name}/Jumping/{i}.png"),(40, 80))
            temp_list.append(img)
        lista_imagens.append(temp_list)
        temp_list = []
        for i in range(4):
            img = pygame.transform.scale(pygame.image.load(
                f"Chaves_Runner/assets/chars/{name}/Ducking/{i}.png"),(40, 80))
            temp_list.append(img)
        lista_imagens.append(temp_list)
        return lista_imagens

    def run(self):
        #ANIMATION
        self.action = 0
        self.image = self.animation_list[self.action][self.step_index // 5]

        ##FUNC
        self.chaves_rect = self.image.get_rect()
        self.chaves_rect.x = X_POS
        self.chaves_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        ##ANIMATION
        self.action = 1
        self.image = self.animation_list[self.action][self.step_index // 3]
        ##FUNC
        if self.chaves_jump:
            self.chaves_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -JUMP_VEL:
            self.chaves_rect_y = Y_POS
            self.chaves_jump = False
            self.jump_vel = JUMP_VEL
        self.step_index += 1
    def duck(self):
        ##ANIMATION
        self.action = 2
        self.image = self.animation_list[self.action][self.step_index // 3]
        self.update_time = pygame.time.get_ticks()

        ##FUNC
        self.chaves_rect = self.image.get_rect()
        self.chaves_rect.x = X_POS
        self.chaves_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.chaves_duck = False
        self.step_index += 1
    def draw(self, screen):
        screen.blit(self.image, (self.chaves_rect.x, self.chaves_rect.y))
