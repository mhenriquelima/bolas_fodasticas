import pygame

class Team:
    def __init__(self, name: str, color: pygame.Color, members: list, attack_buff: float = 1.0, defense_buff: float = 1.0):
        self.name = name
        self.color = color
        self.members = members
        self.attack_buff = attack_buff
        self.defense_buff = defense_buff

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def remove_member_by_index(self, index):
        if 0 <= index < len(self.members):
            del self.members[index]

    def get_member(self, index):
        if 0 <= index < len(self.members):
            return self.members[index]
        return None

    def get_members(self):
        return self.members

    def set_attack_buff(self, buff: float):
        self.attack_buff = buff

    def set_defense_buff(self, buff: float):
        self.defense_buff = buff

    def apply_attack_buff(self, members):
        for member in members:
            member.dano *= self.attack_buff

    def apply_defense_buff(self, members):
        for member in members:
            member.vida *= self.defense_buff