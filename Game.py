import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NeuroPlay - Adaptive Enemy Difficulty")

font = pygame.font.SysFont(None, 36)

player = pygame.Rect(100, 100, 40, 40)
enemy = pygame.Rect(500, 300, 40, 40)

clock = pygame.time.Clock()

score = 0
enemy_speed = 2

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

if score < 500:
    enemy_speed = 2
elif score < 1000:
    enemy_speed = 3
elif score < 1500:
    enemy_speed = 4
else:
    enemy_speed = 5

if player.colliderect(enemy):
    screen.fill((255, 255, 255))

    game_over = font.render(
        f"Game Over! Score: {score}",
        True,
        (255, 0, 0)
    )

    screen.blit(game_over, (250, 300))
    pygame.display.flip()
    pygame.time.wait(3000)

    running = False

screen.fill((255, 255, 255))

pygame.draw.rect(screen, (0, 0, 255), player)
pygame.draw.rect(screen, (255, 0, 0), enemy)

score_text = font.render(
    f"Score: {score} | Enemy Speed: {enemy_speed}",
    True,
    (0, 0, 0)
)

screen.blit(score_text, (10, 10))

pygame.display.flip()

pygame.quit()        player.y += 5

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
