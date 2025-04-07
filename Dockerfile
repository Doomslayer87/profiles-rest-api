FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive

# Disattiva i servizi non necessari (simulando il disable di apt-daily)
RUN systemctl mask apt-daily.service apt-daily.timer || true

# Installa i pacchetti richiesti
RUN apt-get update && \
    apt-get install -y python3-venv zip && \
    apt-get clean

# Aggiungi alias per "python"
RUN echo "# PYTHON_ALIAS_ADDED" >> /root/.bash_aliases && \
    echo "alias python='python3'" >> /root/.bash_aliases

# Imposta bash come shell di default (utile per alias e interattività)
SHELL ["/bin/bash", "-c"]

# Imposta la directory di lavoro
WORKDIR /app

# Espone la porta 8000 come nel Vagrantfile
EXPOSE 8000

CMD ["bash"]
