import json
import gunicorn

from datetime import datetime



def app(environ, start_response):
    """
        environ - окружение, содержит метод, query_string, заголовки запроса
        start_response - ф-я, которая передает код ответа и заголовки ответа
    """
    print(environ.get('RAW_URI'))
    data = {'time': str(datetime.now().time()),
            'url': environ.get('RAW_URI')}
    response = json.dumps(data).encode()
    start_response('200 OK', [('Content_type', 'application/json'),
                              ('Content_Length', str(len(response)))])
    # Возврат тела ответа
    return iter([response])