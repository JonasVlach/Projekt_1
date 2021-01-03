# Texty ke zpracování
'''
author = Jonáš Vlach
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Registrovaní uživatelé
users = {'bob' : '123',
         'ann' : 'pass123',
         'mike': 'password123',
         'liz' : 'pass123'}

# Nadefinování dělící čáry
def line():
    print(40 * '-')

# Úvod programu
line()
print('Welcome to the app. Please log in:')
username = input('USERNAME: ')
password = input('PASSWORD: ')

# Ověření jména a hesla
if username in users and password == users[username]:
    print('Login was successful.')
else:
    print('Incorrect name or password.')
    exit()

# Vyběr textu a ověření volby
line()
print('We have 3 texts to be analyzed.')
text_choice = input('Enter a number 1-3 to select: ')

if text_choice.isnumeric():
    text_choice = int(text_choice) - 1
else:
    print('Your choice is not possible. Choose a number 1-3.')
    exit()

if text_choice < 0 or text_choice > 2:
    print('Your choice is not possible. Choose a number 1-3.')
    exit()

# Rozdělení a očištění textu
analysis = TEXTS[text_choice].split()
analysis_clean = [slovo.strip(",.") for slovo in analysis]

# Proměnné pro výpočty
count_words = 0
count_title = 0
count_upper = 0
count_lower = 0
count_numbers = 0
count_sum = 0
longest_word = 0
count_graph = {}

# Počet slov
count_len = len(analysis_clean)

# Zjišťování pomocí smyčky
for slovo in analysis_clean:
    if slovo.istitle():
        count_title += 1
    elif slovo.isupper():
        count_upper += 1
    elif slovo.islower():
        count_lower += 1
    elif slovo.isdigit():
        count_numbers += 1
        count_sum += int(slovo)

    count_graph[len(slovo)] = count_graph.get(len(slovo), 0) + 1

# Výpis výsledků
line()
print('There are', count_len, 'words.')
print('There are', count_title, 'titlecase words.')
print('There are', count_upper, 'uppercase words.')
print('There are', count_lower, 'lowercase words.')
print('There are', count_numbers, 'numeric strings.')

# Výpis grafu
line()
for key in sorted(count_graph):
    if key < 10:
        print('', key, count_graph[key] * '*', count_graph[key])
    else:
        print(key, count_graph[key] * '*', count_graph[key])

# Výpis součtu čísel
line()
print('If we summed all the numbers in this text we would get:', count_sum)
