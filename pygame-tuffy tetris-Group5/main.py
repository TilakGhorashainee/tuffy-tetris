import pygame
import sys
from tetris import Tetris, PygameView
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play_survival():
    t = Tetris(PygameView)
    t.IS_SURVIVAL_MODE = True
    t.main()
    main_menu()

def play_sprint():
    t = Tetris(PygameView)
    t.IS_SPRINT_MODE = True
    t.main()
    main_menu()


def gameMode():
    while True:
        SCREEN.blit(BG, (0, 0))

        MODE_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Tuffy Tetris", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))

        SURVIVAL_BUTTON = Button(image=pygame.image.load("assets/Mode Rect.png"), pos=(300, 225),
                          text_input="SURVIVAL MODE", font=get_font(38), base_color="#d7fcd4", hovering_color="White")  
        SPRINT_BUTTON = Button(image=pygame.image.load("assets/Mode Rect.png"), pos=(300, 370),
                        text_input="SPRINT MODE", font=get_font(38), base_color="#d7fcd4", hovering_color="White") 

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MODES_BACK = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 525),
                              text_input="BACK", font=get_font(38), base_color="#d7fcd4", hovering_color="White")

        MODES_BACK.changeColor(MODE_MOUSE_POS)
        MODES_BACK.update(SCREEN)
        

        for button in [SURVIVAL_BUTTON, SPRINT_BUTTON]:
            button.changeColor(MODE_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                      
                if SURVIVAL_BUTTON.checkForInput(MODE_MOUSE_POS):
                    play_survival()
                if SPRINT_BUTTON.checkForInput(MODE_MOUSE_POS):
                    play_sprint()
                if MODES_BACK.checkForInput(MODE_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(16).render(
            "This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(300, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(300, 460),
                              text_input="BACK", font=get_font(18), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Tuffy Tetris", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 225),
                             text_input="PLAY", font=get_font(38), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(300, 375),
                                text_input="OPTIONS", font=get_font(38), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300, 525),
                             text_input="QUIT", font=get_font(38), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):    
                    gameMode()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
