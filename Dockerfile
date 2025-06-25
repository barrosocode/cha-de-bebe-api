# Usa uma imagem oficial Python como base. Mude para a versão que seu Django 5.x exige.
# Python 3.10 é compatível com Django 5.x
FROM python:3.11-slim

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências de compilação para mysqlclient
# Isso inclui ferramentas de compilação e bibliotecas do cliente MySQL.
# `apt-get update` para atualizar a lista de pacotes
# `apt-get install -y` para instalar os pacotes necessários
# `rm -rf /var/lib/apt/lists/*` para limpar o cache do apt e manter a imagem menor
# Também instala netcat-traditional para o script wait-for-it.sh
# E agora, instala o curl!
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    netcat-traditional \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Baixar o wait-for-it
RUN curl -o /wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /wait-for-it.sh

# Copia o arquivo requirements.txt para o contêiner
# Isso permite que o Docker use o cache se o requirements.txt não mudar
COPY requirements.txt /app/

# Instala as dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o script wait-for-it.sh para o contêiner e o torna executável
# Certifique-se de que o script 'wait-for-it.sh' está no mesmo diretório que este Dockerfile
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

COPY . .

# Usar o wait-for-it para aguardar o banco antes de iniciar o Django
CMD ["/wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# ============================================================================================

# # Usa uma imagem oficial Python como base. Mude para a versão que seu Django 5.x exige.
# # Python 3.10 é compatível com Django 5.x
# FROM python:3.11-slim

# # Define variáveis de ambiente
# ENV PYTHONUNBUFFERED=1

# # Define o diretório de trabalho dentro do contêiner
# WORKDIR /app

# # Instala as dependências de compilação para mysqlclient
# # Isso inclui ferramentas de compilação e bibliotecas do cliente MySQL.
# # `apt-get update` para atualizar a lista de pacotes
# # `apt-get install -y` para instalar os pacotes necessários
# # `rm -rf /var/lib/apt/lists/*` para limpar o cache do apt e manter a imagem menor
# # Também instala netcat-traditional para o script wait-for-it.sh
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     build-essential \
#     default-libmysqlclient-dev \
#     pkg-config \
#     netcat-traditional && \
#     rm -rf /var/lib/apt/lists/*

# # Baixar o wait-for-it
# RUN curl -o /wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
#     && chmod +x /wait-for-it.sh

# # Copia o arquivo requirements.txt para o contêiner
# # Isso permite que o Docker use o cache se o requirements.txt não mudar
# COPY requirements.txt /app/

# # Instala as dependências Python
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copia o script wait-for-it.sh para o contêiner e o torna executável
# # Certifique-se de que o script 'wait-for-it.sh' está no mesmo diretório que este Dockerfile
# COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
# RUN chmod +x /usr/local/bin/wait-for-it.sh

# COPY . .

# # Usar o wait-for-it para aguardar o banco antes de iniciar o Django
# CMD ["/wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]


# # Copia todo o resto do código da sua aplicação para o contêiner
# COPY . /app/

# # Expõe a porta que sua aplicação Django vai escutar.
# EXPOSE 8000

# # Comando padrão para iniciar a aplicação Django.
# # Agora, o CMD usa o script wait-for-it.sh para esperar pelo serviço 'db' na porta 3306
# CMD ["wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
