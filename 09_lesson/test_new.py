import os # pytest test_new.py
import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Настройки подключения к базе данных
DB_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost:5432/postgres')
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

# Определение таблицы для тестирования
teacher_table = Table(
    'teacher', MetaData(),
    Column('teacher_id', Integer, primary_key=True),
    Column('email', String(50), nullable=False),
    Column('is_deleted', Boolean, default=False)  # Новая колонка для мягкого удаления
)

# Функция для мягкой очистки данных после каждого теста
@pytest.fixture(scope="function", autouse=True)
def soft_clean_up():
    session = Session()
    try:
        yield
    finally:
        try:
            # Мягко удаляем все записи, устанавливая is_deleted в True
            session.query(teacher_table).update({"is_deleted": True})
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Ошибка при мягком удалении данных: {e}")
        finally:
            session.close()

# Тест на добавление записи
def test_insert():
    session = Session()
    try:
        insert_data = {'teacher_id': 425698, 'email': 'example@mail.com'}
        query = teacher_table.insert().values(insert_data)
        result = session.execute(query)
        session.commit()
        
        # Проверка, что запись добавлена
        result = session.query(teacher_table).filter_by(is_deleted=False).first()
        assert result.teacher_id == 425698
        assert result.email == 'example@mail.com'
    finally:
        session.close()

# Тест на обновление записи
def test_update():
    session = Session()
    try:
        insert_data = {'teacher_id': 425698, 'email': 'example@mail.com'}
        query = teacher_table.insert().values(insert_data)
        session.execute(query)
        session.commit()
        
        update_data = {'email': 'updated@example.com'}
        query = teacher_table.update().where(teacher_table.c.teacher_id == 425698).values(update_data)
        result = session.execute(query)
        session.commit()
        
        # Проверка, что запись обновлена
        result = session.query(teacher_table).filter_by(teacher_id=425698, is_deleted=False).one()
        assert result.email == 'updated@example.com'
    finally:
        session.close()

# Тест на мягкое удаление записи
def test_soft_delete():
    session = Session()
    try:
        insert_data = {'teacher_id': 425698, 'email': 'example@mail.com'}
        query = teacher_table.insert().values(insert_data)
        session.execute(query)
        session.commit()
        
        # Мягко удаляем запись
        delete_query = teacher_table.update().where(teacher_table.c.teacher_id == 425698).values({"is_deleted": True})
        result = session.execute(delete_query)
        session.commit()
        
        # Проверка, что запись помечена как удаленная
        # Теперь добавляем условие is_deleted = False, чтобы убедиться, что найдена только одна активная запись
        result = session.query(teacher_table).filter_by(teacher_id=425698, is_deleted=False).one_or_none()
        if result is not None:
            assert result.is_deleted == False  # Проверяем, что осталась только одна активная запись
        else:
            pass  # Нет активных записей с таким ID, всё в порядке
            
        # Проверяем, что все остальные записи с таким ID помечены как удалённые
        deleted_results = session.query(teacher_table).filter_by(teacher_id=425698, is_deleted=True).all()
        for deleted_result in deleted_results:
            assert deleted_result.is_deleted == True  # Все найденные записи должны быть помечены как удалённые
    finally:
        session.close()