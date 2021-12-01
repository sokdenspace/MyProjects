# pip install pygame
# ------------------

# Import python packages
import pygame, os

# Set screen size & Title
WIDHT, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Space Fight!")

# Set frame per second, Velocity & Sprite rotate, scale
FPS = 60
VEL = 5
SPACE_WIDTH, SPACE_HEIGHT = 96, 96

# Import the images
BACKGROUND = pygame.image.load("Assets/bg.png")
WASD_KEYS = pygame.image.load("Assets/wasd_keys.png")
SPACE_IMAGE = pygame.image.load(os.path.join('Assets', 'space.png'))
SPACE_IMAGE_PRODUCT = pygame.transform.rotate(pygame.transform.scale(
    SPACE_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 0)

# Update screen every second
def draw_window(space):
    WINDOW.blit(BACKGROUND, [0, 0])
    WINDOW.blit(SPACE_IMAGE_PRODUCT, (space.x, space.y))
    WINDOW.blit(WASD_KEYS, [20, 450])
    pygame.display.update()

# Create keyboard to control input from player
def keyborad(space):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        space.x -= VEL
    if keys_pressed[pygame.K_d]:
        space.x += VEL
    if keys_pressed[pygame.K_w]:
        space.y -= VEL
    if keys_pressed[pygame.K_s]:
        space.y += VEL

# Main function & Set false window running when press close(x) button
def main():
    space = pygame.Rect(360, 300, SPACE_WIDTH, SPACE_HEIGHT)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Call the functions
        keyborad(space)
        draw_window(space)

if __name__ == "__main__":
    main()
