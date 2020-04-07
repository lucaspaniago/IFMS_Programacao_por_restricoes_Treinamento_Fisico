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
numeroDeRepeticoesPadrao = 12
velocidadeDeExecucaoPadrao = '2020'
tempoDeExecucaoPadrao = calculaTempoDeExecucao(velocidadeDeExecucaoPadrao) * numeroDeRepeticoesPadrao

exercicios = [
    {
        'id': 1,
        'nome': 'CRUCIFIXO DECLINADO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'flexibilidade'],
        'nivel': ['iniciante']
    },
    {
        'id': 2,
        'nome': 'CRUCIFIXO RETO COM ELÁSTICO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['flexibilidade'],
        'nivel': ['iniciante']
    },
    {
        'id': 3,
        'nome': 'CRUCIFIXO DECLINADO COM ELÁSTICO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['flexibilidade'],
        'nivel': ['avançado']
    },
    {
        'id': 4,
        'nome': 'CRUCIFIXO RETO CROSS OVER EM PÉ',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 5,
        'nome': 'PULLOVER NO BANCO COM HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'flexibilidade'],
        'nivel': ['iniciante']
    },
    {
        'id': 6,
        'nome': 'CRUCIFIXO EM PÉ INCLINADO CROSS OVER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'flexibilidade'],
        'nivel': ['avançado']
    },
    {
        'id': 7,
        'nome': 'CRUCIFIXO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['avançado']
    },
    {
        'id': 8,
        'nome': 'APOIO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['iniciante']
    },
    {
        'id': 9,
        'nome': 'PRESSÃO ARCO MÁGICO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['iniciante']
    },
    {
        'id': 10,
        'nome': 'PARTIDA COM O PEITO NO CHÃO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['avançado']
    },
    {
        'id': 11,
        'nome': 'SUPINO RETO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 12,
        'nome': 'SUPINO RETO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['iniciante']
    },
    {
        'id': 13,
        'nome': 'SUPINO INCLINADO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 14,
        'nome': 'SUPINO FECHADO BARRA',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['iniciante']
    },
    {
        'id': 15,
        'nome': 'SUPINO RETO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['iniciante']
    },
    {
        'id': 16,
        'nome': 'SUPINO DECLINADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 17,
        'nome': 'SUPINO DECLINADO FECHADO ALTERNADO HALTER',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 18,
        'nome': 'APOIO FECHADO FITA DE SUSPENSÃO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['avançado']
    },
    {
        'id': 19,
        'nome': 'APOIO COM BOSU INVERTIDO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['avançado']
    },
    {
        'id': 20,
        'nome': 'APOIO NO BOSU',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['avançado']
    },
    {
        'id': 21,
        'nome': 'APOIO SOLO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 22,
        'nome': 'APOIO DECLINADO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado']
    },
    {
        'id': 23,
        'nome': 'APOIO SOLO JOELHO NO CHÃO',
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['iniciante']
    }
]
