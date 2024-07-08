import pygame
from level import Level


def main():
    WIDTH = 500
    HEIGHT = 700
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    level = Level()
    
    
    
    game_loop: bool = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
                
        screen.fill('#939393')
        
        level.draw_game(screen)

        
        pygame.display.update()
        clock.tick(15)
            
            
    pygame.quit()


if __name__ == '__main__':
    main()
