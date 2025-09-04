# app.py
import streamlit as st
import sound_generator
import midi_parser
import os

st.set_page_config(layout="wide")

st.title('🎵 Sintetizador de Música Multi-Instrumental a partir de MIDI')

st.write(
    "Faça o upload de um arquivo MIDI (`.mid`) com um ou mais instrumentos. "
    "O aplicativo irá sintetizar e mixar o áudio em um arquivo `.wav`."
)

uploaded_file = st.file_uploader("Escolha um arquivo .mid", type="mid")

if uploaded_file is not None:
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    temp_midi_path = os.path.join(temp_dir, uploaded_file.name)
    
    with open(temp_midi_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button('Sintetizar Áudio'):
        with st.spinner("Lendo e separando as trilhas do MIDI..."):
            parsed_tracks = midi_parser.parse_midi_file(temp_midi_path)

        if parsed_tracks:
            st.write(f"Arquivo MIDI processado. {len(parsed_tracks)} trilhas de instrumentos encontradas:")
            for track in parsed_tracks:
                st.text(f" - Trilha: '{track['name']}' (Instrumento MIDI #{track['program_number']}) com {len(track['notes'])} notas.")
            
            with st.spinner('Sintetizando e mixando o áudio... Isso pode demorar bastante!'):
                output_wav_name = os.path.splitext(uploaded_file.name)[0] + ".wav"
                caminho_do_arquivo = sound_generator.gerar_musica_e_salvar(parsed_tracks, output_wav_name)
            
            if caminho_do_arquivo:
                st.success(f'Áudio mixado com sucesso! 🎶')
                
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
            st.error("Não foi possível extrair nenhuma trilha de instrumento do arquivo MIDI.")