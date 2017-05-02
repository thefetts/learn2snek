import copy

class Pokemon:
    def __init__(self, name, health, power, speed):
        self.name = name
        self.health = health
        self.power = power
        self.speed = speed


data = {
    'roster': [
        Pokemon('Oddish', 0, 100, 50),
        Pokemon('Pikachu', 100, 50, 70),
        Pokemon('Butterfree', 60, 40, 40),
        Pokemon('Charizard', 110, 70, 80),
        Pokemon('Mew', 500, 100, 90),
        Pokemon('Mewtwo', 500, 100, 80)
    ]
}


def attack(offense, defense):
    combat_log = []
    attacker = find_by_name(offense)
    defender = find_by_name(defense)

    pika_power = attacker.power
    ouchies = defender.health - pika_power
    defender.health = ouchies
    combat_log.append(offense + ' hits ' + defense + ' for ' + str(pika_power) + '!')
    if ouchies > 0:
        combat_log.append(defense + ' has ' + str(ouchies) + ' HP remaining.')
    else:
        combat_log.append(defense + ' has fainted!')
    return combat_log


def find_by_name(name):
    return list(filter(lambda pokemon: pokemon.name == name, data['roster']))[0]


def battle(offense, defense):
    roster_copy = copy.deepcopy(data['roster'])
    attacker = find_by_name(offense)
    defender = find_by_name(defense)

    if defender.health <= 0:
        return [defense + ' has fainted!']
    elif attacker.health <= 0:
        return [offense + ' has fainted!']
    else:
        results = []
        while attacker.health > 0:
            results += attack(offense, defense)
            if defender.health > 0:
                results += attack(defense, offense)
            else:
                break
        data['roster'] = roster_copy
        return results
