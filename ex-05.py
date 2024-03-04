x =int(input("Digite o salario do funcionario: "))

if x < 500:
    print("Salario do funcionario reajustado para R$", x * 1.15)
elif x >= 500 and x < 1000:
    print("Salario do funcionario reajustado para R$", x * 1.1)
else:
    print("Salario do funcionario reajustado para R$", x * 1.05)
