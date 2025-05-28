FROM python:3.13-alpine AS builder

WORKDIR /build
RUN python -m venv .env && .env/bin/pip install --no-cache-dir -U pip setuptools
COPY requirements.txt .
RUN .env/bin/pip install --no-cache-dir -r requirements.txt && \
    find /build/.env \( -type d -a -name test -o -name tests \) -o \
        \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' +


FROM python:3.13-alpine AS runner
WORKDIR /app

COPY --from=builder /build /app
COPY . /app
RUN crontab crontab

CMD ["crond", "-f"]
