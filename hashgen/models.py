from django.db import models, connection

# вызвать один раз чтобы создать последовательность в базе данных
def create_sequence():
    with connection.cursor() as cursor:
        cursor.execute("CREATE SEQUENCE IF NOT EXISTS num_for_gen START WITH 1 INCREMENT BY 1")

# получает уникальное число
def get_next_num():
    with connection.cursor() as cursor:
        cursor.execute("SELECT nextval('num_for_gen')")
        result = cursor.fetchone()
        return result[0]