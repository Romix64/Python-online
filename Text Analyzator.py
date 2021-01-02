print(30 * '*')
print(30 * '*')
print('* Vitejte v Text Analyzatoru *')
print(30 * '*')

users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
TEXT1 = ('''

Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''')

TEXT2 = ('''

At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''')

TEXT3 = ('''

The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''')

otazka = input('Jsi registrovany? a/n ')
if otazka == 'n':
    print('Zaregistruj se prosim: ')
    novejmeno = input('Zadej sve jmeno: ')
    noveheslo = input('Zadej sve heslo: ')
    users[novejmeno] = noveheslo
    print('Registrace probehla v poradku, muzes se prihlasit...')

elif otazka == 'a':
    print('Prihlas se, prosim...')
else:
    print('Chybne zadani, ukoncuji...')
    exit()

jmeno = input('Jmeno: ')
heslo = input('Heslo: ')

if heslo == users.get(jmeno):
    print('Pristup povolen.')
    print(30 * '*')
else:
    print('Neplatne heslo.')
    exit()
system = input('Mame zde 3 texty urcene k analyze. Chces je vypsat? Pokud stisknes "n", program se ukonci. a/n ')
print(60 * '-')
if system == 'a':
    print('')
    print('Text 1: ', TEXT1)
    print(60 * '-')
    print('')
    print('Text 2: ', TEXT2)
    print(60 * '-')
    print('')
    print('Text 3: ', TEXT3)
    print(60 * '-')
    print(' ')
else:
    print('Ukoncuji Analyzator...')
    exit()

mod = True
while mod:
    system2 = input('''Vyber si prosim jeden z textu, ktery chces analyzovat (1 - 3). 
Vyber 4 ti umozni analyzovat vlastni text. Pokud chces program ukoncit, napis "konec": ''')

    if system2 == '4':
        TEXT4 = input('Zde zadej vlastni text urceny k analyze: ')
        system2 = TEXT4
    elif system2 == '1':
        system2 = TEXT1
    elif system2 == '2':
        system2 = TEXT2
    elif system2 == '3':
        system2 = TEXT3
    elif system2 == 'konec':
        print('Ukoncuji Analyzator...')
        exit()
    elif '1, 2, 3, 4, konec' not in system2:
        print('')
        print('Chybne zadani, opakujte akci...')
        print('')
        continue

    muj_text1 = []
    pocet_mala = 0
    pocet_velka = 0
    pocet_velka2 = 0
    pocet_cisel = 0
    cetnosti = {}
    soucet = 0
    for slovo in system2.split():
        delka = len(slovo.strip(',.?!/*-;@'))
        if delka in cetnosti.keys():
            cetnosti[delka] = cetnosti[delka]+1
        else:
            cetnosti[delka] = 1
        muj_text1.append(slovo.strip(',.?!/*-;@'))
        if slovo.islower():
            pocet_mala = pocet_mala + 1
        elif slovo.istitle():
            pocet_velka = pocet_velka + 1
        elif slovo.isupper():
            pocet_velka2 = pocet_velka2 + 1
        elif slovo.isnumeric():
            pocet_cisel = pocet_cisel + 1
            soucet += int(slovo)

    print(60 * '-')
    # print(muj_text1)
    print('Celkovy pocet slov je:', len(muj_text1))
    print('Celkovy pocet slov psanych malymi pismeny:', pocet_mala)
    print('Celkovy pocet slov psanych velkymi pismeny:', pocet_velka2)
    print('Celkovy pocet slov zacinajicich velkym pismenem je:', pocet_velka)
    print('Pocet cisel v textu:', pocet_cisel)
    print(60 * '-')
    for i in cetnosti.keys():
        print(str(i) + ": " + "*" * cetnosti[i], int(cetnosti[i]))
    print('Soucet vsech cisel v textu je:', soucet)
    print(60 * '-')