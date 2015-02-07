import json
from django.http import HttpResponse


def json_success(request, data):
    return json_response({
        'success': 1,
        'data': data,
    })


def json_fail(request, data=None):
    return json_response({
        'success': 0,
        'data': data,
    })


def json_response(response_data):
    return HttpResponse(json.dumps(response_data), content_type='application/json')

