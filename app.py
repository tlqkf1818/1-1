pip install pygame
import pygame
import random

# 초기 설정
pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# 뱀 초기 위치
snake = [(100, 100)]
dx, dy = BLOCK, 0

# 음식 위치
food = (
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
)

score = 0
running = True

while running:
    clock.tick(10)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -BLOCK
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, BLOCK
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -BLOCK, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = BLOCK, 0

    # 머리 이동
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    new_head = (head_x, head_y)

    # 벽 충돌
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        running = False

    snake.insert(0, new_head)

    # 음식 먹기
    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        )
    else:
        snake.pop()

    # 화면 그리기
    screen.fill(BLACK)

    # 음식
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

    # 뱀
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, BLOCK, BLOCK))

    # 점수
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
