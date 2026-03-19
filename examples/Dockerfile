FROM postgres:16

RUN apt-get update && apt-get install -y locales \
    && echo "es_MX.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen es_MX.UTF-8 \
    && rm -rf /var/lib/apt/lists/*