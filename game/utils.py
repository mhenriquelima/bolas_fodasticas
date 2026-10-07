import math
import random

from bolas import Bola

def speed_cap(bola: Bola, max_speed: float | None = None):
    limit = bola.speed_cap if max_speed is None else max_speed
    if bola.vel.length() > limit:
        bola.vel.scale_to_length(limit)

def check_collision(bola1: Bola, bola2: Bola) -> bool:
    distance = math.hypot(bola2.pos.x - bola1.pos.x, bola2.pos.y - bola1.pos.y)
    return distance < (bola1.radius + bola2.radius)

def check_collision_with_arena(bola: Bola, arena_width: int, arena_height: int) -> bool:
    if (bola.pos.x - bola.radius < 0 or
        bola.pos.x + bola.radius > arena_width or
        bola.pos.y - bola.radius < 0 or
        bola.pos.y + bola.radius > arena_height):
        return True
    return False