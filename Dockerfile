# Base leve do sistema
FROM python:3.11-slim

# Pasta central de operações
WORKDIR /app

# Garante o buffer imediato de logs (sem atraso na saída do terminal)
ENV PYTHONUNBUFFERED=1

# Injeta o código local no container
COPY src/ /app/src/

# Gatilho que dispara a execução
CMD ["python", "src/main.py"]
