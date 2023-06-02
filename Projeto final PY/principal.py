from viagem import PacoteViagem
import os

viagem= PacoteViagem()


while True:
    escolha=input('''
                  
================================================
                  
1 - Cadastrar um novo pacote de viagem
2 - Listar viagem cadastrados
3 - Deletar viagem
4 - Editar viagem
5 - Sair

================================================    
Escolha uma opção: ''')

    if escolha == '1':
        #INSERIR VALORES:
        os.system('cls')
        codigo= int(input("Digite o id do produto: "))
        nome= (input("Digite o o destino da viagem: "))
        preco= float(input("Digite o preço da viagem: "))
        quantidade= int(input("Digite a descricao da viagem: "))
        viagem.cadastrar(id, destino, preco, descricao)

        
    elif escolha == "2":
        #CONSULTAR VALORES
        os.system('cls')
        viagem.consultar()
        
    elif escolha == "3":
        #DELETAR VALORES
        os.system('cls')
        id= int(input("Digite o id da viagem a ser excluido: "))
        viagem.deletar(id)
    
    elif escolha == "5":
        print("\nViagen concluida com sucesso!\n")
        break 
            
    elif escolha == "4":
        os.system('cls')
        escolha2= input('''
======================================   
                     
1- Editar nome do produto.
2- Editar preço do produto.
3- Editar estoque do produto.

======================================
Escolha uma opção: ''')
    
    
        
        if escolha2 == "1":    
            #ATUALIZAR NOME:
            os.system('cls')
            nome= input("Digite o id para ser atualiado: ")
            codigo=int(input("Digite o destino da viagem pra ser atualizada: "))
            viagem.id_pacote(id, destino)

        if escolha2 == "2":
            # #ATUALIZAR PREÇO:
            os.system('cls')
            preco= float(input("Digite o preço para ser atualizado: "))
            codigo=int(input("Digite o destino da viagem para ser atuaizado: "))
            viagem.preco(preco, destino)

        if escolha2 == "3":
            #ATUALIZAR QUANTIDADE
            os.system('cls')
            quantidade= input("Digite a quantidade a ser atualiada: ")
            codigo=int(input("Digite o código do produto a ser atualizado: "))
            viagem.descricao(descricao, destino)

    else:
        os.system('cls')
        print("Digite uma opção válida!") 