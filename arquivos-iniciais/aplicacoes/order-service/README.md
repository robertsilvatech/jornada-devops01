# README.md

## Deploy local

Start postgres
```bash
docker compose -f docker-compose-db-dev-local.yaml up -d
```

Create .env with variables

```bash
DATABASE_URL=postgresql://fastapi:fastapi@127.0.0.1/orders
MENU_SERVICE_URL=http://127.0.0.1:8001
```

Start microservice
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## FastAPI - Swagger UI

- http://127.0.0.1:8000/docs#

