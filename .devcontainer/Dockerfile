FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm
# Remove o repositorio apt do Yarn: a chave expirada quebra o apt-get update
RUN rm -f /etc/apt/sources.list.d/yarn.list
