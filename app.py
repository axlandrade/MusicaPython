import streamlit as st
import brilha_brilha # Importa nosso script refatorado

# Título da nossa aplicação
st.title('🎵 Gerador de Música com Python')

st.write(
    "Esta é uma interface simples para o projeto MusicaPython. "
    "Clique no botão abaixo para gerar a música 'Brilha Brilha Estrelinha'."
)

# Cria um botão
if st.button('Gerar Música'):
    
    # Exibe uma mensagem de progresso
    with st.spinner('Sintetizando áudio, por favor aguarde...'):
        # Chama a função que gera e salva a música
        caminho_do_arquivo = brilha_brilha.gerar_musica_e_salvar()
    
    # Exibe uma mensagem de sucesso
    st.success(f'Música gerada com sucesso! 🎶')
    
    # Abre o arquivo de áudio e o exibe em um player na página
    audio_file = open(caminho_do_arquivo, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
    
    # Oferece o arquivo para download
    st.download_button(
        label="Baixar arquivo .wav",
        data=audio_bytes,
        file_name="brilha_brilha.wav",
        mime="audio/wav"
    )