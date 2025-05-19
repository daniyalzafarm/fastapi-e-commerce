# E-commerce API

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Database Migrations

### 1. Generate Migrations
To create new database migrations:
```bash
alembic revision --autogenerate -m "message"
```

### 2. Apply Migrations
To apply pending migrations:
```bash
alembic upgrade head
```

## Database Seeding

Note: Make sure to run the migrations first before seeding the database.

### Running Seeders

There are two ways to run the database seeders:

1. Using the `-m` flag (recommended):
```bash
python -m db.seed_db
```

2. Using PYTHONPATH:
```bash
PYTHONPATH=$PYTHONPATH:. python db/seed_db.py
```

Both methods will work the same way. The `-m` flag is recommended as it's more portable and handles Python module resolution automatically.

## Running the Application

To start the FastAPI application with hot-reload enabled:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload when code changes are detected, which is useful during development.

The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.
