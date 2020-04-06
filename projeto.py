import random
from ortools.sat.python import cp_model
from exercicios import exercicios

quantidadeDeExercicios = 4

restricoes = {
    'objetivo': 'hipertrofia',
    'nivel': 'iniciante'
}

def obter_selecao_de_exercicios(restricoes, exercicios):
    '''
        Como ainda não tem restrições pelas necessidades dos alunos, gero aleatóriamente a lista
        de exercícios selecionados
    '''
    global quantidadeDeExercicios

    if restricoes: # equivalente a len(restricoes) > 0
        exerciciosSelecionados = filtra_exercicios(exercicios)

        while len(exerciciosSelecionados) < quantidadeDeExercicios:
            quantidadeDeExercicios = int(input(f"Existem apenas {len(exerciciosSelecionados)} exercicios que satisfazem as exigências. Diminua a quantidade de exercícios para este músculo.\nDigite a nova quantidade: "))
            
        return seleciona_amostra(exerciciosSelecionados, quantidadeDeExercicios)
    else:
        return seleciona_amostra(exercicios, quantidadeDeExercicios)

def filtra_exercicios(exercicios):
    selecao = []

    for exercicio in exercicios:
        nivel_adequado = exercicio['nivel'] == restricoes['nivel']
        objetivo_adequado = restricoes['objetivo'] in exercicio['objetivos']

        if nivel_adequado and objetivo_adequado:
            selecao.append(exercicio)
    
    return selecao

def seleciona_amostra(exercicios, quantidade):
    return [exercicios[i] for i in random.sample(range(len(exercicios)), quantidade)]

if __name__ == '__main__':
    model = cp_model.CpModel()
    variaveis = []
    exerciciosSelecionados = obter_selecao_de_exercicios(restricoes, exercicios)

    for exercicio in exerciciosSelecionados:
        variaveis.append(model.NewIntVar(0, 1, "{}".format(exercicio['nome'])))

    exercicios = [variaveis[i] for i in range(quantidadeDeExercicios)]
    exerciciosTotal = sum(exercicios)

    tempos = [variaveis[i] * exerciciosSelecionados[i]['tempo'] for i in range(len(variaveis))]
    tempoTotal = sum(tempos)

    model.Minimize(tempoTotal)

    model.Add(tempoTotal <= 60*60)
    model.Add(exerciciosTotal == quantidadeDeExercicios)


    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    for i in range(len(variaveis)):
        if solver.Value(variaveis[i]):
            print (exerciciosSelecionados[i]['nome'])

