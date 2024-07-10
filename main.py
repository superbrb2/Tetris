import pygame
import select_screen
from level import Level



def main():
    WIDTH = 500
    HEIGHT = 700
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    level = Level()
    menu = select_screen.Menu()

    in_menu = True
    
    game_loop: bool = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if in_menu:
                    menu_choice = menu.detect_selection_mouse(pygame.mouse.get_pos())
                    if menu_choice != -1:
                        in_menu = False
        screen.fill('#939393')
        if in_menu:
            menu.display(screen)
        else:   
            level.draw_game(screen)

        
        pygame.display.update()
        clock.tick(15)
            
            
    pygame.quit()


if __name__ == '__main__':
    main()
