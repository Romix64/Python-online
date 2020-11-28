
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

print('*' * 65)
print('Vitejte v programu pro prevod jednotek               ************')
print('*' * 65)

kilogram = int(input('Zadej vahu v kg, ja ji prevedu na libry? '))

print('Vysledek prevodu kg na lb je: ' , kilogram * kg_lb , 'liber')
print('-' * 65)

kilometr = int(input('Zadej pocet km a ja to prevedu na mile: '))

print('Vysledek prevodu km na mile je: ' , kilometr * km_mile , 'mil')
print('-' * 65)
litr = int(input('Zadej pocet litru, ktere mam prevest na galony: '))

print('Vysledek prevodu litru na galony: ' , litr * l_gal , 'galonu')
print('-' * 65)
pokracovani = input('stiskni libovolne pismeno a pak stiski ENTER pro pokracovani: ')
print('=' * 70)
print('=' * 70)
print('=' * 70)
print('=' * 70)

print('Zadani ukolu:' ,
    '80 kg na lb, '
    '54 km na míle, '
    '5 l na galony, ')

print('80 kg je: ', kg_lb * 80 , 'liber')
print('54 km je: ' , km_mile * 54 , 'mil')
print('5 litru je: ' , l_gal * 5 , 'galonu')



