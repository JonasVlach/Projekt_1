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
USERS = {'bob' : '123',
         'ann' : 'pass123',
         'mike': 'password123',
         'liz' : 'pass123'}

# Nastavení oddělovače
ODDELOVAC = 40 * '-'


# Úvod programu
print(ODDELOVAC)
print('Welcome to the app. Please log in:')
username = input('USERNAME: ')
password = input('PASSWORD: ')

# Ověření jména a hesla
if USERS.get(username) == password:
    print('Login was successful.')
else:
    print('Incorrect name or password.')
    exit()

# Vyběr textu a ověření volby
print(ODDELOVAC)
print('We have 3 texts to be analyzed.')
text_choice = input('Enter a number 1-3 to select: ')

if text_choice.isnumeric() and int(text_choice) in range(1, 4):
    text_choice = int(text_choice) - 1
else:
    print('Your choice is not possible. Choose a number 1-3.')
    exit()

# Proměnné pro výpočty
title_case = 0
upper_case = 0
lower_case = 0
digits = list()
frequencies = dict()

for word in TEXTS[text_choice].split():
    word = word.strip(",.")
    if len(word) not in frequencies:
        frequencies[len(word)] = 1
    else:
        frequencies[len(word)] += 1

    if word.istitle():
        title_case = title_case + 1
    elif word.isupper():
        upper_case = upper_case + 1
    elif word.islower():
        lower_case = lower_case + 1
    elif word.isdigit():
        digits.append(int(word))

# Výpis výsledků
print(ODDELOVAC)
print(                                                                         # staci jeden `print` na vsechny vystupy
    f"There are {title_case} titlecase words",
    f"There are {lower_case} lowercase words",
    f"There are {upper_case} uppercase words",
    f"There are {len(digits)} numeric words",                                  # pomoci seznamu urcime delku
    f"If we summed all the numbers in this text we would get: {sum(digits)}",  # pomoci seznamu pocitame sumu
    sep="\n"                                                                   # mezi kazdy vypisem novy radek
)

# Výpis grafu
print(ODDELOVAC)
for klic, hodnota in sorted(frequencies.items()):        # prochazim jak klice, tak hodnoty pro vzestupne setrizeny slovnik
    print(f"{klic:>2} {hodnota * '*':<17} {hodnota}")  # vypisuji (+ zarovnavam na ruzne delky)
