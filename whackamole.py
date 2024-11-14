import pygame
import random

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")

        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (32, 32))

        mole_x = 0
        mole_y = 0

        def draw_grid():
            for x in range (0,641,32):
                pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, 512))
            for y in range(0, 513, 32):  # Include 512 for last line
                pygame.draw.line(screen, (100, 100, 100), (0, y), (640, y))

        def is_click_in_mole_square(click_pos):
            click_x, click_y = click_pos
            return (mole_x <= click_x < mole_x + 32) and (mole_y <= click_y < mole_y + 32)

        def move_mole_to_random_square():
            nonlocal mole_x, mole_y
            mole_x = random.randrange(0, 20) * 32
            mole_y = random.randrange(0, 16) * 32

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if is_click_in_mole_square(event.pos):
                        move_mole_to_random_square()

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
