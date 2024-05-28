import base64
import hashlib

from django.shortcuts import render
from django.http import JsonResponse

from hashgen.models import get_next_num

# Create your views here.
def next_num(request):
    # получим уникальное число из базы данных
    num = get_next_num()
    # Преобразуем его в строку и кодируем в байты
    orig_id = str(num).encode('utf-8')  
    # Используем SHA-256 для хэширования
    hash_object = hashlib.sha256(orig_id)
    # Получаем хэш и кодируем его в base64
    hash_digest = hash_object.digest()
    short_url_byte = base64.urlsafe_b64encode(hash_digest)[:13]   
    short_url = short_url_byte.decode('utf-8')

    return JsonResponse({'hash': short_url})


