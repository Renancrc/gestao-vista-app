# syntax=docker/dockerfile:1

# ---------- Estágio 1: compila o React (gera HTML, JS e CSS estáticos) ----------
FROM node:24-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# ---------- Estágio 2: só o nginx com os arquivos prontos (sem Node) ----------
FROM nginxinc/nginx-unprivileged:1.29-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8080
