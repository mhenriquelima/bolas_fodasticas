import pygame

class Habilidade:
    def __init__(self, nome: str, cooldown: float, duracao: float, charge : int, efeito: str):
        self.nome = nome
        self.cooldown = cooldown
        self.duracao = duracao
        self.charge = charge
        self.efeito = efeito