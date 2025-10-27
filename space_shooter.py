# space_shooter.py
import pygame, random, sys
pygame.init()

W, H = 480, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
player = pygame.Rect(W//2-25, H-60, 50, 50)
bullets = []
enemies = [pygame.Rect(random.randint(0, W-40), 0, 40, 40) for _ in range(5)]

def draw():
    screen.fill((30,30,30))
    pygame.draw.rect(screen, (0,255,0), player)
    for b in bullets: pygame.draw.rect(screen, (255,255,0), b)
    for e in enemies: pygame.draw.rect(screen, (255,0,0), e)
    pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x>0: player.x -= 5
    if keys[pygame.K_RIGHT] and player.x<W-50: player.x += 5
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player.centerx-5, player.y, 10, 20))
    for b in bullets[:]:
        b.y -= 8
        if b.y < 0: bullets.remove(b)
    for e in enemies[:]:
        e.y += 3
        if e.y > H: enemies.remove(e); enemies.append(pygame.Rect(random.randint(0,W-40),0,40,40))
        for b in bullets[:]:
            if e.colliderect(b):
                enemies.remove(e)
                enemies.append(pygame.Rect(random.randint(0,W-40),0,40,40))
                bullets.remove(b)
    draw()
    clock.tick(60)
