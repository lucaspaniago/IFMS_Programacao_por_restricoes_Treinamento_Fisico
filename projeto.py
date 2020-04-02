import random
from ortools.sat.python import cp_model


def isnumber(digito):
    try:
         int(digito)
    except ValueError:
         return False
    return True

def calculaTempoDeExecucao(velocidadeDaExecucao):

    return sum([int(x) for x in velocidadeDaExecucao if isnumber(x)])

'''
    Variáveis que o usuário irá inserir
'''
quantidadeDeExercicios = 3
numeroDeRepeticoesPadrao = 12
velocidadeDeExecucaoPadrao = '2020'
tempoDeExecucaoPadrao = calculaTempoDeExecucao(velocidadeDeExecucaoPadrao) * numeroDeRepeticoesPadrao


listaDeExercicios = [
    {
        'id': 1,
        'nome': 'CRUCIFIXO DECLINADO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 2,
        'nome': 'CRUCIFIXO RETO COM ELÁSTICO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 3,
        'nome': 'CRUCIFIXO DECLINADO COM ELÁSTICO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 4,
        'nome': 'CRUCIFIXO RETO CROSS OVER EM PÉ',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 5,
        'nome': 'PULLOVER NO BANCO COM HALTER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 6,
        'nome': 'CRUCIFIXO EM PÉ INCLINADO CROSS OVER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 7,
        'nome': 'CRUCIFIXO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 8,
        'nome': 'APOIO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 9,
        'nome': 'PRESSÃO ARCO MÁGICO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 10,
        'nome': 'PARTIDA COM O PEITO NO CHÃO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 11,
        'nome': 'SUPINO RETO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 12,
        'nome': 'SUPINO RETO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 13,
        'nome': 'SUPINO INCLINADO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 14,
        'nome': 'SUPINO FECHADO BARRA',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 15,
        'nome': 'SUPINO RETO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 16,
        'nome': 'SUPINO DECLINADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 17,
        'nome': 'SUPINO DECLINADO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 18,
        'nome': 'APOIO FECHADO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 19,
        'nome': 'APOIO COM BOSU INVERTIDO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 20,
        'nome': 'APOIO NO BOSU',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 21,
        'nome': 'APOIO SOLO',
        'tempo': tempoDeExecucaoPadrao,
    },
    {
        'id': 22,
        'nome': 'APOIO DECLINADO',
        'tempo': tempoDeExecucaoPadrao,
    },
]




'''
    ::..Seção 1 - Definição das variáveis do modelo..::
'''

model = cp_model.CpModel()

vars = []

for ex in listaDeExercicios:
    vars.append(model.NewIntVar(0, 1, "{}".format(ex['nome'])))

'''
    ::..Seção 2 - Definição das restrições..::
'''

'''
    Como ainda não tem restrições pelas necessidades dos alunos, gero aleatóriamente a lista
    de exercícios selecionados
'''
indices = random.sample(range(len(listaDeExercicios)), quantidadeDeExercicios)
exerciciosSelcionados = [listaDeExercicios[i] for i in indices]

'''
    Acho que modularizar a contrução, criando uma lista de exercícios para cada músculo
    será mais organizado, eficaz e viável. Por isso tornei a variável abaixo genérica
'''
exercicios = [vars[i] for i in range(quantidadeDeExercicios)]
exerciciosTotal = sum(exercicios)

'''
    Como a ideia aqui é selecionar apenas os exercícios de peitoral, o tempo pode ser calculado
    depois, com a lista de exercícios completa.
'''
#tempoTotal = vars[0] * listaDeExercicios[0]['tempo'] + vars[1] * listaDeExercicios[1]['tempo']
tempos = [vars[i] * listaDeExercicios[i]['tempo'] for i in range(len(vars))]
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

for i in range(len(vars)):
    if solver.Value(vars[i]):
        print (exerciciosSelcionados[i]['nome'])
'''

if solver.Value(vars[0]):
    print (listaDeExercicios[0]['nome'])
if solver.Value(vars[1]): 
    print (listaDeExercicios[1]['nome'])
if solver.Value(vars[2]): 
    print (listaDeExercicios[2]['nome'])
'''

