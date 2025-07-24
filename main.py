Tarefas = [] 

def adicionarTarefa():
    adicao = input('Descreva sua tarefa:  ')
    Tarefas.append(adicao)

def Listar_tarefas():
   # print(Tarefas)
    for lista, value in enumerate(Tarefas, start=1):
        print(f"{lista} --- Tarefa: {value}")

# proximo passo organização visual da listagem
# Adicionar opção de remover tarefas
# Adicionar status de tarefa
while True: 
    print('1- Adicione uma nova tarefa')
    print()
    print('2- Listar Todas as tarefas')
    print()
    print('3- Encerrar')
    escolha = int(input(' Escolha uma opção acima: '))

    if escolha == 1: 
        print('Adicionando nova tarefa....')
        adicionarTarefa()     
    elif escolha == 2:
        print('Listando Todas as tarefas.....')
        Listar_tarefas()
    elif escolha == 3:
        print('Encerrando o programa.....')
        break
    else:
        print('opção inválida')
