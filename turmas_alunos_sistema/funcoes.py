from random import randint
import tabulate

def turmas(lista_turmas):
    id = randint(1, 10000)
    for i in lista_turmas:
        if i["ID"] == id:
            return
    nome = input("Digite o nome da turma: ")
    turma = {
        "Turma": nome,
        "ID": id,
        "Alunos": []
    }
    lista_turmas.append(turma)
    
def alunos(lista_turmas, lista_alunos):
    id_aluno = randint(1, 10000)
    nome = input("Digite o nome do aluno: ")
    turma_perte = int(input("Digite a turma a qual o aluno pertence (ID): ")).lower().stipt()
    aluno = {
        "ID": id_aluno,
        "Nome": nome,
        "Turma": turma_perte
    }
    lista_alunos.append(aluno)
    for i in lista_turmas:
        if i["Turma"] == turma_perte:
            i['Alunos'].append(aluno)
    
def listar_turmas(lista_turmas):
    tabela = [[i["Turma"], i["ID"]] for i in lista_turmas]
    print(tabulate(tabela, headers=["Turma", "ID"], tablefmt="fancy_grid"))
    
def listar_alunos(lista_alunos):
    tabela = [[i["Turma"], i["ID"], i["Nome"]] for i in lista_alunos]
    print(tabulate(tabela, headers=["Turma", "ID", "Nome"], tablefmt="fancy_grid"))
    
def buscar_turma_por_id(lista_turmas):
    id_buscar = int(input("Digite o ID da truma que deseja buscar: "))
    for i in lista_turmas:
        if i["ID"] == id_buscar:
            tabela = [[i["Turma"], i["ID"], i["Alunos"]]]
            print(tabulate(tabela, headers=["Turma", "ID", "Alunos"], tablefmt="fancy_grid"))
            break
        else:
            print("Turma não encontrada, tente novamente")
            
def burcar_aluno_por_id(lista_alunos):
    aluno_buscar = int(input("Digite o ID do aluno que quer buscar: "))
    for i in lista_alunos:
        if i["ID"] == aluno_buscar:
            print(i)

def listar_alunos_da_turma(lista_alunos):
    id_turma = int(input("Digite o ID da turma que quer exibir os alunos: "))
    lista = []
    for i in lista_alunos:
        if i["Turma"] == id_turma:
            lista.append(i)
    return print(lista)

def remover_aluno(lista_turmas):
    id_remover = int(input("Digite o ID do aluno que deseja remover: "))
    for turma in lista_turmas:
        for aluno in turma["Alunos"]:
            if aluno["ID"] == id_remover:
                turma["Alunos"].remove(aluno)
                print("Aluno removido com sucesso!")
                return