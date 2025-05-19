import os

from dotenv import load_dotenv

load_dotenv()


class Env:
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", 8000))

    db_user: str = os.getenv("DB_USER", "root")
    db_password: str = os.getenv("DB_PASSWORD", "rootpassword")
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: str = os.getenv("DB_PORT", "3306")
    db_name: str = os.getenv("DB_NAME", "e-commerce-api")

    db_url: str = (
        f"mysql+aiomysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    db_url_alembic: str = (
        f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )


env = Env()
