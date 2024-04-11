FROM python:3.11

COPY --from=snake_builder /snakesss/snake /app

WORKDIR /app

RUN pip install --no-cache-dir numpy matplotlib

CMD ["python3", "snakesss/run.py"]
