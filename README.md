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

### Generate Migrations
To create new database migrations:
```bash
alembic revision --autogenerate -m "message"
```

### Apply Migrations
To apply pending migrations:
```bash
alembic upgrade head
```