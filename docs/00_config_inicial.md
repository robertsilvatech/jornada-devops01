# Configurações iniciais para apresentar as aplicações

- Iniciar na pasta: /home/robertsilvatech/Workspace/me/my-github/jornada-devops01

- [Configurações iniciais para apresentar as aplicações](#configurações-iniciais-para-apresentar-as-aplicações)
  - [Criar rede para os containers](#criar-rede-para-os-containers)
  - [menu-service](#menu-service)
    - [Criar banco de dados postgres-db-menu](#criar-banco-de-dados-postgres-db-menu)
    - [Criar arquivo de variável local na pasta arquivos-iniciais/aplicacoes/menu-service/.env](#criar-arquivo-de-variável-local-na-pasta-arquivos-iniciaisaplicacoesmenu-serviceenv)
    - [Iniciar aplicação](#iniciar-aplicação)
  - [order-service](#order-service)
    - [Criar banco de dados postgres-db-order](#criar-banco-de-dados-postgres-db-order)
    - [Criar arquivo de variável local na pasta arquivos-iniciais/aplicacoes/order-service/.env](#criar-arquivo-de-variável-local-na-pasta-arquivos-iniciaisaplicacoesorder-serviceenv)
    - [Iniciar aplicação](#iniciar-aplicação-1)


## Criar rede para os containers
```bash
docker network create microservices -d bridge
```

## menu-service

### Criar banco de dados postgres-db-menu

```bash
docker container run -d \
--name postgres-db-menu \
--network microservices \
-p 5432:5432 \
-e POSTGRES_USER=menu \
-e POSTGRES_PASSWORD=dbmenu2023 \
-e POSTGRES_DB=menu \
-e POSTGRES_HOST_AUTH_METHOD=trust \
postgres:15
```

### Criar arquivo de variável local na pasta arquivos-iniciais/aplicacoes/menu-service/.env

```bash
echo "POSTGRES_USER=menu" > .env
echo "POSTGRES_PASSWORD=dbmenu2023" >> .env
echo "POSTGRES_SERVER=127.0.0.1" >> .env
echo "POSTGRES_PORT=5432" >> .env
echo "POSTGRES_DB=menu" >> .env
```

### Iniciar aplicação

- Criar ambiente virtual

```bash
python3 -m venv .venv
```

- Instalar dependencias

```bash
source .venv/bin/activate
pip install -U pip 
pip install -r requirements.txt
```

- Iniciar a aplicação

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## order-service

### Criar banco de dados postgres-db-order

```bash
docker container run -d \
--name postgres-db-order \
--network microservices \
-p 5433:5432 \
-e POSTGRES_USER=order \
-e POSTGRES_PASSWORD=dborder2023 \
-e POSTGRES_DB=order \
-e POSTGRES_HOST_AUTH_METHOD=trust \
postgres:15
```

### Criar arquivo de variável local na pasta arquivos-iniciais/aplicacoes/order-service/.env

```bash
echo "POSTGRES_USER=order" > .env
echo "POSTGRES_PASSWORD=dborder2023" >> .env
echo "POSTGRES_SERVER=127.0.0.1" >> .env
echo "POSTGRES_PORT=5433" >> .env
echo "POSTGRES_DB=order" >> .env
echo "MENU_SERVICE_URL=http://127.0.0.1:8000" >> .env
```

### Iniciar aplicação

- Criar ambiente virtual

```bash
python3 -m venv .venv
```

- Instalar dependencias

```bash
source .venv/bin/activate
pip install -U pip 
pip install -r requirements.txt
```

- Iniciar a aplicação

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```
