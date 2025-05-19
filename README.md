# E-commerce API

## Table of Contents
- [Setup](#setup)
- [Database Migrations](#database-migrations)
  - [Generate Migrations](#1-generate-migrations)
  - [Apply Migrations](#2-apply-migrations)
- [Database Seeding](#database-seeding)
  - [Running Seeders](#running-seeders)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
  - [Authentication & Users](#authentication--users)
  - [Products](#products)
  - [Inventory](#inventory)
  - [Orders](#orders)
  - [Warehouses](#warehouses)

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


## Project Structure

```
fastapi-e-commerce/
├── alembic/             # Database migration files
├── core/                # Core application configuration
│   └── config.py         # Application settings and configuration
├── db/                  # Database related files
│   └── seed_db.py       # Database seeding script
├── src/                 # Source code
│   ├── auth/            # Authentication module
│   ├── inventory/       # Inventory management module
│   ├── order/           # Order management module
│   ├── product/         # Product management module
│   ├── warehouse/       # Warehouse management module
│   ├── models.py        # Database models
│   └── routers.py       # API route definitions
├── tests/               # Test files
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
├── alembic.ini          # Alembic configuration
├── pyproject.toml       # Project metadata and build system configuration
├── .flake8               # Flake8 configuration
└── lint.sh              # Linting script
```

## Endpoints

### Authentication & Users
- `GET /roles` - List all available roles
- `POST /users` - Create a new user
- `GET /users/{user_id}` - Get user details by ID

### Products
- `GET /products` - List all products (with pagination)
- `GET /products/{product_id}` - Get detailed product information
- `POST /products` - Create a new product
- `PUT /products/{product_id}` - Update product information
- `DELETE /products/{product_id}` - Delete a product
- `GET /products/categories` - List all product categories
- `POST /products/categories` - Create a new product category

### Inventory
- `GET /inventory` - List current inventory status of all products
- `GET /inventory/{product_id}` - Get inventory for a specific product
- `PUT /inventory/{product_id}` - Update inventory for a product
- `GET /inventory/history/{product_id}` - Get inventory change history for a product

### Orders
- `GET /orders/user/{user_id}` - List orders for a specific user (with filtering options)
- `GET /orders/{order_id}` - Get detailed order information
- `POST /orders` - Create a new order
- `GET /orders/analytics` - Get daily order analytics between two dates (here we can get daily, weekly, monthly, and yearly)
- `GET /orders/analytics/by-product` - Get product-wise order analytics
- `GET /orders/analytics/by-category` - Get category-wise order analytics

### Warehouses
- `GET /warehouses` - List all warehouses (with pagination)
- `GET /warehouses/{warehouse_id}` - Get warehouse details
- `POST /warehouses` - Create a new warehouse
