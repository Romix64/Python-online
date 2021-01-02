DESTINACE = ('Praha', 'Viden', 'Brno', 'Svitavy', 'Zlin', 'Ostrava',)
CENY = (1000, 1100, 2000, 1500, 2300, 3400,)
SLEVA = ('Svitavy', 'Ostrava',)


# Pozdrav klienta
print('=' * 42)
print('Dobry den, vitejte v programu DESTINATION =')
print('=' * 42)



# Nabídni mu destinace
print(''' ''')
print('V soucasne dobe nabizime cestovani do techto destinaci:')
print('''
1 - Praha	1000
2 - Viden	1100
3 - Brno	2000
4 - Svitavy	1500
5 - Zlin	2300
6 - Ostrava	3400
''')

# Získej vstup uživatele o destinaci
ZVOLENI_DESTINACE = int(input('Zadej prosim cislo destinace: '))

if ZVOLENI_DESTINACE > 6 or ZVOLENI_DESTINACE < 1:
    print('Chyba! V soucasne dobe nabizime pouze vyse uvedene destinace (1 - 6)')
    exit()


index_ceny = CENY[ZVOLENI_DESTINACE -1]
index_destinace = DESTINACE[ZVOLENI_DESTINACE-1]
print('Vybral jste si destinaci: ', index_destinace)
if index_destinace in SLEVA:
    print('Cena destinace je se slevou 25%',)
    input('Stisknete ENTER pro pokracovani ')
    index_ceny = index_ceny * 0.75



print('-' * 42)
print('''
******** REGISTRACE ********
''')

JMENO = input('Zadejte prosim Vase cele jmeno: ')
NAROZENI = input('Zadejte prosim rok narozeni: ')
EMAIL = input('Zadejte prosim Vas e-mail: ')
HESLO = input('Zadejte prosim Vase nove heslo: ')




if 2020 - int(NAROZENI) < 15:
    print('Uzivateli musi byt nejmene 15 let.')
elif '@' not in EMAIL and '.' not in EMAIL:
    print('Zadal jsi neplatny email.')
elif len(HESLO) < 8 or HESLO[0].isnumeric() or HESLO[-1].isnumeric() or HESLO.isnumeric() or HESLO.isalpha():
    print('''
    Chyba !!!
    Heslo musi obsahovat minimalne 8 znaku
    Heslo nesmi obsahovat cislici na zacatku a na konci
    Heslo musi obsahovat cisla a pismena''')
else:
    print(' ')
    print('Registrace dokoncena. Dekujeme.')
    print('-' * 42)
    print(' ')
    print(' ')
    print('Vse probehlo v poradku, potvrzeni bylo zaslano na e-mail: ', EMAIL)
    print('Objednavka c. 205894 byla prijata na jmeno: ', JMENO)
    print('Narozen: ', NAROZENI)
    print(' ')
    print('Vybrana destinace: ', index_destinace)
    print('Celkova cena, vcetne DPH 21% je',index_ceny, 'Kc')
    print(' ')
    print('Dekujeme :)')
    print('*'*42)