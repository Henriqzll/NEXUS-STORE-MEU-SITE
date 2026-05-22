#!/usr/bin/env bash
# Saia imediatamente se qualquer comando falhar
set -o errexit

# Instala todas as dependências que estão no seu requirements.txt
pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS/JS) para o servidor
python manage.py collectstatic --no-input

# Aplica as migrações do banco de dados
python manage.py migrate