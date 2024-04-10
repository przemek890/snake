# Jedynie niezbędne zależności do wdrożenia
FROM python:3

# Skopiowanie skompilowanego kodu źródłowy i zależności z obrazu budowy
COPY --from=snake_builder /snake /app

WORKDIR /app

RUN pip install --no-cache-dir numpy

CMD ["python3", "run.py"]
