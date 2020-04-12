import random
from ortools.sat.python import cp_model
from exercicios import exercicios

'''
    Variáveis globais - cp_model
'''
model = cp_model.CpModel()
variaveis_ortools = []

random.shuffle(exercicios)
for exercicio in exercicios:
    variaveis_ortools.append(model.NewIntVar(0, 1, "{}".format(exercicio['nome'])))


def lista_de_exercicios_de_nivel(nivel_em_questao):
    
    # Aqui eu queria conferir se o nivel_em_questao é um dos niveis contidos 
    # na lista dos possíveis níveis, que está no exercicios.py, mas não consegui
    #print(exercicios.lista_de_niveis())
    lista = []

    for exercicio in exercicios:
        if nivel_em_questao in exercicio['nivel']:
            lista.append(1)
        else: 
            lista.append(0)
    
    return lista
    
def modela_quantidade_de_exercicios(quantidade):
    # VERIFICAR SE ESTÁ CORRETO USAR A VARIÁVEL total_de_exercicios AQUI, DESSA FORMA, SEM DECLARÁ-LA NESTE ESCOPO
    model.Add(total_de_exercicios == quantidade)

def modela_quantidade_de_exercicios_do_nivel_por(quantidade_ou_porcentagem, valor_estabelecido, nivel_em_questao):
    
    total_de_exercicios_do_nivel_em_questao = sum([variaveis_ortools[i] * lista_de_exercicios_de_nivel(nivel_em_questao)[i] for i in range(len(variaveis_ortools))])

    if (quantidade_ou_porcentagem == 'quantidade'):
        model.Add(total_de_exercicios_do_nivel_em_questao >= valor_estabelecido)
            
    elif(quantidade_ou_porcentagem == 'porcentagem'):    
        model.Add(total_de_exercicios_do_nivel_em_questao >= round(quantidade_de_exercicios * valor_estabelecido / 100))
    else:
        print('Erro 1: A função modela_quantidade_de_exercicios_do_nivel_por só aceita, como primeiro argumento, o texto, todas minúsculas: quantidade ou porcentagem;' )

def modela_distribuicao_padrao_dos_exercicios_de_acordo_com_nivel(nivel_do_aluno):
    modela_quantidade_de_exercicios_do_nivel_por('porcentagem', 100, nivel_do_aluno)

if __name__ == '__main__':
    
    total_de_exercicios = sum(variaveis_ortools)

    tempos = [variaveis_ortools[i] * exercicios[i]['tempo'] for i in range(len(variaveis_ortools))]
    tempoTotal = sum(tempos)

    '''
        Variáveis que serão setadas pelo usuário
    '''
    quantidade_de_exercicios = 3
    nivel_do_aluno = 'iniciante'
    
    '''
        Modelagem - Criação das restrições
    '''
    #model.Minimize(tempoTotal)
    #model.Add(tempoTotal <= 60*60)    
    modela_quantidade_de_exercicios(quantidade_de_exercicios)
    modela_distribuicao_padrao_dos_exercicios_de_acordo_com_nivel(nivel_do_aluno)
    #modela_quantidade_de_exercicios_do_nivel_por('porcentagem', 33, 'iniciante')
    #modela_quantidade_de_exercicios_do_nivel_por('porcentagem', 33, 'intermediario')
    #modela_quantidade_de_exercicios_do_nivel_por('porcentagem', 33, 'avancado')
    modela_distribuicao_padrao_dos_exercicios_de_acordo_com_nivel(nivel_do_aluno)
    
    '''
        Resolução
    '''
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    '''
        Impressão
    '''

    for i in range(len(variaveis_ortools)):
        if solver.Value(variaveis_ortools[i]):
            print (f"{exercicios[i]['nome']} - {exercicios[i]['nivel']}")

