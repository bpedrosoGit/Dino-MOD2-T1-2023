import pygame
from Chaves_Runner.utils.constants import *
from Chaves_Runner.components.Char import Char
from Chaves_Runner.components.obstacles.obstacle_manager import ObstacleManager
from Chaves_Runner.utils.text_utils import draw_message_component
from Chaves_Runner.components.powerups.power_up_manager import PowerUpManager




def insideMenu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Launcher.exe")
    drawBg = pygame.transform.scale(pygame.image.load('Chaves_Runner/assets/background/MenuInsideBg.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    #coins = Game.score_list
    #coins = sum(coins)
    clicked = False
    insideMenuOn = True
    #chars_have = ['chaves', 'kiko']
    while insideMenuOn:
        screen.blit(drawBg, (0,0))
        posx, posy = pygame.mouse.get_pos()
        if (posx > 0 and posx < 600) and (posy > 150 and posy < 300):
            if clicked == True:
                SelectChar()
        #if (posx > 0 and posx < 300) and (posy > 600 and posy < 1000):
            #if clicked == True:
                # Lojinha(coins)
        for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key == pygame.K_ESCAPE:
                    insideMenuOn = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True

        pygame.display.flip()

""" def Lojinha(dindin, chars_have):
    if dindin >= 500:
        chars_have.append("MJ")
    
    return chars_have """


def SelectChar():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Launcher.exe")
    drawBg = pygame.transform.scale(pygame.image.load('Chaves_Runner/assets/background/Char_choose.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgBtn = pygame.image.load("Chaves_Runner/assets/background/Jogar.png")
    imgBtnLocked = pygame.image.load("Chaves_Runner/assets/background/JogarLocked.png")
    clicked = False
    selectedChar = None
    selectchar = True
    butaum = imgBtnLocked
    while selectchar:
        
        posx, posy = pygame.mouse.get_pos()
        screen.blit(drawBg, (0,0))
        screen.blit(butaum, (500,100))

        if (posx > 500 and posx < 660) and (posy > 100 and posy < 180):
                    if clicked == True and selectedChar != None:
                        game = Game(selectedChar)
                        game.execute()


        if (posx > 0 and posx < 390) and (posy > 0 and posy < 600):
            if clicked == True:    
                selectedChar = 'chaves'
                butaum = imgBtn

        if (posx > 400 and posx < 700) and (posy > 0 and posy < 600):
            if clicked == True:    
                selectedChar = 'kiko'
                butaum = imgBtn
        #if "MJ" in chars_have:         
        if (posx > 701 and posx < 1100) and (posy > 0 and posy < 600):
            if clicked == True:    
                selectedChar = 'MJ'
                butaum = imgBtn
    
        
        clicked = False
        for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key == pygame.K_ESCAPE:
                    selectchar = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True

        pygame.display.flip()




#JOGO

class Game:
    def __init__(self, char):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.char = char
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Char(char)
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score_list = []

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
        if user_input[pygame.K_ESCAPE]:
            running = False
            insideMenu()
        
            

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((177,103,88))
        imgBG = pygame.transform.scale(pygame.image.load(('Chaves_Runner/assets/background/gameBG.png')), (SCREEN_WIDTH, (SCREEN_HEIGHT // 2)+ 90))
        self.screen.blit(imgBG, (0,0))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        draw_message_component(
            f"score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50,
        )

    def draw_power_up_time(self):
        
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"VOCÊ ESTARÁ EM MODO RUSBÉ POR MAIS {time_to_show} SEGUNDOS",
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((133,133,133))

        if self.death_count == 0:
            self.screen.blit(IMG0DEATH, (0,0))
            #draw_message_component(f"Press any tecla to começar", self.screen)
        else:
            self.screen.blit(IMGDEATH, (0,0))
            self.screen.blit(lapide, ((SCREEN_WIDTH // 2) -275, SCREEN_HEIGHT - 370))
            draw_message_component(
                "Press any Tecla to Restart", self.screen,
                pos_y_center=SCREEN_HEIGHT - 180)
            draw_message_component(f"Your pontitoszitos: {self.score}", self.screen,
                                   pos_y_center=SCREEN_HEIGHT - 150)
            draw_message_component(
                f"Counter mortitas: {self.death_count}",
                self.screen,
                pos_y_center=SCREEN_HEIGHT - 100
            )
            self.score_list.append(self.score)
            draw_message_component(
                "Press ESC to MENU", self.screen,
                pos_y_center=100)

        pygame.display.flip()

        self.handle_events_on_menu()
