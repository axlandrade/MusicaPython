# sound_generator.py
import numpy as np
from scipy.io import wavfile
import funcoes
import os

SAMPLE_RATE = 44100
AMPLITUDE_PICO = 4096
DIRETORIO_SAIDA = 'data'

# A função agora recebe as listas de notas e durações
def gerar_musica_e_salvar(notes, durations, output_filename="output.wav"):
    """
    Gera música a partir de uma lista de notas e durações e salva em .wav.
    """
    print(f"Gerando áudio para {len(notes)} notas...")
    
    # Parâmetros de síntese (podemos transformá-los em parâmetros da UI no futuro)
    sustain_level = 0.1
    factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01, 0.01]
    length = [0.01, 0.29, 0.6, 0.1]
    decay = [0.05, 0.02, 0.005, 0.1]
    
    # Usa a função get_song_data com as notas e durações fornecidas
    # Nota: A função apply_pedal pode não fazer sentido para todos os MIDIs.
    # Por enquanto, vamos usar um valor de compasso fixo.
    bar_value = 4.0 
    
    # O get_song_data pode precisar de ajustes dependendo do MIDI, mas vamos testar
    data = funcoes.get_song_data(
        notes, durations, bar_value, factor, length, decay, sustain_level
    )

    if data.size == 0:
        print("Nenhum dado de áudio foi gerado.")
        return None

    data = data * (AMPLITUDE_PICO / np.max(np.abs(data)))

    os.makedirs(DIRETORIO_SAIDA, exist_ok=True)
    caminho_arquivo = os.path.join(DIRETORIO_SAIDA, output_filename)
    wavfile.write(caminho_arquivo, SAMPLE_RATE, data.astype(np.int16))
    
    return caminho_arquivo