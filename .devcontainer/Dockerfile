# Use uma imagem oficial do Python como base. A versão 'slim' é mais leve.
FROM python:3.10-slim-bookworm

# Define o diretório de trabalho dentro do container
WORKDIR /app

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