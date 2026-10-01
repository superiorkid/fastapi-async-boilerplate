# FastAPI Async Boilerplate

A minimal, ready-to-use template for FastAPI projects featuring asynchronous database support.

## Tech Stack
* FastAPI
* SQLAlchemy (Async)
* Alembic (Async)

## Quick Start

1. Install dependencies:
    ```
   pip install -r requirements.txt
   ```

2. Update your database URL (make sure to use an async driver like `asyncpg` or `aiosqlite`):

    ```
   # Example in alembic.ini or .env: 
   # postgresql+asyncpg://user:pass@localhost/db
   ```

3. Run migrations to set up the database:
 
   ```alembic upgrade head```

4. Start the server:

   ```uv run fastapi dev```

## Making Database Changes
When you update your models, create a new migration:

```
alembic revision --autogenerate -m "added new table"
alembic upgrade head
```