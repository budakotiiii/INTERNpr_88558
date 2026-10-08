import pygame, random

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

snake = [(300, 200)]
food = (100, 100)
dx, dy = 20, 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy == 0: dx, dy = 0, -20
            if e.key == pygame.K_DOWN and dy == 0: dx, dy = 0, 20
            if e.key == pygame.K_LEFT and dx == 0: dx, dy = -20, 0
            if e.key == pygame.K_RIGHT and dx == 0: dx, dy = 20, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)

    if head in snake or not (0 <= head[0] < 600 and 0 <= head[1] < 400):
        break

    snake.insert(0, head)

    if head == food:
        food = (random.randrange(0, 600, 20),
                random.randrange(0, 400, 20))
    else:
        snake.pop()

    screen.fill("black")

    for part in snake:
        pygame.draw.rect(screen, "green", (*part, 20, 20))

    pygame.draw.rect(screen, "red", (*food, 20, 20))

    pygame.display.update()
    clock.tick(10)

pygame.quit()