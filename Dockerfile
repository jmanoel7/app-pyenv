# imagem basica 'Debian Stretch'
FROM debian:stretch

# configura repositorios e troca locale para 'pt_BR.UTF-8'
RUN echo 'deb http://sft.if.usp.br/debian/ stretch main' > /etc/apt/sources.list \
    && echo 'deb-src http://sft.if.usp.br/debian/ stretch main' >> /etc/apt/sources.list \
    && echo 'deb http://sft.if.usp.br/debian/ stretch-updates main' >> /etc/apt/sources.list \
    && echo 'deb-src http://sft.if.usp.br/debian/ stretch-updates main' >> /etc/apt/sources.list \
    && echo 'deb http://sft.if.usp.br/debian-security/ stretch/updates main' >> /etc/apt/sources.list \
    && echo 'deb-src http://sft.if.usp.br/debian-security/ stretch/updates main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends locales \
    && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG pt_BR.UTF-8

# adiciona os pacotes necessarios para instalacao do pyenv
RUN apt-get install -y --no-install-recommends \
	bash-completion vim-nox git \
	make build-essential libssl1.0-dev zlib1g-dev libbz2-dev \
	libreadline-dev libsqlite3-dev wget curl llvm \
	libncurses5-dev libncursesw5-dev \
	xz-utils tk-dev libcurl4-openssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

# configura o ambiente
RUN mkdir -p /opt/app/app && \
    mkdir -p /opt/app/config && \
    mkdir -p /opt/app/log && \
    mkdir -p /opt/app/data
WORKDIR /opt/app
EXPOSE 80
ENV APP_ROOT   /opt/app
ENV APP_CONFIG /opt/app/config
ENV APP_APP    /opt/app/app
ENV APP_LOG    /opt/app/log
ENV APP_DATA   /opt/app/data
ENV SHELL /bin/bash
ENV HOME /root
USER root

# adiciona arquivos do app
ADD ./config /opt/app/config
ADD ./app    /opt/app/app

# instala python via pyenv
RUN chmod a+x "${APP_CONFIG}/pyenv_install.sh" && \
    /bin/bash -c "${APP_CONFIG}/pyenv_install.sh"
RUN chmod a+x "${APP_CONFIG}/pyenv_pip.sh" && \
    /bin/bash -c "${APP_CONFIG}/pyenv_pip.sh"

# instala os modulos python
RUN chmod a+x "${APP_CONFIG}/venv_install.sh" && \
    /bin/bash -c "${APP_CONFIG}/venv_install.sh"

# configura as permissoes de shell scripts
RUN chmod a+x   "${APP_APP}/flask_run.sh"

# SOMENTE PARA TESTES COM OS DADOS PRIVADOS !!!
# NUNCA FACA A PUBLICACAO DA IMAGEM COM DADOS PRIVADOS !!!
#ADD ./data       /opt/app/data
#ADD ./log        /opt/app/log

# executa o app
CMD /bin/bash -c "${APP_APP}/flask_run.sh"
