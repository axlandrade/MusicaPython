# Use uma imagem oficial do Python como base. A versão 'slim' é mais leve.
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /workspace

# Instala o Git e outras dependências do sistema operacional
# É uma boa prática fazer o update, install e clean na mesma camada RUN
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
# A flag --no-cache-dir mantém a imagem um pouco menor
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do seu projeto para o diretório de trabalho no container
COPY . .

# Comando padrão a ser executado quando o container iniciar (opcional para Dev Containers,
# mas é uma boa prática). Quando o container rodar, ele vai gerar a música.
CMD ["python", "brilha_brilha.py"]