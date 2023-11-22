# Criando manifestos menu

- [Criando manifestos menu](#criando-manifestos-menu)
  - [Criando arquivos do postgesql](#criando-arquivos-do-postgesql)
    - [Criar arquivo de deployment](#criar-arquivo-de-deployment)
    - [Editar o arquivo de deployment e adicionar variaveis](#editar-o-arquivo-de-deployment-e-adicionar-variaveis)
    - [Fazer deploy](#fazer-deploy)
    - [Criar arquivo de service](#criar-arquivo-de-service)
    - [Fazer deploy do service](#fazer-deploy-do-service)
  - [Criando arquivos da aplicação](#criando-arquivos-da-aplicação)
    - [Criar arquivo de deployment](#criar-arquivo-de-deployment-1)
    - [Editar o arquivo de deployment e adicionar variaveis](#editar-o-arquivo-de-deployment-e-adicionar-variaveis-1)
    - [Fazer deploy](#fazer-deploy-1)
    - [Criar arquivo de service](#criar-arquivo-de-service-1)
    - [Fazer deploy do service](#fazer-deploy-do-service-1)


## Criando arquivos do postgesql

> Atenção o postgresql em containers é apenas para estudos e desenvolvimento

### Criar arquivo de deployment

```bash
kubectl create deployment db-postgresql-menu --image postgres:15 --dry-run=client -o yaml > deployment-db-menu.yaml
```

### Editar o arquivo de deployment e adicionar variaveis

```yaml
    spec:
      containers:
      - image: postgresq:15
        name: postgresq
        resources: {}
        env:
          - name: POSTGRES_USER
            value: "menu"
          - name: POSTGRES_PASSWORD
            value: "dbmenu2023"
          - name: POSTGRES_DB
            value: "menu"
          - name: POSTGRES_HOST_AUTH_METHOD
            value: "trust"          
```

### Fazer deploy

```bash
kubectl apply -f deployment-db-menu.yaml
```

### Criar arquivo de service

```bash
kubectl expose deployment db-postgresql-menu --port 5432 --dry-run=client -o yaml > service-db-menu.yaml
```

### Fazer deploy do service

```bash
kubectl apply -f service-db-menu.yaml
```
 

## Criando arquivos da aplicação

### Criar arquivo de deployment

```bash
kubectl create deployment menu --image robertsilvatech/menu-service-playground --dry-run=client -o yaml > deployment-menu.yaml
```

### Editar o arquivo de deployment e adicionar variaveis

```yaml
    spec:
      containers:
      - image: robertsilvatech/menu-service-playground
        name: menu-service-playground
        resources: {}
        env:
          - name: DATABASE_HOST
            value: "postgres-menu-db"
          - name: DATABASE_USERNAME
            value: "menu"
          - name: DATABASE_PASSWORD
            value: "dbmenu2023"
          - name: DATABASE_NAME
            value: "menu"
```

### Fazer deploy

```bash
kubectl apply -f deployment-menu.yaml
```

### Criar arquivo de service

```bash
kubectl expose deployment menu --port 8000 --dry-run=client -o yaml > service-menu.yaml
```

### Fazer deploy do service

```bash
kubectl apply -f service-menu.yaml
```