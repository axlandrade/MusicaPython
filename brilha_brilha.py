#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contém a lógica para gerar a música "Brilha Brilha Estrelinha".
Refatorado para ser chamado como um módulo.

@Autor: Axl
"""
import numpy as np
from scipy.io import wavfile
import funcoes
import os

# --- Constantes e Configurações ---
SAMPLE_RATE = 44100
AMPLITUDE_PICO = 4096
DIRETORIO_SAIDA = 'data'
NOME_ARQUIVO_SAIDA = 'brilha_brilha.wav'
DURACAO_COMPASSO = 2.0

# Movida a lógica principal para uma função que podemos chamar
def gerar_musica_e_salvar():
    """
    Gera a música completa, salva o arquivo .wav e retorna o caminho do arquivo.
    """
    # --- Definição da Melodia e Acompanhamento ---
    right_hand_notes = ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4', 'F4', 'F4', 'E4', 'E4',
                       'D4', 'D4', 'C4', 'G4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4', 'G4',
                       'G4', 'F4', 'F4', 'E4', 'E4', 'D4', 'C4', 'C4', 'G4', 'G4', 'A4',
                       'A4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4',]
    right_hand_duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0] * 6

    left_hand_notes = ['C3', 'A3', 'F3', 'D3', 'C3', 'G3', 'F3', 'E3', 'D3', 'G3', 'F3',
                       'E3', 'D3', 'C3', 'E3', 'G3', 'C4', 'A3', 'A3', 'G3', 'F3', 'B2',
                       'E3', 'C3', 'D3', 'D3', 'C3']
    left_hand_duration = [2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                          1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0, 0.5, 0.5, 0.5, 0.5,
                          0.5, 0.5, 1.0]

    # --- Parâmetros de Síntese de Som (Timbre) ---
    sustain_level = 0.1
    factor_rh = [0.68, 0.26, 0.03, 0.0, 0.03]
    length_rh = [0.01, 0.6, 0.29, 0.1]
    decay_rh = [0.05, 0.02, 0.005, 0.1]
    factor_lh = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01, 0.01]
    length_lh = [0.01, 0.29, 0.6, 0.1]
    decay_lh = [0.05, 0.02, 0.005, 0.1]

    # --- Geração do Áudio ---
    right_hand = funcoes.get_song_data(right_hand_notes, right_hand_duration, DURACAO_COMPASSO,
                                     factor_rh, length_rh, decay_rh, sustain_level)
    left_hand = funcoes.get_song_data(left_hand_notes, left_hand_duration, DURACAO_COMPASSO,
                                    factor_lh, length_lh, decay_lh, sustain_level)

    data = left_hand + right_hand
    data = data * (AMPLITUDE_PICO / np.max(np.abs(data)))

    # --- Salvando o Arquivo .wav ---
    os.makedirs(DIRETORIO_SAIDA, exist_ok=True)
    caminho_arquivo = os.path.join(DIRETORIO_SAIDA, NOME_ARQUIVO_SAIDA)
    wavfile.write(caminho_arquivo, SAMPLE_RATE, data.astype(np.int16))
    
    return caminho_arquivo

# Permite que o script ainda seja executável diretamente, se quisermos
if __name__ == "__main__":
    print("Executando o modo de geração de música direta...")
    caminho = gerar_musica_e_salvar()
    print(f"Música salva em: {caminho}")