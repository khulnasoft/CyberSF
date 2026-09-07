FROM python:3.9-alpine

LABEL org.opencontainers.image.title="cybersf" \
      org.opencontainers.image.description="A Modular Penetration Testing Framework" \
      org.opencontainers.image.authors="khulnasoft <contact@khulnasoft.com>" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="https://github.com/khulnasoft/cybersf" \
      org.opencontainers.image.documentation="https://khulnasoft.com/"

# Environment variables for efficient builds
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY . /cybersf
WORKDIR /cybersf

RUN apk add --update --no-cache git nmap && pip install -e .

CMD ["--info"]
ENTRYPOINT ["cybersf"]
