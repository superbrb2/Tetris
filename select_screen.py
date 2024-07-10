import pygame
from font_wrap import wrap_text

class Menu():
    
    def __init__(self) -> None:
        self.box_width: int = 450
        self.box_height: int = 100
        self.box_gap: int = 25
        self.font_size = 50
        
    def display(self,screen):
        self.display_logo(screen)
        self.display_menu_options(screen)
        
    def display_menu_options(self,screen):
        menu_options = ['Normal','Faster','Oh god no']
        number_font = pygame.font.SysFont('Ariel',self.font_size)
        for i in range(3):
            pygame.draw.rect(screen, '#B2B2B2', pygame.Rect(25,(i*(self.box_gap+self.box_height))+325,self.box_width,self.box_height))
            screen.blit(number_font.render(menu_options[i],True,(0,0,0)),(wrap_text(menu_options[i],self.font_size,self.box_width,25),i*(self.box_gap+self.box_height)+325+(self.box_height-self.font_size)/1.7))
            
    def display_logo(self,screen):
        logo_img = pygame.transform.scale(pygame.image.load("logo.png"), (400,400 * 0.694))
        screen.blit(logo_img,pygame.Rect(50,25,0,0))
     
    def detect_selection_mouse(self,mouse_pos):
        x , y = mouse_pos
        if x >= 25 and x <= 475:
            for i in range(3):
                if y >= (i*(self.box_gap+self.box_height))+325 and y <= (i*(self.box_gap+self.box_height))+325+self.box_height:
                    return i
        return -1
        
        