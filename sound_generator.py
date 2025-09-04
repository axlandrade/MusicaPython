# sound_generator.py
import numpy as np
import funcoes
import timbres
import os
from scipy.io import wavfile

SAMPLE_RATE = 44100
AMPLITUDE_PICO = 4096
DIRETORIO_SAIDA = 'data'

def gerar_musica_e_salvar(instrument_tracks, output_filename="output.wav"):
    """
    Gera áudio para múltiplas trilhas de instrumentos, posicionando cada nota
    em seu tempo absoluto na linha do tempo da música.
    """
    if not instrument_tracks:
        return None

    print("Calculando a duração total da música...")
    # 1. Encontrar o final da última nota para determinar a duração total
    total_duration = 0
    for track in instrument_tracks:
        for note in track['notes']:
            note_end_time = note['start'] + note['duration']
            if note_end_time > total_duration:
                total_duration = note_end_time

    # 2. Criar a "tela" de áudio final, com base na duração total
    total_samples = int(total_duration * SAMPLE_RATE)
    final_mix = np.zeros(total_samples)
    
    print(f"Duração total: {total_duration:.2f} segundos. Iniciando síntese...")
    
    note_freqs = funcoes.get_piano_notes()

    # 3. Iterar sobre cada trilha e cada nota, adicionando-a à "tela"
    for track in instrument_tracks:
        timbre = timbres.get_timbre(track['program_number'])
        print(f"- Sintetizando trilha: '{track['name']}'...")

        for note in track['notes']:
            # Posição de início da nota na linha do tempo (em amostras)
            start_sample = int(note['start'] * SAMPLE_RATE)
            
            # Gera o áudio apenas para esta nota
            frequency = note_freqs.get(note['name'], 0)
            note_audio = funcoes.generate_note_audio(
                frequency,
                note['duration'],
                timbre,
                SAMPLE_RATE,
                AMPLITUDE_PICO
            )
            
            # Posição final da nota
            end_sample = start_sample + len(note_audio)

            # Garante que não vamos escrever fora dos limites do array final
            if end_sample > len(final_mix):
                # Se a nota ultrapassar o final, truncamos o áudio da nota
                note_audio = note_audio[:len(final_mix) - start_sample]
                end_sample = len(final_mix)

            # Adiciona (mixa) o som da nota na posição correta da linha do tempo
            final_mix[start_sample:end_sample] += note_audio

    # 4. Normalizar o resultado final
    print("Normalizando o áudio final...")
    max_amp = np.max(np.abs(final_mix))
    if max_amp > 0:
        final_mix = final_mix * (AMPLITUDE_PICO / max_amp)
    
    # 5. Salvar o arquivo
    os.makedirs(DIRETORIO_SAIDA, exist_ok=True)
    caminho_arquivo = os.path.join(DIRETORIO_SAIDA, output_filename)
    wavfile.write(caminho_arquivo, SAMPLE_RATE, final_mix.astype(np.int16))
    
    return caminho_arquivo