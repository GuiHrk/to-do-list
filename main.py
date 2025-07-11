Tarefas = [] 

def adicionarTarefa():
    adicao = input('Descreva sua tarefa:  ')
    Tarefas.append(adicao)

print('1- Adicione uma nova tarefa')
print('2- Listar Todas as tarefas')
print('3- Encerrar')
escolha = int(input(' Escolha uma opção acima: '))


if escolha == 1: 
    print('Adicionando nova tarefa....')
    adicionarTarefa()