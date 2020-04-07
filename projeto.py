import random
from ortools.sat.python import cp_model
from exercicios import exercicios

quantidadeDeExercicios = 2

restricoes = {
    'objetivo': 'hipertrofia',
    'nivel': 'iniciante'
}

def obter_selecao_de_exercicios(restricoes, exercicios):
    copia_exercicios = exercicios[:]
    random.shuffle(copia_exercicios)
    return filtra_exercicios(copia_exercicios) if restricoes else copia_exercicios

def filtra_exercicios(exercicios):
    selecao = []

    for exercicio in exercicios:
        #nivel_adequado =  restricoes['nivel'] in exercicio['nivel']
        objetivo_adequado = restricoes['objetivo'] in exercicio['objetivos']
        
        '''Retirei o "nivel_adequado and" do if abaixo'''
        if objetivo_adequado:
            selecao.append(exercicio)
    
    return selecao

if __name__ == '__main__':
    model = cp_model.CpModel()
    variaveis = []
    exerciciosSelecionados = obter_selecao_de_exercicios(restricoes, exercicios)

    '''
    for ex in enumerate(exerciciosSelecionados):
        print(ex, end="\n")
    '''
    for exercicio in exerciciosSelecionados:
        variaveis.append(model.NewIntVar(0, 1, "{}".format(exercicio['nome'])))
    '''
    A partir daqui, sabemos que len(variaveis) == len(exerciciosSelecionados)
    '''
    exercicios = [variaveis[i] for i in range(len(variaveis))]
    exerciciosTotal = sum(exercicios)

    tempos = [variaveis[i] * exerciciosSelecionados[i]['tempo'] for i in range(len(variaveis))]
    tempoTotal = sum(tempos)

    nivel = [variaveis[i] for i in range(len(variaveis)) if restricoes['nivel'] in exerciciosSelecionados[i]['nivel']]
    nivelTotal = sum(nivel)

    model.Minimize(tempoTotal)

    model.Add(tempoTotal <= 60*60)
    model.Add(exerciciosTotal == quantidadeDeExercicios)
    model.Add(nivelTotal == quantidadeDeExercicios)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    for i in range(len(variaveis)):
        if solver.Value(variaveis[i]):
            print (exerciciosSelecionados[i]['nome'])

