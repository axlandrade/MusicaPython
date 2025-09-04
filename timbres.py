# timbres.py

# Timbre padrão, caso o instrumento do MIDI não seja reconhecido
TIMBRE_PADRAO = {
    'factor': [0.73, 0.16, 0.06, 0.01, 0.02, 0.01, 0.01],
    'length': [0.01, 0.29, 0.6, 0.1],
    'decay': [0.05, 0.02, 0.005, 0.1],
    'sustain_level': 0.1
}

# Um dicionário com presets de timbres. A chave é o "program number" do MIDI.
# 0 = Piano Acústico, 32 = Baixo Acústico
PRESETS = {
    0: { # Piano Acústico
        'factor': [0.68, 0.26, 0.03, 0.0, 0.03],
        'length': [0.01, 0.6, 0.29, 0.1],
        'decay': [0.05, 0.02, 0.005, 0.1],
        'sustain_level': 0.1
    },
    32: { # Baixo Acústico
        'factor': [0.8, 0.1, 0.05, 0.05], # Mais fundamental, menos harmônicos
        'length': [0.02, 0.2, 0.7, 0.08], # Sustain mais longo
        'decay': [0.05, 0.02, 0.005, 0.1],
        'sustain_level': 0.2
    }
}

def get_timbre(program_number):
    """
    Retorna os parâmetros de timbre para um dado 'program number' de instrumento MIDI.
    Se o número não estiver nos presets, retorna o timbre padrão.
    """
    return PRESETS.get(program_number, TIMBRE_PADRAO)