import pygame
from times import Team
from bolas import KingOfKnights, KingOfHeroes
from arena import Arena
from utils import speed_cap

BOLA_RADIUS = 50

pygame.init()
screen = pygame.display.set_mode((1280, 720))

Time1 = Team("Time 1", pygame.Color("blue"), [])
Time2 = Team("Time 2", pygame.Color("red"), [])

arena = Arena(600, 600, screen)

saber = KingOfKnights(arena.x + 120, arena.y + 120, 100, 10, BOLA_RADIUS, pygame.Color("blue"), Time1, None)
gilgamesh = KingOfHeroes(arena.x + 420, arena.y + 240, 100, 15, BOLA_RADIUS, pygame.Color("red"), Time2, None)

saber.vel = pygame.Vector2(180, 110)
gilgamesh.vel = pygame.Vector2(-150, 210)

Time1.add_member(saber)
Time2.add_member(gilgamesh)
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000

    for bola in (saber, gilgamesh):
        bola.pos += bola.vel * dt

        min_x = arena.x + bola.radius
        max_x = arena.x + arena.width - bola.radius
        min_y = arena.y + bola.radius
        max_y = arena.y + arena.height - bola.radius

        if bola.pos.x < min_x:
            bola.pos.x = min_x
            bola.vel.x *= -1
        elif bola.pos.x > max_x:
            bola.pos.x = max_x
            bola.vel.x *= -1

        if bola.pos.y < min_y:
            bola.pos.y = min_y
            bola.vel.y *= -1
        elif bola.pos.y > max_y:
            bola.pos.y = max_y
            bola.vel.y *= -1

    dx = gilgamesh.pos.x - saber.pos.x
    dy = gilgamesh.pos.y - saber.pos.y
    distance_sq = dx * dx + dy * dy
    min_dist = saber.radius + gilgamesh.radius

    if distance_sq > 0 and distance_sq < min_dist * min_dist:
        distance = distance_sq ** 0.5
        normal = pygame.Vector2(dx, dy) / distance
        overlap = min_dist - distance

        saber.pos -= normal * (overlap / 2)
        gilgamesh.pos += normal * (overlap / 2)

        relative_velocity = gilgamesh.vel - saber.vel
        velocity_along_normal = relative_velocity.dot(normal)

        if velocity_along_normal < 0:
            impulse = -velocity_along_normal * 1.1
            saber.vel -= normal * impulse
            gilgamesh.vel += normal * impulse

    speed_cap(saber, 1000.0)
    speed_cap(gilgamesh, 1000.0)

    screen.fill((0, 0, 0))
    arena.draw()
    saber.draw(screen)
    gilgamesh.draw(screen)

    pygame.display.flip()

pygame.quit()