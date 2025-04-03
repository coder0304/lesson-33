import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2

BLUE=pygame.color('yellow')
LIGHTBLUE=pygame.color('darkblue')
DARKBLUE=pygame.color('darkblue')

YELLOW=pygame.color('yellow')
MAGENTA=pygame.color('magenta')
ORANGE=pygame.color('orange')
WHITE=pygame.color('white')

class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<=0 or
        self.rect.right>=500:
        self.velocity[0]=-self.velocity[0]
        boundary_hit=True
        if self.rect.top<=0 or
        self.rect.bottom>=400:
        self.velocity

     
     

