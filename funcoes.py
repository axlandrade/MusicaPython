#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funcoes Utilitarias pra escrever musica em Python

@Autor: Axl
"""
import numpy as np

# funcoes.py

def get_piano_notes():
    '''
    Gera as frequências em hertz para as teclas de um piano.
    Versão modificada para incluir todas as notas de 9 oitavas,
    não apenas as 88 teclas padrão.

    Retorna
    -------
    note_freqs : dicionario
        Mapeamento entre o nome da nota e a sua frequencia
    '''
    
    # Teclas brancas em maiusculo e teclas pretas em minusculo
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 440 # Frequência da nota A4
    
    # Gera todas as notas de 9 oitavas (0 a 8)
    keys = np.array([x+str(y) for y in range(0,9) for x in octave])
    
    # --- ALTERAÇÃO PRINCIPAL ---
    # Removemos o corte para 88 teclas para suportar qualquer nota
    # que o MIDI possa ter dentro dessas 9 oitavas.
    # start = np.where(keys == 'A0')[0][0]
    # end = np.where(keys == 'C8')[0][0]
    # keys = keys[start:end+1]
    
    # Calcula as frequências para todas as chaves geradas
    # A fórmula continua a mesma, baseada na nota A4 como referência (a 49ª tecla)
    note_freqs = dict(zip(keys, [2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
    note_freqs[''] = 0.0 # stop
    
    return note_freqs

def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    '''
    Obtem a onda senoidal.

    Parametros
    ----------
    frequency : float
        Frequencia em hertz.
    duration : float
        Tempo em segundos.
    sample_rate : int, optional
        Taxa de amostragem do arquivo wav. O padrao e 44100
    amplitude : int, optional
        Pico de amplitude. O padrao e 4096

    Retorna
    -------
    wave : TYPE
        Descricao.

    '''
    t = np.linspace(0, duration, int(sample_rate*duration))
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

def apply_overtones(frequency, duration, factor, sample_rate=44100, amplitude=4096):
    '''
    Retorna a fundamental com os sobretons aplicados.

    Parametros
    ----------
    frequency : float
        Frequencia em hertz
    duration : float
        Tempo em segundos.
    factor : list
        Lista dos flutuantes como fracoes da fundamental, amplitude por amplitude dos sobretons.
    sample_rate : int, optional
        Taxa de amostragem do arquivo WAV. O padrao e 44100
    amplitude : int, optional
        Pico de amplitude, o padrao e 4096

    Retorna
    -------
    fundamental : ndarray
        Nota de saida do tipo "float"

    '''
    assert abs(1-sum(factor)) < 1e-8
    
    frequencies = np.minimum(np.array([frequency*(x+1) for x in range(len(factor))]), sample_rate//2)
    amplitudes = np.array([amplitude*x for x in factor])
    
    fundamental = get_sine_wave(frequencies[0], duration, sample_rate, amplitudes[0])
    for i in range(1, len(factor)):
        overtone = get_sine_wave(frequencies[i], duration, sample_rate, amplitudes[i])
        fundamental += overtone
    return fundamental

def get_adsr_weights(duration, length, decay, sustain_level, sample_rate=44100):
    """
    Gerador de envelope ADSR (ataque, decaimento, sustentação e liberação)
    com uma lógica matemática mais robusta para evitar erros de arredondamento.
    """
    # Calcula o número total de amostras de forma consistente
    num_samples = int(duration * sample_rate)
    if num_samples == 0:
        return np.array([])

    # Calcula o número de amostras para cada estágio do ADSR
    len_A = int(length[0] * num_samples)
    len_D = int(length[1] * num_samples)
    len_S = int(length[2] * num_samples)
    
    # O estágio de Release (R) pega todas as amostras restantes para garantir o tamanho exato
    len_R = num_samples - len_A - len_D - len_S
    if len_R < 0: len_R = 0 # Garante que não seja negativo

    # Gera cada estágio (usando interpolação linear, que é mais estável)
    A = np.linspace(0, 1, len_A, endpoint=False)
    D = np.linspace(1, sustain_level, len_D, endpoint=False)
    S = np.full(len_S, sustain_level)
    R = np.linspace(sustain_level, 0, len_R, endpoint=False) if len_R > 0 else np.array([])

    # Concatena todos os estágios
    weights = np.concatenate((A, D, S, R))
    
    # Garante que o array final tenha o tamanho EXATO, corrigindo qualquer desvio de 1 amostra
    if len(weights) < num_samples:
        weights = np.append(weights, np.zeros(num_samples - len(weights)))
    
    return weights[:num_samples]

def apply_pedal(note_values, bar_value):
    '''
    Pressiona e segura o pedal de sustain atraves do compasso.

    Parametros
    ----------
    note_values : list
        Lista de duracao das notas
    bar_value : float
        Duracao de uma medida em segundos.


    Retorno
    -------
    new_values : list
        Lista da duracao das notas com sustain.

    '''
    assert sum(note_values) % bar_value == 0
    new_values = []
    start = 0
    while True:
        cum_value = np.cumsum(np.array(note_values[start:]))
        end = np.where(cum_value == bar_value)[0][0]
        if end == 0:
            new_values += [note_values[start]]
        else:
            this_bar = np.array(note_values[start:start+end+1])
            new_values += [bar_value-np.sum(this_bar[:i]) for i in range(len(this_bar))]
        start += end+1
        if start == len(note_values):
            break
    return new_values

# funcoes.py

# funcoes.py

def get_song_data(music_notes, note_values, bar_value, factor, length,
                  decay, sustain_level, sample_rate=44100, amplitude=4096):
    """
    Gera musicas a partir das notas. (Versão final e robusta)
    """
    note_freqs = get_piano_notes()
    frequencies = [note_freqs.get(note, 0) for note in music_notes]

    total_duration_sec = sum(note_values)
    if total_duration_sec == 0:
        return np.array([])
        
    duration_total_samples = int(total_duration_sec * sample_rate)
    song = np.zeros((duration_total_samples,))
    
    # Calcula os pontos de início e fim de cada nota em amostras. Esta é nossa fonte de verdade.
    cumulative_duration_samples = np.cumsum(np.array([0] + note_values) * sample_rate).astype(int)
    
    for i in range(len(music_notes)):
        if frequencies[i] > 0 and note_values[i] > 0:
            start_idx = cumulative_duration_samples[i]
            end_idx = cumulative_duration_samples[i+1]

            # O número de amostras para esta nota é a diferença entre o fim e o início.
            num_samples_for_note = end_idx - start_idx
            if num_samples_for_note <= 0:
                continue

            # A duração em segundos é derivada deste número exato de amostras.
            duration_sec_for_note = num_samples_for_note / sample_rate

            # Geramos a onda e o envelope usando esta duração precisa.
            this_note = apply_overtones(frequencies[i], duration_sec_for_note, factor, sample_rate, amplitude)
            weights = get_adsr_weights(duration_sec_for_note, length, decay, sustain_level, sample_rate)

            # Por segurança, garantimos que os arrays tenham o tamanho exato do nosso espaço.
            final_len = min(num_samples_for_note, len(this_note), len(weights))
            
            # Adiciona a nota gerada no array da música.
            song[start_idx : start_idx + final_len] += this_note[:final_len] * weights[:final_len]

    if np.max(np.abs(song)) > 0:
        song = song * (amplitude / np.max(np.abs(song)))
        
    return song

<<<<<<< HEAD
=======
# funcoes.py

# ... (todas as outras funções continuam aqui) ...

>>>>>>> 69f1097 (Adds multi-instrument MIDI synthesis support)
def generate_note_audio(frequency, duration, timbre, sample_rate=44100, amplitude=4096):
    """
    Gera o áudio para uma única nota com um timbre específico.
    """
    if frequency <= 0 or duration <= 0:
        return np.array([])

    # Gera a onda base com sobretons
    note_wave = apply_overtones(
        frequency,
        duration,
        timbre['factor'],
        sample_rate,
        amplitude
    )
    
    # Gera o envelope ADSR para a nota
    weights = get_adsr_weights(
        duration,
        timbre['length'],
        timbre['decay'],
        timbre['sustain_level'],
        sample_rate
    )
    
    # Garante que os tamanhos sejam compatíveis antes de multiplicar
    min_len = min(len(note_wave), len(weights))
    
<<<<<<< HEAD
    return note_wave[:min_len] * weights[:min_len]
=======
    return note_wave[:min_len] * weights[:min_len]
>>>>>>> 69f1097 (Adds multi-instrument MIDI synthesis support)
