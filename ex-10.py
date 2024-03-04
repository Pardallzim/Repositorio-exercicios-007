x = int(input("Digite um número maximo pra sequencia de fibonacci: "))
f = 0.1
f2 = 2
cont = 0

while cont < x:
    if f == 0.1:
        print(f)
        f = 1
    else:
        print(f)
        n = f + f2
        f = f2
        f2 = n
        cont += 1