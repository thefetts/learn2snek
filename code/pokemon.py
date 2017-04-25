import copy

data = {
    'pokedex': {
        'Pikachu': {
            'health': 100,
            'power': 50
        },

        'Butterfree': {
            'health': 60,
            'power': 40
        },

        'Charizard': {
            'health': 110,
            'power': 70
        },

        'Mew': {
            'health': 500,
            'power': 100
        },

        'Mewtwo': {
            'health': 500,
            'power': 100
        },

        'Oddish': {
            'health': 0,
            'power': 100
        }
    }
}


def attack(offense, defense):
    combat_log = []
    pika_power = data['pokedex'][offense]['power']
    ouchies = data['pokedex'][defense]['health'] - pika_power
    data['pokedex'][defense]['health'] = ouchies
    combat_log.append(offense + ' hits ' + defense + ' for ' + str(pika_power) + '!')
    if ouchies > 0:
        combat_log.append(defense + ' has ' + str(ouchies) + ' HP remaining.')
    else:
        combat_log.append(defense + ' has fainted!')
    return combat_log


def battle(offense, defense):
    pokedex_copy = copy.deepcopy(data['pokedex'])
    if data['pokedex'][defense]['health'] <= 0:
        return [defense + ' has fainted!']
    elif data['pokedex'][offense]['health'] <= 0:
        return [offense + ' has fainted!']
    else:
        results = []
        while data['pokedex'][offense]['health'] > 0:
            results += attack(offense, defense)
            if data['pokedex'][defense]['health'] > 0:
                results += attack(defense, offense)
            else:
                break
        data['pokedex'] = pokedex_copy
        return results
