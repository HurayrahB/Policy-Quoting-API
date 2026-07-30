# Policy Quoting API

A small Django REST Framework service for quoting insurance policies, built to practice a Django/Postgres/Redis stack

## Stack

Django 5, Django REST Framework, PostgreSQL 16, Redis 7, Docker Compose, GitHub Actions.

## Status

Working CRUD API for applicants and quotes, served from Postgres in Docker Compose. Quote pricing runs through a Redis cache with a 5 minute TTL. The list endpoint uses `select_related` on the applicant foreign key, with a `django_assert_num_queries` test pinning the query count. Tests run on every push via GitHub Actions.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET, POST | `/api/applicants/` | List and create applicants |
| GET, PUT, PATCH, DELETE | `/api/applicants/<id>/` | Retrieve and modify an applicant |
| GET, POST | `/api/quotes/` | List and create quotes |
| GET, PUT, PATCH, DELETE | `/api/quotes/<id>/` | Retrieve and modify a quote |
| POST | `/api/quotes/<id>/price/` | Compute and store the premium |

## Running it

```bash
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py seed
```

Browsable API at `http://localhost:8000/api/`. `seed` wipes existing data and creates 50 applicants with one quote each.

## Tests

```bash
docker compose exec web pytest -q
```
