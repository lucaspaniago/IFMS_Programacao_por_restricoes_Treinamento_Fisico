'''
    Listas de itens possíveis
'''
def lista_de_niveis():
    return ['iniciante', 'intermediario', 'avancado']

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
        'articulacao': ['ombro'],
        'musculo': ['peitoral'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'flexibilidade'],
        'nivel': ['intermediario', 'avancado'],
        'caracteristicas': ['porcao_inferior', 'deitado', 'bilateral', 'monoarticular', 'empunhadura_neutra'],
        'equipamentos': ['halter', 'banco_declinado']
    },
    {
        'id': 2,
        'nome': 'CRUCIFIXO RETO COM ELÁSTICO',
        'articulacao': ['ombro'],
        'musculo': ['peitoral', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['mobilidade', 'flexibilidade'],
        'nivel': ['iniciante', 'intermediario'],
        'caracteristicas': ['compromete_deltoide_anterior', 'em_pe', 'monoarticular', 'bilateral', 'resistencia_variada', 'aquecimento', 'aquecimento_ombro','reabilitacao_ombro', 'empunhadura_neutra'],
        'equipamentos': ['elastico']
    },
    {
        'id': 3,
        'nome': 'CRUCIFIXO DECLINADO COM ELÁSTICO',
        'articulacao': ['ombro'],
        'musculo': ['peitoral'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['flexibilidade', 'mobilidade'],
        'nivel': ['iniciante', 'intermediario'],
        'caracteristicas': ['porcao_inferior', 'monoarticular', 'bilateral', 'deitado', 'resistencia_variada', 'aquecimento_ombro', 'reabilitacao_ombro', 'aquecimento', 'empunhadura_neutra'],
        'equipamentos': ['elastico', 'banco_declinado']
    },
    {
        'id': 4,
        'nome': 'CRUCIFIXO RETO CROSS OVER EM PÉ',
        'articulacao': ['ombro'],
        'musculo': ['peitoral', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avançado', 'intermediario'],
        'caracteristicas': ['em_pe', 'monoarticular', 'bilateral', 'compromete_deltoide_anterior', 'perigoso_para_ombro', 'empunhadura_neutra'],
        'equipamentos': ['cross_over', 'cabo', 'polia']
        
    },
    {
        'id': 5,
        'nome': 'PULLOVER NO BANCO COM HALTER',
        'articulacao': ['ombro'],
        'musculo': ['peitoral', 'grande_dorsal', 'triceps'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'flexibilidade', 'mobilidade'],
        'nivel': ['iniciante', 'avancado', 'intermediario'],
        'caracteristicas': ['reduz_ativacao_cabeca_medial_e_lateral_triceps', 'compromete_deltoide_anterior', 'deitado', 'monoarticular', 'bilateral', 'compromete_grande_dorsal', 'compromete_triceps', 'compromete_peitoral', 'empunhadura_pronada'],
        'equipamentos': ['halter', 'banco_reto']
    },
    {
        'id': 6,
        'nome': 'CRUCIFIXO EM PÉ INCLINADO CROSS OVER',
        'articulacao': ['ombro'],
        'musculo': ['peitoral', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['avancado', 'intermediario'],
        'caracteristicas': ['em_pe', 'monoarticular', 'compromete_deltoide_anterior', 'perigoso_para_ombro', 'bilateral', 'empunhadura_neutra'],
        'equipamentos': ['cross_over', 'cabo', 'polia']
    },
    {
        'id': 7,
        'nome': 'CRUCIFIXO FITA DE SUSPENSÃO',
        'articulacao': ['ombro'],
        'musculo': ['peitoral', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['mobilidade', 'flexibilidade', 'hipertrofia'],
        'nivel': ['avancado', 'intermediario'],
        'caracteristicas': ['em_pe', 'monoarticular', 'pouca_amplitude', 'bilateral', 'compromete_deltoide_anterior', 'empunhadura_neutra'],
        'equipamentos': ['fita_de_suspensao']
        
    },
    {
        'id': 8,
        'nome': 'APOIO FITA DE SUSPENSÃO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['iniciante', 'avancado', 'intermediario'],
        'caracteristicas': ['compromete_deltoide_anterior', 'em_pe', 'biarticular', 'bilateral', 'empunhadura_pronada', 'reduz_ativacao_cabeca_longa_triceps', 'compromete_triceps', 'compromete_peitoral'],
        'equipamentos': ['fita_de_suspensao']
    },
    {
        'id': 9,
        'nome': 'PRESSÃO ARCO MÁGICO',
        'articulacao': ['ombro'],
        'musculo': ['peitoral'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': [],
        'nivel': ['iniciante', 'intermediario'],
        'caracteristicas': ['isometria', 'pouca_amplitude', 'compromete_deltoide_anterior', 'aquecimento', 'aquecimento_ombro', 'monoarticular', 'bilateral', 'empunhadura_neutra'],
        'equipamentos': ['arco_magico']
    },
    {
        'id': 10,
        'nome': 'PARTIDA COM O PEITO NO CHÃO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['avançado', 'intermediario'],
        'caracteristicas': ['deitado', 'biarticular', 'reduz_ativacao_cabeca_longa_triceps', 'compromete_deltoide_anterior', 'bilateral', 'empunhadura_pronada', 'compromete_peitoral', 'compromete_triceps'],
        'equipamentos': []
    },
    {
        'id': 11,
        'nome': 'SUPINO RETO ALTERNADO HALTER',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['avançado', 'intermediario', 'iniciante'],
        'caracteristicas': ['compromete_deltoide_anterior', 'reduz_ativacao_cabeca_longa_triceps', 'deitado', 'biarticular', 'compromete_triceps', 'compromete_peitoral', 'alternado', 'empunhadura_pronada'],
        'equipamentos': ['halter', 'banco_reto']
    },
    {
        'id': 12,
        'nome': 'SUPINO RETO FECHADO ALTERNADO HALTER',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['iniciante', 'avancado', 'intermediario'],
        'caracteristicas': ['reduz_ativacao_cabeca_longa_triceps', 'compromete_deltoide_anterior', 'compromete_triceps', 'biarticular', 'bilateral', 'deitado', 'compromete_peitoral', 'reabilitacao_ombro', 'empunhadura_neutra'],
        'equipamentos': ['halter', 'banco_reto']
    },
    {
        'id': 13,
        'nome': 'SUPINO INCLINADO FECHADO ALTERNADO HALTER',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['avançado', 'intermediario', 'iniciante'],
        'caracteristicas': ['biarticular', 'compromete_triceps', 'compromete_deltoide_anterior', 'compromete_peitoral', 'bilateral', 'deitado', 'compromete_peitoral', 'reabilitacao_ombro', 'empunhadura_neutra', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': ['halter', 'banco_inclinado']
    },
    {
        'id': 14,
        'nome': 'SUPINO FECHADO BARRA',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['iniciante', 'avancado', 'intermediario'],
        'caracteristicas': ['deitado', 'compromete_deltoide_anterior', 'empunhadura_pronada', 'biarticular', 'bilateral', 'reduz_ativacao_cabeca_longa_triceps', 'reabilitacao_ombro', 'compromete_peitoral'],
        'equipamentos': ['barra', 'banco_reto']
    },
    {
        'id': 15,
        'nome': 'SUPINO RETO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['iniciante', 'avancado', 'intermediario'],
        'caracteristicas': ['empunhadura_pronada', 'biarticular', 'bilateral', 'compromete_deltoide_anterior', 'compromete_peitoral', 'compromete_triceps', 'reduz_ativacao_cabeca_longa_triceps', 'deitado', 'importante'],
        'equipamentos': ['barra', 'banco_reto']
    },
    {
        'id': 16,
        'nome': 'SUPINO DECLINADO ALTERNADO HALTER',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['avançado', 'intermediario'],
        'caracteristicas': ['alternado', 'bilateral', 'biarticular', 'empunhadura_pronada', 'compromete_triceps', 'compromete_peitoral', 'deitado', 'porcao_inferior', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': ['halter', 'banco_declinado']
    },
    {
        'id': 17,
        'nome': 'SUPINO DECLINADO FECHADO ALTERNADO HALTER',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['avançado', 'intermediario'],
        'caracteristicas': ['bilateral', 'biarticular', 'empunhadura_neutra', 'compromete_peitoral', 'compromete_deltoide_anterior', 'compromete_triceps', 'deitado', 'reabilitacao_ombro', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': ['halter', 'banco_declinado']
    },
    {
        'id': 18,
        'nome': 'APOIO FECHADO FITA DE SUSPENSÃO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['iniciante', 'intermediario'],
        'caracteristicas': ['bilateral', 'biarticular', 'empunhadura_neutra', 'compromete_triceps', 'compromete_peitoral', 'compromete_deltoide_anterior', 'em_pe', 'reduz_ativacao_cabeca_longa_triceps', 'reabilitacao_ombro'],
        'equipamentos': ['fita_de_suspensao']
    },
    {
        'id': 19,
        'nome': 'APOIO COM BOSU INVERTIDO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['sensorio_motor', 'mobilidade'],
        'nivel': ['intermediario', 'avançado'],
        'caracteristicas': ['base_instavel', 'bilateral', 'biarticular', 'deitado', 'ativacao_core', 'empunhadura_pronada', 'aquecimento_ombro', 'aquecimento', 'compromete_deltoide_anterior', 'compromete_peitoral', 'compromete_triceps', 'reabilitacao_ombro', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': ['bosu']
    },
    {
        'id': 20,
        'nome': 'APOIO NO BOSU',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['sensorio_motor', 'mobilidade'],
        'nivel': ['intermediario', 'avançado'],
        'caracteristicas': ['base_instavel', 'bilateral', 'biarticular', 'deitado', 'ativacao_core', 'empunhadura_pronada', 'aquecimento_ombro', 'aquecimento', 'compromete_deltoide_anterior', 'compromete_peitoral', 'compromete_triceps', 'reabilitacao_ombro', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': ['bosu']
    },
    {
        'id': 21,
        'nome': 'APOIO SOLO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['iniciante', 'intermediario', 'avançado'],
        'caracteristicas': ['bilateral', 'biarticular', 'deitado', 'ativacao_core', 'empunhadura_pronada', 'aquecimento_ombro', 'aquecimento', 'compromete_deltoide_anterior', 'compromete_peitoral', 'compromete_triceps', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': []
    },
    {
        'id': 22,
        'nome': 'APOIO DECLINADO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia'],
        'nivel': ['intermediario', 'avançado'],
        'caracteristicas': ['bilateral', 'biarticular', 'deitado', 'ativacao_core', 'empunhadura_pronada', 'aquecimento_ombro', 'aquecimento', 'compromete_deltoide_anterior', 'compromete_peitoral', 'compromete_triceps', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': []
    },
    {
        'id': 23,
        'nome': 'APOIO SOLO JOELHO NO CHÃO',
        'articulacao': ['ombro', 'cotovelo'],
        'musculo': ['peitoral', 'triceps', 'deltoide'],
        'tempo': tempoDeExecucaoPadrao,
        'objetivos': ['hipertrofia', 'mobilidade'],
        'nivel': ['iniciante'],
        'caracteristicas': ['bilateral', 'biarticular', 'deitado', 'ativacao_core', 'empunhadura_pronada', 'aquecimento_ombro', 'aquecimento', 'compromete_deltoide_anterior', 'compromete_peitoral', 'compromete_triceps', 'reduz_ativacao_cabeca_longa_triceps'],
        'equipamentos': []
    }
]
