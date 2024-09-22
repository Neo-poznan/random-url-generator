import redis
import asyncio

from django.http import JsonResponse

from .url_generating import generate
from url_generator.settings import REDIS_CHECK_TIMEOUT, REDIS_HOST, REDIS_PORT

# Create your views here.
async def generate_url_view(request):
    '''
    Если в кэше есть уже сгенерированные хэши, то берем один из них,
    а если они закончились и сервер не сгенерировал их, то ждем пока
    они сгенерируются и повторяем попытку
    '''
    client = redis.Redis(REDIS_HOST, REDIS_PORT)
    if client.llen('urls') > 0:
        url_hash = client.rpop('urls').decode()
    else:
        url_hash = await generate()

    return JsonResponse({'hash': url_hash})

