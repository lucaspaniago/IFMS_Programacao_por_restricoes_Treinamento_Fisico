import random
from ortools.sat.python import cp_model


def ehNumero(digito):
    try:
         int(digito)
    except ValueError:
         return False
    return True

def calculaTempoDeExecucao(velocidadeDeExecucao):

    return sum([int(x) for x in velocidadeDeExecucao if ehNumero(x)])

'''
    Variáveis que o usuário irá inserir
'''
quantidadeDeExercicios = 10
numeroDeRepeticoesPadrao = 12
velocidadeDeExecucaoPadrao = '2020'
tempoDeExecucaoPadrao = calculaTempoDeExecucao(velocidadeDeExecucaoPadrao) * numeroDeRepeticoesPadrao
restricoes = {
    'objetivo': 'hipertrofia',
    'nivel': 'iniciante'
}

listaDeExercicios = [
    {
        'id': 1,
        'nome': 'CRUCIFIXO DECLINADO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 1,
        'iniciante': 0
    },
    {
        'id': 2,
        'nome': 'CRUCIFIXO RETO COM ELÁSTICO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 1,
        'iniciante': 1
    },
    {
        'id': 3,
        'nome': 'CRUCIFIXO DECLINADO COM ELÁSTICO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 1,
        'iniciante': 0
    },
    {
        'id': 4,
        'nome': 'CRUCIFIXO RETO CROSS OVER EM PÉ',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 5,
        'nome': 'PULLOVER NO BANCO COM HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 1,
        'iniciante': 1
    },
    {
        'id': 6,
        'nome': 'CRUCIFIXO EM PÉ INCLINADO CROSS OVER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 1,
        'iniciante': 0
    },
    {
        'id': 7,
        'nome': 'CRUCIFIXO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 8,
        'nome': 'APOIO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 1
    },
    {
        'id': 9,
        'nome': 'PRESSÃO ARCO MÁGICO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 1
    },
    {
        'id': 10,
        'nome': 'PARTIDA COM O PEITO NO CHÃO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 11,
        'nome': 'SUPINO RETO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 12,
        'nome': 'SUPINO RETO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 1
    },
    {
        'id': 13,
        'nome': 'SUPINO INCLINADO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 14,
        'nome': 'SUPINO FECHADO BARRA',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 1
    },
    {
        'id': 15,
        'nome': 'SUPINO RETO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 1
    },
    {
        'id': 16,
        'nome': 'SUPINO DECLINADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 17,
        'nome': 'SUPINO DECLINADO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 18,
        'nome': 'APOIO FECHADO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 19,
        'nome': 'APOIO COM BOSU INVERTIDO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 20,
        'nome': 'APOIO NO BOSU',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 21,
        'nome': 'APOIO SOLO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 22,
        'nome': 'APOIO DECLINADO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 1,
        'flexibilidade': 0,
        'iniciante': 0
    },
    {
        'id': 23,
        'nome': 'APOIO SOLO JOELHO NO CHÃO',
        'tempo': tempoDeExecucaoPadrao,
        'hipertrofia': 0,
        'flexibilidade': 0,
        'iniciante': 1
    }
]



'''
    ::..Seção 1 - Definição das variáveis do modelo..::
'''

model = cp_model.CpModel()

variaveis = []

for exercicio in listaDeExercicios:
    variaveis.append(model.NewIntVar(0, 1, "{}".format(exercicio['nome'])))

'''
    ::..Seção 2 - Definição das restrições..::
'''

'''
    Como ainda não tem restrições pelas necessidades dos alunos, gero aleatóriamente a lista
    de exercícios selecionados
'''
exerciciosSelecionados = []

if len(restricoes) > 0:
    status = True

    for exercicio in listaDeExercicios:
        status = True
        for restricao in restricoes:
            if not exercicio[restricoes[restricao]]:
                status = False
        
        if status:
            exerciciosSelecionados.append(exercicio)

    while len(exerciciosSelecionados) < quantidadeDeExercicios:
        quantidadeDeExercicios = int(input(f"Existem apenas {len(exerciciosSelecionados)} exercicios que satisfazem as exigências. Diminua a quantidade de exercícios para este músculo.\nDigite a nova quantidade: "))
        
    indices = random.sample(range(len(exerciciosSelecionados)), quantidadeDeExercicios)
    exerciciosSelecionados = [exerciciosSelecionados[i] for i in indices]
else:
    indices = random.sample(range(len(listaDeExercicios)), quantidadeDeExercicios)
    exerciciosSelecionados = [listaDeExercicios[i] for i in indices]
    

# for i in exerciciosSelecionados:
#     print(i)
'''
    Acho que modularizar a contrução, criando uma lista de exercícios para cada músculo
    será mais organizado, eficaz e viável. Por isso tornei a variável abaixo genérica
'''
exercicios = [variaveis[i] for i in range(quantidadeDeExercicios)]
exerciciosTotal = sum(exercicios)

'''
    Como a ideia aqui é selecionar apenas os exercícios de peitoral, o tempo pode ser calculado
    depois, com a lista de exercícios completa.
'''
#tempoTotal = vars[0] * listaDeExercicios[0]['tempo'] + vars[1] * listaDeExercicios[1]['tempo']
tempos = [variaveis[i] * listaDeExercicios[i]['tempo'] for i in range(len(variaveis))]
tempoTotal = sum(tempos)

# Caso, realizar o treino no menor tempo possível, seja uma exigência
model.Minimize(tempoTotal)

model.Add(tempoTotal <= 60*60)
model.Add(exerciciosTotal == quantidadeDeExercicios)


'''
    ::..Seção 3 - Busca e impressão das soluções..::
'''

solver = cp_model.CpSolver()
status = solver.Solve(model)

for i in range(len(variaveis)):
    if solver.Value(variaveis[i]):
        print (exerciciosSelecionados[i]['nome'])
'''

if solver.Value(vars[0]):
    print (listaDeExercicios[0]['nome'])
if solver.Value(vars[1]): 
    print (listaDeExercicios[1]['nome'])
if solver.Value(vars[2]): 
    print (listaDeExercicios[2]['nome'])
'''

