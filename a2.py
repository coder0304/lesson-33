import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
RECT_COLOR = (255, 0, 0)

font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to Pygame!", True, (0, 0, 0))

rect_width = 150
rect_height = 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, RECT_COLOR, rectangle)
    screen.blit(text, (160, 50))
    pygame.display.flip()

pygame.quit()
