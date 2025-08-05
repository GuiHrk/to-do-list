Tarefas = [] 

Conclusão = {
  " ✅ "
  " ❌ "
  " 🟡 "
}


def adicionarTarefa():
    adicao = input('Descreva sua tarefa:  ')
    Tarefas.append(adicao)

def Listar_tarefas():
    if not Tarefas:
        print('Lista de tarefas vazia!')
    else: 
       for lista, value in enumerate(Tarefas, start=1):
        print(f"{lista} --- Tarefa: {value}")

def Excluir_tarefa():
    lista = int(input('Escolha a tarefa para excluir: ')) -1
    del Tarefas[lista]

def Editar_Tarefa():
    if not Tarefas:
        print('Lista de tarefas vazia!')
    else: 
       for lista, value in enumerate(Tarefas, start=1):
        print(f"{lista} --- Tarefa: {value}")    
    lista = int(input('Escolha a tarefa para editar: '))
    
    
    if lista == 1:
          print(f"{lista}  ✅  {value}")
    elif lista == 2:
          print(f"{lista}  🟡  {value}")
    elif lista ==3:
          print(f"{lista}  ❌  {value}")


while True: 
    print('1- Adicione uma nova tarefa')
    print()
    print('2- Listar Todas as tarefas')
    print()
    print('3- Excluir Tarefa')
    print()
    print('4- Editar Tarefa')
    print()
    print('5- Encerrar')
    escolha = int(input(' Escolha uma opção acima: '))

    if escolha == 1: 
        print('Adicionando nova tarefa....')
        adicionarTarefa()
        print('Tarefa Adicionada com Sucesso!!!')     
    elif escolha == 2:
        print('Listando Todas as tarefas.....')
        Listar_tarefas()
    elif escolha == 3:
        print('Excluindo Tarefa selecionada')
        Excluir_tarefa()
    elif escolha == 4:
        print('Editando Tarefa...')
        Editar_Tarefa()
    elif escolha == 5:
        print('Encerrando o programa.....')
        break
    else:
        print('opção inválida')
