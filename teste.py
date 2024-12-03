# a = 10
# b = 5

# soma = a + b
# subtracao = a - b
# multiplicar = a * b
# dividir = a / b

# print(f"a soma dos numeros são: {soma}")
# print(f"a subtração dos numeros são: {subtracao}")
# print(f"a multiplicação dos numeros são: {multiplicar}")
# print(f"a divisão dos numeros são: {dividir}")



# nome = input("Insira seu nome: ")
# idade = input("insira sua idade: ")

# print(f" olá meu nome é {nome} é eu tenho {idade} anos e um prazer te conhecer")


#par

verificar = float(input("insira o valor para verificar se e impa ou par: "))

if verificar%2 == 0:
    print(f"{verificar} é par")
    
else:
    print(f"{verificar} é impar")
    


for i in range(2, 21):
    if i %3 !=0 :
        print(i)
    