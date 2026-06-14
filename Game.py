import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NeuroPlay")

player = pygame.Rect(100, 100, 40, 40)
enemy = pygame.Rect(500, 300, 40, 40)

clock = pygame.time.Clock()

enemy_speed = 2
score = 0

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if enemy.x < player.x:
        enemy.x += enemy_speed
    if enemy.x > player.x:
        enemy.x -= enemy_speed
    if enemy.y < player.y:
        enemy.y += enemy_speed
    if enemy.y > player.y:
        enemy.y -= enemy_speed

    score += 1

    if score % 500 == 0:
        enemy_speed += 0.5

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.flip()

pygame.quit()
