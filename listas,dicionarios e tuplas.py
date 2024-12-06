'''dic = { }
while True:
    pergunta = input("digite 1 para inserir novos usuarios\ndigite 2 para fazer a busca das idades dos usuarios: ")
      
      
    if pergunta == "1":
        a= input("insira seu nome: ")
        b= int(input("Insira sua idade: "))

        dic[a] = b

        print(dic)

    elif pergunta == "2":
        nome = input("insira o nome do usuario que deseja saber a idade:")
        busca_idade = dic.get(nome)
        
        for i in dic:
            if i == nome:
                print(f"{i}: {busca_idade} anos")
                
        else:
                print("nenhum usuario com esse nome encontrado")'''
                
lista_num = [1,1,1,2,2,2,2,3,3,3,4,4,4,4,5,6]
unico = []



    
    
