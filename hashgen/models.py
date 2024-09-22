from django.db import connection
from asgiref.sync import sync_to_async

# вызвать один раз чтобы создать последовательность в базе данных
def create_sequence() -> None:
    with connection.cursor() as cursor:
        cursor.execute("CREATE SEQUENCE IF NOT EXISTS num_for_gen START WITH 1 INCREMENT BY 1")

# получает уникальное число
@sync_to_async
def get_next_num() -> int:
    with connection.cursor() as cursor:
        cursor.execute("SELECT nextval('num_for_gen')")
        result = cursor.fetchone()
        return result[0]

