# README.md

## Deploy local

Start postgres
```bash
docker compose -f docker-compose-db-dev-local.yaml up -d
```

Start microservice
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```









