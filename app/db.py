import os
from sqlalchemy import create_engine

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:" \
               f"{os.getenv('POSTGRES_PASSWORD')}@" \
               f"{os.getenv('POSTGRES_HOST','db')}:" \
               f"{os.getenv('POSTGRES_PORT','5432')}/" \
               f"{os.getenv('POSTGRES_DB')}"

engine = create_engine(DATABASE_URL)