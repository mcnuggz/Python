from random import randint

ninja_words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

#replace random word in ninja_words with word from ipsum file 
def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f"{word} {ninja_words[random_pos]}"

#ask how many paragraphs does the user want
paragraphs = int(input("How many paragraphs you would like? "))

#open the file
with open("ipsum.txt") as ipsum_original:
    #split string into a list of individual words
    items = ipsum_original.read().split()

    #cycle how many paragraphs
    for n in range(paragraphs):
        #map the original list of words in items list to ninja words list
         ninja_text = list(map(ninjarize, items))
         #amend desired text length to other file
         with open("ninja_ipsum.txt", 'a') as ipsum_ninja:
             ipsum_ninja.write(' '.join(ninja_text) + '\n\n')
