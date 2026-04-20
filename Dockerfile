FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

RUN mkdir -p certs && \
    openssl genrsa -out certs/private.pem 2048 && \
    openssl rsa -in certs/private.pem -pubout -out certs/public.pem

RUN pip install --upgrade pip wheel uv

COPY pyproject.toml uv.lock prestart.sh ./

RUN uv pip compile ./pyproject.toml -o requirements.txt
RUN uv pip install -r requirements.txt

COPY src ./src

ENTRYPOINT ["./prestart.sh"]
CMD ["python", "-m", "src.__main__"]