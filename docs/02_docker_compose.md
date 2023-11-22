# Trabalhando com Docker compose

- [Trabalhando com Docker compose](#trabalhando-com-docker-compose)
  - [Criando o compose file](#criando-o-compose-file)
  - [Deploy utilizando compose](#deploy-utilizando-compose)

## Criando o compose file

```bash
version: "3.10"

services:
  db-menu-service:
    image: postgres:15
    networks:
      - "microservices"
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=menu
      - POSTGRES_PASSWORD=dbmenu2023
      - POSTGRES_DB=menu
      - POSTGRES_HOST_AUTH_METHOD=trust
  menu-service:
    image: robertsilvatech/menu-service-playground:0.0.1
    networks:
      - "microservices"
    ports:
      - "8000:8000"
    environment:
      - DATABASE_HOST=menu-service-db-menu-service-1
      - DATABASE_USERNAME=menu
      - DATABASE_PASSWORD=dbmenu2023
      - DATABASE_NAME=menu
    restart: always
networks:
  microservices:
    external: true
```

## Deploy utilizando compose

- Primeiro vamos parar o container do postgresql

```bash
docker container rm -f db-menu-service
```

- Fazer o deploy

```bash
docker compose up -d 
```

- Verificar logs
  - Corrigir endereço do DB

- Fazer o deploy novamente
  - Observe que o container menu-service-menu-service-1 será **recriado**.

- Validar a aplicação utilizando o postman

- Repita o processo para aplicação **order-service**