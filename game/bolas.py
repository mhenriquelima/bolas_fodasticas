import pygame
import habilidades as habilidades
import times as times

from arena import ARENA_WIDTH, ARENA_HEIGHT

class Bola:
    def __init__(self, x, y, vida: int, dano: int, radius: int, color: pygame.Color, team: times.Team, habilidade: habilidades.Habilidade, speed_cap: float = 500.0):
        if isinstance(x, pygame.Vector2):
            self.pos = x.copy()
        else:
            self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.speed_cap = speed_cap
        self.vida = vida
        self.dano = dano
        self.radius = radius
        self.color = color
        self.team = team
        self.habilidade = habilidade

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def move(self, direction: pygame.Vector2, speed: float, dt: float):
        self.pos += direction * speed * dt

    def check_collision(self, other_bola) -> bool:
        distance = pygame.Vector2(self.pos).distance_to(other_bola.pos)
        return distance < (self.radius + other_bola.radius)

    def use_habilidade(self):
        if self.habilidade:
            print(f"Usando habilidade: {self.habilidade.nome}")
            # logica de habilidade
    
    def take_damage(self, amount: int):
        self.vida -= amount
        if self.vida <= 0:
            print("Bola destruída!")

    def is_alive(self) -> bool:
        return self.vida > 0

class KingOfKnights(Bola):
    def __init__(self, x, y, vida: int, dano: int, radius: int, color: pygame.Color, team: times.Team, habilidade: habilidades.Habilidade, speed_cap: float = 500.0):
        super().__init__(x, y, vida, dano, radius, color, team, habilidade, speed_cap)
        self.special_ability_used = False

    def use_special_ability(self):
        if not self.special_ability_used:
            print("Usando habilidade especial do King of Knights!")
            self.special_ability_used = True
            # lógica da habilidade especial

class KingOfHeroes(Bola):
    def __init__(self, x, y, vida: int, dano: int, radius: int, color: pygame.Color, team: times.Team, habilidade: habilidades.Habilidade, speed_cap: float = 500.0):
        super().__init__(x, y, vida, dano, radius, color, team, habilidade, speed_cap)
        self.special_ability_used = False

    def use_special_ability(self):
        if not self.special_ability_used:
            print("Usando habilidade especial do King of Heroes!")
            self.special_ability_used = True
            # lógica da habilidade especial