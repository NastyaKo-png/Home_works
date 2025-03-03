import os
from sqlalchemy import create_engine, MetaData, Table, Column, Boolean

# Настройки подключения к базе данных
DB_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost:5432/postgres')
engine = create_engine(DB_URL)

# Метаданные для работы с таблицей
metadata = MetaData()

# Определение таблицы users
users_table = Table(
    'users', metadata,
    autoload_with=engine  # Загружаем существующую таблицу из базы данных
)

# Определение новой колонки is_deleted
is_deleted_column = Column('is_deleted', Boolean, default=False)

# Добавляем новую колонку в таблицу
with engine.connect() as conn:
    # Получаем существующую таблицу
    users_table = Table('users', metadata, autoload_with=conn)
    
    # Добавляем новую колонку
    with conn.begin():
        users_table.append_column(is_deleted_column)

print("Колонка 'is_deleted' успешно добавлена!")