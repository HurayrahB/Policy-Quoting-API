# Policy Quoting API

A small Django REST Framework service for quoting insurance policies, built to practice a Django/DRF stack.

## Stack

Django 5, Django REST Framework, SQLite

## Status

Working CRUD API. Two models (`Applicant`, `Quote`) with a foreign key relationship, `ModelSerializer` and `ModelViewSet` for each, wired through a DRF `DefaultRouter`, plus a custom action that computes a premium from coverage amount, a base rate, and a province factor.

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
cd backend
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Browsable API at `http://localhost:8000/api/`. `seed` wipes existing data and creates 50 applicants with one quote each.
