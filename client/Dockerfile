# Usa una imagen base de Python
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiar el script wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

EXPOSE 8080

# Ejecutar wait-for-it.sh para esperar el API Gateway antes de iniciar el cliente
CMD ["/wait-for-it.sh", "api-gateway:5000", "--", "python", "app.py"]
