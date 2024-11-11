# Geração de "Brilha Brilha Estrelinha" com Ondas Senoidais

Este projeto sintetiza a música "Brilha Brilha Estrelinha" usando ondas senoidais puras para representar cada nota musical. O código aplica conceitos de síntese de som, incluindo sobretons (harmônicos) e envelopes ADSR (ataque, decaimento, sustentação e liberação) para moldar o timbre e a dinâmica de cada nota, criando uma melodia com acompanhamento que é exportada para um arquivo `.wav`.

## Estrutura do Código

### Arquivo `brilha_brilha.py`

O arquivo `brilha_brilha.py` define as notas e durações da melodia e do acompanhamento, configurando os parâmetros de som para cada nota.

1. **Definição das Notas e Durações**:
   - `right_hand_notes` e `left_hand_notes` contêm as notas da melodia e do acompanhamento, respectivamente.
   - `right_hand_duration` e `left_hand_duration` definem a duração de cada nota, garantindo que cada uma seja tocada no tempo correto.

2. **Parâmetros de Som e Configuração do ADSR**:
   - Harmônicos (`factor`), envelope ADSR (`length` e `decay`), e nível de sustentação (`sustain_level`) são ajustados para moldar o som das notas, simulando o comportamento de instrumentos reais.

3. **Geração das Ondas**:
   - A função `get_song_data` (do módulo `funcoes`) gera ondas senoidais para cada nota, aplicando sobretons e o envelope ADSR. O resultado é uma onda contínua para cada "mão" (direita e esquerda).
   - As ondas da melodia e do acompanhamento são combinadas para formar a música completa.

4. **Exportação do Áudio**:
   - O resultado final é normalizado e salvo em um arquivo `.wav` chamado `brilha_brilha.wav`.

### Arquivo `funcoes.py`

O `funcoes.py` contém funções essenciais para gerar ondas senoidais, aplicar sobretons e envelopes ADSR. Estas funções permitem simular a qualidade de som de instrumentos musicais. 

1. **Função `get_piano_notes`**:
   - Gera um dicionário com a frequência de cada nota no teclado padrão do piano (88 teclas), permitindo fácil acesso às frequências corretas para as notas nomeadas, como "C4" ou "A4".

2. **Função `get_sine_wave`**:
   - Cria uma onda senoidal simples com uma frequência, duração e amplitude especificadas, gerando o som fundamental de cada nota.

3. **Função `apply_overtones`**:
   - Adiciona sobretons (harmônicos) à nota base usando uma lista de fatores que representam frações da amplitude da fundamental para cada harmônico. Isso enriquece o som e o torna mais realista.

4. **Função `get_adsr_weights`**:
   - Implementa um envelope ADSR (Ataque, Decaimento, Sustentação, Liberação), que ajusta a amplitude da onda ao longo do tempo, simulando o comportamento dinâmico de instrumentos.

5. **Função `apply_pedal`**:
   - Extende a duração das notas dentro de uma medida, simulando o uso do pedal de sustain de um piano.

6. **Função `get_song_data`**:
   - A função central do `funcoes.py`. Ela usa `apply_overtones` e `get_adsr_weights` para criar a sequência de ondas para cada nota e organiza as notas conforme suas durações para formar a música final.

## Como Executar

1. **Instale as dependências necessárias**:
   - As bibliotecas `numpy` e `scipy` são necessárias para rodar o código.
   ```bash
   pip install numpy scipy

2. **Rode o arquivo brilha_brilha.py para gerar o arquivo de áudio brilha_brilha.wav.
    Execute o script:
   ```bash
   python brilha_brilha.py
3. **O arquivo brilha_brilha.wav estará disponível na pasta data.
