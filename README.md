# Música com Python: Geração de "Brilha Brilha Estrelinha"

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Este projeto, parte de um Trabalho de Conclusão de Curso, demonstra a síntese de áudio em Python para gerar a melodia e o acompanhamento da canção "Brilha Brilha Estrelinha". O som é construído a partir de ondas senoidais puras, que são enriquecidas com sobretons (harmônicos) e moldadas por um envelope ADSR (Ataque, Decaimento, Sustentação e Liberação) para simular o timbre de um instrumento musical.

## 🎶 Demonstração de Áudio

O resultado final é um arquivo `.wav` que pode ser ouvido aqui:
*(Dica: Após gerar o arquivo `brilha_brilha.wav`, você pode subí-lo para o repositório e colocar um link direto para ele aqui)*

## 📂 Estrutura do Projeto

O repositório está organizado da seguinte forma:

```
MusicaPython/
├── .gitignore
├── LICENSE
├── README.md
├── brilha_brilha.py
├── funcoes.py
├── requirements.txt
└── data/
    └── (esta pasta será criada para o arquivo .wav gerado)
```

- **`brilha_brilha.py`**: O script principal que define a melodia, o acompanhamento e os parâmetros sonoros, orquestrando a geração da música.
- **`funcoes.py`**: Módulo utilitário contendo o "motor" de síntese de som (geração de ondas, ADSR, sobretons, etc.).
- **`requirements.txt`**: Lista as dependências do projeto.
- **`LICENSE`**: Contém a licença do projeto (GPLv3).
- **`data/`**: Diretório onde o arquivo de áudio `brilha_brilha.wav` será salvo.

## 🚀 Como Executar

Para gerar o arquivo de áudio, siga os passos abaixo. Recomenda-se o uso de um ambiente virtual (`venv`).

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/MusicaPython.git](https://github.com/seu-usuario/MusicaPython.git)
    cd MusicaPython
    ```

2.  **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script principal:**
    ```bash
    python brilha_brilha.py
    ```

Após a execução, o arquivo `brilha_brilha.wav` estará disponível no diretório `data/`.

## 🛠️ Detalhes Técnicos

O processo de síntese de som envolve os seguintes conceitos implementados no módulo `funcoes.py`:

- **Frequências de Notas**: Um dicionário mapeia nomes de notas de piano (ex: "C4") para suas frequências em Hertz.
- **Geração de Onda Senoidal**: A base de cada nota é uma onda senoidal pura.
- **Sobretons (Harmônicos)**: Para criar um timbre mais rico e realista, múltiplos senoides (harmônicos) com amplitudes menores são somados à frequência fundamental da nota.
- **Envelope ADSR**: A amplitude de cada nota é modulada ao longo do tempo para simular a forma como o som de um instrumento evolui:
  - **Ataque (Attack)**: O tempo que o som leva para atingir a amplitude máxima.
  - **Decaimento (Decay)**: O tempo para o som diminuir até o nível de sustentação.
  - **Sustentação (Sustain)**: O nível de amplitude mantido enquanto a nota é segurada.
  - **Liberação (Release)**: O tempo que o som leva para desaparecer após a nota ser solta.

## 💡 Possíveis Melhorias

Este projeto serve como uma base sólida para explorações futuras em síntese musical. Algumas ideias:

- [ ] Refatorar o código para ler notas e durações de um formato de arquivo padrão (como MIDI ou MusicXML).
- [ ] Criar uma interface gráfica simples (com `Tkinter` ou `PyQt`) para visualizar a partitura ou alterar parâmetros.
- [ ] Experimentar com outras formas de onda (quadrada, triangular, dente de serra) para criar timbres diferentes.
- [ ] Implementar mais efeitos de áudio, como reverb ou vibrato.

## licença

Este projeto está licenciado sob a Licença Pública Geral GNU v3.0 - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

- **Axl** - *Desenvolvimento do Código*