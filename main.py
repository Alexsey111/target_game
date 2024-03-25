import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра тир')
icon = pygame.image.load('img/tir.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed_x = 1
target_speed_y = 1

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

font = pygame.font.Font('freesansbold.ttf', 16)
score = 0
missed = 0

running = True
while running:
    screen.fill(color)

    score_text = font.render(f'Подания: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    missed_text = font.render(f'Промахи: {missed}', True, (255, 255, 255))
    screen.blit(missed_text, (SCREEN_WIDTH - 120, 10))

    speed_text = font.render('Изменение скорости:', True, (255, 255, 255))
    screen.blit(speed_text, (10, 50))

    speed_up_text = font.render('Вверх - увеличить', True, (255, 255, 255))
    screen.blit(speed_up_text, (10, 90))

    speed_down_text = font.render('Вниз - уменьшить', True, (255, 255, 255))
    screen.blit(speed_down_text, (10, 130))

    target_x += target_speed_x
    target_y += target_speed_y

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                missed += 1

        # Увеличение и уменьшение скорости с клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                target_speed_x *= 1.1
                target_speed_y *= 1.1
            elif event.key == pygame.K_DOWN:
                target_speed_x *= 0.9
                target_speed_y *= 0.9

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
