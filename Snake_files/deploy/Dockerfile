# Jedynie niezbędne zależności do wdrożenia
FROM python:3-slim

# Skopiowanie skompilowanego kodu źródłowy i zależności z obrazu budowy
COPY --from=snake_builder /snake /app

WORKDIR /app

CMD ["python3", "run.py"]
