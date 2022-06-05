from dataclasses import dataclass


@dataclass
class Player:
    name: str



player = Player(name='bla')
player.name='The Hero'

print('------------')
print(player)
