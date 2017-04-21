

# Coral snakes are venomous, and can be recognized by red stripes touching yellow stripes
# Scarlet King snakes are harmless, and can be recognized by red stripes touching black stripes
def is_venomous(snake):
    return 'Snakes???'

animals = ['cat','bird','snake','dog','horse','goose','Jon Bon Jovi']
# I am 99% sure this very wrong.
def is_animal(animals):
    if 'snake' in animals:
        return 'Snake'
    elif animals.index >= 0:
        return 'Not Snake'
    else:
        return 'Not Animal'

def snake_name(i_haz_sign):
    if i_haz_sign == 'I am a Coral Snake':
        return 'venomous'
    elif i_haz_sign == 'I am a Scarlet King':
        return 'harmless'
    else:
        return 'DUNNO!!'
    
def pretty_snake(color1, color2):
    if color1 + '-' + color2 == 'red-yellow':
        return 'venomous'
    elif color1 + '-' + color2 == 'red-black':
        return 'harmless'
    else:
        return 'STILL DUNNO!!'
    
def is_it_snek(animals, i_haz_sign, color1, color2):
    return (is_animal(animals)+','+snake_name(i_haz_sign)+','+pretty_snake(color1, color2))

#this does not work like I want it to yet....
results_list=[is_it_snek('snake','I am a Coral Snake','red','black')]
print results_list
    
