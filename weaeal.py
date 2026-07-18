#My Weasel Program
import random
import string
target_phrase = "METHINKS IT IS LIKE A WEASEL"

letters = string.ascii_uppercase + ' '

def generateword(length):
    return ''.join(random.choice(letters) for _ in range(length))

primordal = generate_word(28)

def create_offspring(ancestor):
    newlist = list(ancestor)
    


#while ancestor != target_phrase:
    
print(primordal)
