wejscie = input('''Program szyfruje adresy stron.
Podaj stronę do zaszyfrowania: ''')
wejscie = wejscie.lower()
n = 'abcdefghijklmnopqrstuvwyzabc'
a = wejscie.split('.')[0]
b = '.'+wejscie.split('.')[1]

x = len(wejscie)
litera3 = n[n.index(wejscie[2])+3]
print(a[0:2]+litera3+str(x)+b)
