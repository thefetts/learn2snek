

# Coral snakes are venomous, and can be recognized by red stripes touching yellow stripes
# Scarlet King snakes are harmless, and can be recognized by red stripes touching black stripes


# def is_venomous(colors):
#     red_index = colors.index('red') if 'red' in colors else -1
#     if red_index > -1:
#         if (red_index < len(colors)-1 and colors[red_index + 1] == 'yellow') or (red_index > 0 and colors[red_index - 1] == 'yellow'):
#             return 'You\'re a dead fellow!'
#         elif (red_index < len(colors)-1 and colors[red_index + 1] == 'black') or (red_index > 0 and colors[red_index - 1] == 'black'):
#             return 'You\'re ok Jack!'
#
#     return 'BAD SNEK!'

def is_venomous(colors):
    red_index = colors.index('red') if 'red' in colors else -1
    if red_index > -1:
        if before_or_after_red('yellow', red_index, colors):
            return 'You\'re a dead fellow!'
        elif before_or_after_red('black', red_index, colors):
            return 'You\'re ok Jack!'

    return 'BAD SNEK!'


def before_or_after_red(color, red_index, colors):
    return (red_index < len(colors)-1 and colors[red_index + 1] == color) or \
           (red_index > 0 and colors[red_index - 1] == color)






class Snake:
    def __init__(self, colors):
        self.colors = colors
        self.red_index = colors.index('red') if 'red' in colors else -1

    def is_venomous(self):
        if self.red_index > -1:
            if self.before_or_after_red('yellow'):
                return 'You\'re a dead fellow!'
            elif self.before_or_after_red('black'):
                return 'You\'re ok Jack!'

        return 'BAD SNEK!'


    def before_or_after_red(self, color):
        return (self.red_index < len(self.colors)-1 and self.colors[self.red_index + 1] == color) or \
               (self.red_index > 0 and self.colors[self.red_index - 1] == color)







































animals = ['cat','bird','snake','dog','horse','goose','Jon Bon Jovi']
# I am 99% sure this very wrong.
def is_animal(animal):
    if animal == 'snake':
        return 'Snake'
    elif animal in animals:
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
    
def is_it_snek(animal, i_haz_sign, color1, color2):
    return [is_animal(animal), snake_name(i_haz_sign), pretty_snake(color1, color2)]

#this does not work like I want it to yet....
results_list=is_it_snek('poo','I am a Coral Snake','red','black')
print(results_list)

    
