from turtle import color
import pygame
import sys
from tetris import Tetris, PygameView
from button import Button
from engine import Piece
from pygame import mixer

mixer.init()
pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
# play background music
background_music_sounds = pygame.mixer.music.load("music.mp3")
#set preferred volume
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1) # Play multiple times
pygame.display.update()

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

        OPTIONS_BACK = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 525),
                              text_input="BACK", font=get_font(38), base_color="#d7fcd4", hovering_color="White")

        OPTIONS_BACK.changeColor(MODE_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        

        for button in [SURVIVAL_BUTTON, SPRINT_BUTTON]:
            button.changeColor(MODE_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                      
                if SURVIVAL_BUTTON.checkForInput(MODE_MOUSE_POS):
                    play_survival()
                if SPRINT_BUTTON.checkForInput(MODE_MOUSE_POS):
                    play_sprint()
                if OPTIONS_BACK.checkForInput(MODE_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        GRAPHICS_BUTTON = Button(image=None, pos=(300, 200),
                              text_input="GRAPHICS", font=get_font(18), base_color="Black", hovering_color="Green")
        
        GRAPHICS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        GRAPHICS_BUTTON.update(SCREEN)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GRAPHICS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    graphics()

        pygame.display.update()

def graphics():
    while True:
        
        GRAPHICS_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.fill("white")

        THEME_TEXT = get_font(18).render(
            "Select Your Preferred Theme", True, "#010203")
        THEME_RECT = THEME_TEXT.get_rect(center=(300, 50))
        SCREEN.blit(THEME_TEXT, THEME_RECT)

        
        GRAPHICS_DEFAULT = Button(image=None, pos=(300, 100),
                              text_input="DEFAULT THEME", font=get_font(18), base_color="Black", hovering_color="Grey")
        GRAPHICS_DEFAULT.changeColor(GRAPHICS_MOUSE_POS)
        GRAPHICS_DEFAULT.update(SCREEN)
        
        GRAPHICS_AQUATIC = Button(image=None, pos=(300, 200),
                              text_input="AQUATIC THEME", font=get_font(18), base_color="Black", hovering_color="Turquoise")
        GRAPHICS_AQUATIC.changeColor(GRAPHICS_MOUSE_POS)
        GRAPHICS_AQUATIC.update(SCREEN)

        GRAPHICS_FOREST = Button(image=None, pos=(300, 300),
                              text_input="FOREST THEME", font=get_font(18), base_color="Black", hovering_color="#415A45")
        GRAPHICS_FOREST.changeColor(GRAPHICS_MOUSE_POS)
        GRAPHICS_FOREST.update(SCREEN)

        GRAPHICS_INDUSTRIAL = Button(image=None, pos=(300, 400),
                              text_input="INDUSTRIAL THEME", font=get_font(18), base_color="Black", hovering_color="#E84C3D")
        GRAPHICS_INDUSTRIAL.changeColor(GRAPHICS_MOUSE_POS)
        GRAPHICS_INDUSTRIAL.update(SCREEN)

        GRAPHICS_BACK = Button(image=None, pos=(300, 500),
                              text_input="BACK", font=get_font(18), base_color="Black", hovering_color="Green")

        GRAPHICS_BACK.changeColor(GRAPHICS_MOUSE_POS)
        GRAPHICS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GRAPHICS_BACK.checkForInput(GRAPHICS_MOUSE_POS):
                    options()
                if GRAPHICS_DEFAULT.checkForInput(GRAPHICS_MOUSE_POS):
                    Piece.L_SHAPE.update(Piece.L_SHAPE_YELLOW)
                    Piece.R_SHAPE.update(Piece.R_SHAPE_ORANGE)
                    Piece.O_SHAPE.update(Piece.O_SHAPE_CYAN)
                    Piece.T_SHAPE.update(Piece.T_SHAPE_MAGENTA)
                    Piece.S_SHAPE.update(Piece.S_SHAPE_BLUE)
                    Piece.Z_SHAPE.update(Piece.Z_SHAPE_GREEN)
                    Piece.I_SHAPE.update(Piece.I_SHAPE_RED)
                if GRAPHICS_AQUATIC.checkForInput(GRAPHICS_MOUSE_POS):
                    Piece.L_SHAPE.update(Piece.L_SHAPE_TIFFANY_BLUE)
                    Piece.R_SHAPE.update(Piece.R_SHAPE_AQUAMARINE)
                    Piece.O_SHAPE.update(Piece.O_SHAPE_HONOLULU_BLUE)
                    Piece.T_SHAPE.update(Piece.T_SHAPE_JACARTA)
                    Piece.S_SHAPE.update(Piece.S_SHAPE_PEARLY_PURPLE)
                    Piece.Z_SHAPE.update(Piece.Z_SHAPE_LEMON_MERINGUE)
                    Piece.I_SHAPE.update(Piece.I_SHAPE_NAPLES_YELLOW)
                if GRAPHICS_FOREST.checkForInput(GRAPHICS_MOUSE_POS):
                    Piece.L_SHAPE.update(Piece.L_SHAPE_DARK_LAVA)
                    Piece.R_SHAPE.update(Piece.R_SHAPE_COYOTE_BROWN)
                    Piece.O_SHAPE.update(Piece.O_SHAPE_CRAYOLAS_OUTER_SPACE)
                    Piece.T_SHAPE.update(Piece.T_SHAPE_GRAY_ASPARAGUS)
                    Piece.S_SHAPE.update(Piece.S_SHAPE_AXOLOTL)
                    Piece.Z_SHAPE.update(Piece.Z_SHAPE_PHILIPPINE_GRAY)
                    Piece.I_SHAPE.update(Piece.I_SHAPE_ARTICHOKE)
                if GRAPHICS_INDUSTRIAL.checkForInput(GRAPHICS_MOUSE_POS):
                    Piece.L_SHAPE.update(Piece.L_SHAPE_JAPANESE_INDIGO)
                    Piece.R_SHAPE.update(Piece.R_SHAPE_CARMINE_PINK)
                    Piece.O_SHAPE.update(Piece.O_SHAPE_BRIGHT_GRAY)
                    Piece.T_SHAPE.update(Piece.T_SHAPE_TUFTS_BLUE)
                    Piece.S_SHAPE.update(Piece.S_SHAPE_CRAYOLAS_GOLD)
                    Piece.Z_SHAPE.update(Piece.Z_SHAPE_SEA_GREEN)
                    Piece.I_SHAPE.update(Piece.I_SHAPE_ASH_GRAY)
                    

        pygame.display.update()




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Tuffy Tetris", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 250),
                             text_input="PLAY", font=get_font(38), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(300, 400),
                                text_input="OPTIONS", font=get_font(38), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300, 550),
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
