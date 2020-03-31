from ortools.sat.python import cp_model

exercicios = [
    {
        'id': 1,
        'tipo': 1,
        'nome': 'Supino Reto',
        'tempo': 30,
        'ombro': 1,
        'cotovelo': 1
    },
    {
        'id': 2,
        'tipo': 1,
        'nome': 'Voador',
        'tempo': 4,
        'ombro': 1
    },
    {
        'id': 3,
        'tipo': 1,
        'nome': 'Apoio',
        'tempo': 4,
        'ombro': 1,
        'cotovelo': 1
    },
    {
        'id': 4,
        'tipo': 1,
        'nome': 'Crucifixo Reto Com Halteres',
        'tempo': 20,
        'ombro': 1,
        'cotovelo': 1
    },
    {
        'id': 5,
        'tipo': 1,
        'nome': 'Supino Vertical',
        'tempo': 40,
        'ombro': 1,
        'cotovelo': 1
    }
]




'''
    Seção 1 - Definição das variáveis do modelo
'''

model = cp_model.CpModel()

vars = []

for ex in exercicios:
    vars.append(model.NewIntVar(0, 1, "{}".format(ex['nome'])))

'''
    Seção 2 - Definição das restrições
'''

peitoral = [vars[i] for i in range(5)]
peitoralTotal = sum(peitoral)


#tempoTotal = vars[0] * exercicios[0]['tempo'] + vars[1] * exercicios[1]['tempo']
tempos = [vars[i] * exercicios[i]['tempo'] for i in range(len(vars))]
tempoTotal = sum(tempos)

model.Minimize(tempoTotal)
model.Add(tempoTotal <= 60)
model.Add(peitoralTotal >= 3)


'''
    Seção 3 - Busca e impressão das soluções
'''

solver = cp_model.CpSolver()
status = solver.Solve(model)

for i in range(len(vars)):
    if solver.Value(vars[i]):
        print (exercicios[i]['nome'])
'''

if solver.Value(vars[0]):
    print (exercicios[0]['nome'])
if solver.Value(vars[1]): 
    print (exercicios[1]['nome'])
if solver.Value(vars[2]): 
    print (exercicios[2]['nome'])
'''

