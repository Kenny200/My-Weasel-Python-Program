#My Weasel Program
import random
import string

target_phrase = "METHINKS IT IS LIKE A WEASEL"
letters = string.ascii_uppercase + ' '
num_offspring = 100
probability = 3

def generate_word():
    return ''.join(random.choice(letters) for _ in range(28))

adam = generate_word()

def generate_char():
    return random.choice(string.ascii_uppercase + ' ')

def mutate(string):
    charlist = []
    for char in string:
        if random.randint(1,probability) == 1:
            charlist.append(char)
        else:
            charlist.append(generate_char())
    return ''.join(charlist)

def create_offspring(parent):
    offspring_list = []
    for i in range(num_offspring):
        offspring_list.append(mutate(parent))
    return offspring_list

def fitness(child):
    child_char = list(child)
    target_char = list(target_phrase)
    fitness_score = 0
    for c, t in zip(child_char, target_char):
        if c == t:
            fitness_score += 1
    return fitness_score

def score_offspring(offspring):
    best_score = 0
    best_child = offspring[0]
    
    for child in offspring:
        score = fitness(child)
    
        if score > best_score:
            best_score = score
            best_child = string
    return best_child

sons_of_adam = create_offspring(adam)
final_child = score_offspring(sons_of_adam)

print(final_child)
