import pygame
from font_wrap import wrap_text

class Level():
    def __init__(self) -> None:
        self.block_grid = [
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','*','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','*','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','*','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','*','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-','-','-'],
            ['*','-','-','-','-','-','-','-','-','-']
        ]
    
        self.block_queue: list = []
        
        # STATS
        self.score: int = 1000000
        self.turn_number: int = 0

        
    def draw_game(self,screen):
        self.draw_game_grid(screen)     
        self.draw_next_block(screen)
        self.draw_score(screen)
        self.draw_queue(screen)
        
        
    def draw_next_block(self,screen):
        font = pygame.font.SysFont('Ariel',38)
        pygame.draw.rect(screen, '#B2B2B2', pygame.Rect(395,20,90,120))
        pygame.draw.rect(screen, '#FFFFFF', pygame.Rect(405,50,70,80))
        screen.blit(font.render('NEXT',True,(0,0,0)),(405,22))
    
    def draw_score(self,screen):
        font = pygame.font.SysFont('Ariel',38)
        number_font = pygame.font.SysFont('Ariel',25)
        pygame.draw.rect(screen, '#B2B2B2', pygame.Rect(395,140,90,65))
        pygame.draw.rect(screen, '#FFFFFF', pygame.Rect(405,170,70,25))
        screen.blit(font.render('SCORE',True,(0,0,0)),(395,145))
        screen.blit(number_font.render(f'{self.score}',True,(0,0,0)),(wrap_text(f'{self.score}',25,70,405),175))
    
    def draw_game_grid(self,screen):
        pygame.draw.rect(screen, '#B2B2B2', pygame.Rect(25,20,350,660))
        grid_colours = ['#D2D2D2','#BFBFBF']
        for i in range(10):
            for j in range(20):
                colour = grid_colours[((i + j) % 2)]
                pygame.draw.rect(screen, colour, pygame.Rect((i*32)+40,(j*32)+30,32,32))
    
    def draw_queue(self,screen):
        pygame.draw.rect(screen, '#B2B2B2', pygame.Rect(395,240,90,440))
        for i in range(5):
            pygame.draw.rect(screen, '#FFFFFF', pygame.Rect(405,(i*85)+250,70,70))
    
    def display_blocks(self,screen):
        for i in range(len(self.block_grid)):
            for j in range(len(self.block_grid[0])):
                if self.block_grid[i][j] == '*':
                    pass
                
        