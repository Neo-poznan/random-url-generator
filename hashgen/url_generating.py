import redis
import time
import hashlib
import base64

from .models import get_next_num
from url_generator.settings import REDIS_HOST, REDIS_PORT, READY_URLS_LIST_LIMIT, REDIS_CHECK_TIMEOUT   

def url_generation_loop() -> None:
    '''
    Цикл генерации уникальных хэшей. Он проверяет наличие хэшей в в кэше 
    и если их меньше положенного, то запускается цикл пополнения кэша
    '''
    client = redis.Redis(REDIS_HOST, REDIS_PORT)
    while True:
        if client.llen('urls') < READY_URLS_LIST_LIMIT:
            list_filing_loop()
        time.sleep(REDIS_CHECK_TIMEOUT)
        
def list_filing_loop() -> None:
    '''
    Цикл пополнения кэша. Запускается при нехватке хэшей в кэше.
    Вызывает функцию генерации хэша и добавляет его в кэш пока список
    не заполнится по указанную отметку    
    '''
    client = redis.Redis(REDIS_HOST, REDIS_PORT)
    while client.llen('urls') < READY_URLS_LIST_LIMIT:
        url_hash: str = generate()
        client.rpush('urls', url_hash)

def generate() -> str:
    '''
    Получает уникальное число из базы данных, преобразует его в строку,
    хэширует его, кодирует в безопасный для урла байтовый формат, возвращает его
    '''
    num: int = get_next_num()
    orig_id = str(num).encode('utf-8')  
    hash_object = hashlib.sha256(orig_id)
    hash_digest = hash_object.digest()
    short_url_byte = base64.urlsafe_b64encode(hash_digest)[:13]   
    short_url = short_url_byte.decode('utf-8')
    return short_url

