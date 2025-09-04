import streamlit as st
import sound_generator # Importa nosso novo módulo gerador
import midi_parser     # Importa nosso novo módulo parser
import os

st.set_page_config(layout="wide")

st.title('🎵 Sintetizador de Música a partir de Arquivos MIDI')

st.write(
    "Faça o upload de um arquivo MIDI (`.mid`) e este aplicativo irá sintetizar o áudio "
    "usando ondas senoidais e o salvará como um arquivo `.wav`."
)

# Componente de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo .mid", type="mid")

if uploaded_file is not None:
    # Para ler o arquivo, precisamos salvá-lo temporariamente
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    temp_midi_path = os.path.join(temp_dir, uploaded_file.name)
    
    with open(temp_midi_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info(f"Arquivo `{uploaded_file.name}` carregado. Clique no botão para gerar o áudio.")

    # Botão para iniciar a síntese
    if st.button('Sintetizar Áudio'):
        # 1. Parse o arquivo MIDI
        with st.spinner("Lendo o arquivo MIDI..."):
            notes, durations = midi_parser.parse_midi_file(temp_midi_path)

        if notes and durations:
            st.write(f"Arquivo MIDI processado. {len(notes)} notas encontradas.")
            
            # 2. Gere o áudio com base nas notas e durações
            with st.spinner('Sintetizando áudio, isso pode levar um momento...'):
                output_wav_name = os.path.splitext(uploaded_file.name)[0] + ".wav"
                caminho_do_arquivo = sound_generator.gerar_musica_e_salvar(notes, durations, output_wav_name)
            
            if caminho_do_arquivo:
                st.success(f'Áudio gerado com sucesso! 🎶')
                
                # 3. Mostre o player de áudio e o botão de download
                audio_file = open(caminho_do_arquivo, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/wav')
                
                st.download_button(
                    label="Baixar arquivo .wav",
                    data=audio_bytes,
                    file_name=output_wav_name,
                    mime="audio/wav"
                )
            else:
                st.error("Ocorreu um erro durante a geração do áudio.")
        else:
            st.error("Não foi possível extrair notas do arquivo MIDI. Tente outro arquivo.")