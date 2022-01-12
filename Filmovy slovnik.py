# Vstupní proměnné
oddelovac = "=" * 62
uzivatele = {"tomas", "petr", "marek"}
sluzby = ("dostupne filmy", "detaily filmu", "reziseri")
film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
              "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
              "Jeffrey DeMunn", "Larry Brandenburg"
              )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
              "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
              "John Marley", "Richard Conte"
              )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
              "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
              "Monique Gabriela", "Ron Dean", "Cillian Murphy"
              )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
              "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
              "David Bowie"
              )
}

# Společný slovník 'filmy'
filmy = {'film_4': film_4, 'film_3': film_3, 'film_2': film_2, 'film_1': film_1}
vsechny_filmy = []

# registrace noveho uzivatele
def registrace():
    new_user = input('Zadej nove registracni jmeno: ')
    if new_user in uzivatele:
        print('Tento uzivatel jiz existuje...')
        exit()
    else:
        print('Zapisuji do databaze...')
    return uzivatele.add(new_user)

# Ulozeni vsech dostupnych filmu do promenne vsechny filmy
def filmy_vsechny():
    for i in filmy:
        a = (filmy[i]['JMENO'])
        vsechny_filmy.append(a)

# Vypis detailu filmu
def detail_filmu():
    filmy_tupl = tuple(vsechny_filmy)
    print(oddelovac,'Dostupne filmy:'.upper().center(62),filmy_tupl,oddelovac, sep="\n")
    jaky = input('Jaky film te zajima? Zapisuj presne! ')
    if jaky == filmy_tupl[0]:
        print(filmy['film_4'])
    elif jaky == filmy_tupl[1]:
        print(filmy['film_3'])
    elif jaky == filmy_tupl[2]:
        print(filmy['film_2'])
    elif jaky == filmy_tupl[3]:
        print(filmy['film_1'])
    else:
        print('Chyba! Neplatne zadani!')
        exit()

# Vypis vsech reziseru
def reziseri():
    filmy_tupl = tuple(vsechny_filmy)
    print(oddelovac,'Dostupne filmy:'.upper().center(62),filmy_tupl,oddelovac, sep="\n")
    print('Zde muzes vypsat seznam reziseru. Bud vsech dohromady, nebo k jednotlivym filmum...')
    rozhodnuti = input('Zadej nazev filmu pro vypsani reziseru. Nebo napis slovo \"vsichni\" pro vypsani seznamu vsech reziseru: ' )
    if rozhodnuti == 'vsichni':
        print({filmy['film_1']["REZISER"], filmy['film_2']["REZISER"], filmy['film_3']["REZISER"],
               filmy['film_4']["REZISER"]})
    elif rozhodnuti == filmy_tupl[0]:
        print(filmy['film_4']['REZISER'])



# Přihlášení, uvítání, nabídka (případně ukončení)
print(oddelovac)
print('Aplikace filmovy slovnik'.center(62))
print(oddelovac)
print('Pocet registrovanych clenu:', len(uzivatele))
# Cyklus, ktery ridi prihlaseni, nebo registraci
while True:
    otazka = input('Jsi registrovany? a/n ')
    if otazka == 'n':
        print('Napred se musis registrovat...')
        registrace()
    elif otazka == 'a':
        user = input('Zadej sve prihlasovaci jmeno: ')
        if user not in uzivatele:
            print('Tohle jmeno nemam v databazi... Ukoncuji program.')
            exit()
        else:
            print(user, 'se prihlasil do programu!')
            break
    else:
        print('Chybne zadani, ukoncuji')
        exit()
print('Nyni registrovano clenu:', len(uzivatele))
print(oddelovac, 'VITEJTE V NASEM FILMOVEM SLOVNIKU!'.upper().center(62), oddelovac, sep="\n")
print('1'.center(33), '2'.center(1), '3'.center(22))
print(f"| {' | '.join(sluzby)} |".upper().center(62), oddelovac, sep="\n")
volba = input('Vyber si prosim z nabidky sluzeb podle cisla, nebo vepis text: ')


if volba.upper() in sluzby[0].upper() or volba == str(1):
    filmy_vsechny()
    filmy_tupl = tuple(vsechny_filmy)
    print(oddelovac,'Dostupne filmy:'.upper().center(62),filmy_tupl,oddelovac, sep="\n")
elif volba.upper() in sluzby[1].upper() or volba == str(2):
    filmy_vsechny()
    detail_filmu()
elif volba.upper() in sluzby[2].upper() or volba == str(3):
    filmy_vsechny()
    reziseri()
else:
    print('Chybne zadani! Ukoncuji...')
    exit()