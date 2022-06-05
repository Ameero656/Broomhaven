# from dataclasses import dataclass


# @dataclass
# class Player:
#     name: str



# player = Player(name='bla')
# player.name='The Hero'

# print('------------')
# print(player)


class Player():
    level =1
    health_points = level+5
    base_damage = level+3
    deck = []

    
monsters = {
    'slime' : {
    'health_points' : '10',
    'base_damage' : '2'
}}

player1 = Player()



player_attacks = {
    'Scratch': {
        'lv' : 1,  
        'dmg_multiplier' : 1
    },

    'Dance': {
        'lv' : 2,
        'dmg_multiplier' : 1.5
    }
    
}

def player_turn(player_attacks):
    print('Attacks:')
    for attack_type, attack_details in player_attacks.items():
        print(attack_type, attack_details)
        if attack_details['lv'] <= player1.level:
            deck.append(attack_type)
        
        # if x['lv'] <= player1.level:
        #     print(x)
player_turn(player_attacks)   
def battle(monster):
    battleinfo()
    player_turn()
    monster_turn()
    battleinfo()
