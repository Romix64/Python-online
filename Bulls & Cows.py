import random
import time

cisla = []
pokusy = 0
oddelovac = '-' * 34

def generator_cisla():
    x = list(random.sample(range(0, 10), 4))
    for cislo in x:
        cisla.append(cislo)
    print(cisla)

def uvitani():
    print(oddelovac)
    print('** Vitej ve hre Bulls and Cows! **')
    print(oddelovac)
    print('')
    rozhodnuti = input('Cilem hry je uhodnout nahodne vygenerovane 4 ciferne cislo s tim, ze kazda cifra je jina. Troufnes si? a/n: ')
    if rozhodnuti == 'n':
        print('GAME OVER... srabe! :)')
        exit()
    if rozhodnuti == 'a':
        print('Jdeme na to !!!')
        time.sleep(2)
    else:
        print("Je nutne zadat pouze 'a' - ano nebo 'n' - ne, program se ukoncuje...")
        exit()


def hra():
    global pokusy
    pokusy += 1
    cows = 0
    bulls = 0
    while True:
        volba_hrace = input('Zkus uhodnout 4 ciferne cislo...: ').strip('/*-+.,;`!£$%^&')
        if volba_hrace.isalpha():
            print('Myslis si, ze', volba_hrace, 'je cislice? Je nutne zadavat pouze cislice!')
            continue
        if len(volba_hrace) > 4 or len(volba_hrace) < 4:
            print('Je nutne zadat 4 ciferne cislo!')
            continue
        if len(set(volba_hrace)) < 4:
            print('cisla nesmi byt stejna! ')
        else:
            break
    hracova_volba = []
    for i in range(4):
        hracova_volba.append(int(volba_hrace[i]))
    for i in range(4):
        for j in range(4):
            if hracova_volba[i] == cisla[j] and i != j:
                cows += 1
    for x in range(4):
        if hracova_volba[x] == cisla[x]:
            bulls += 1
    print('Bulls', bulls)
    print('Cows', cows)
    if bulls == 4:
        print('Vyhral jsi! Celkem pokusu:', pokusy)
    if bulls != 4:
        print('Jeste to neni ono, zkousej dal!')
        time.sleep(1)
        hra()


def main():
    generator_cisla()
    uvitani()
    hra()


main()
