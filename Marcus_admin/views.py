from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from study import update_problems_dict
from reply import reply_output
from helper import sanitizer
from sql import con


# Create your views here.

@api_view(['POST'])
def study(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)

        sanitized_text = sanitizer(request_data['user_text'])
        con.ping()

        update_problems_dict(sanitized_text, request_data['user_tags'], 0)

        return JsonResponse('OK', status=status.HTTP_200_OK, safe=False)


@api_view(['POST'])
def reply(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)

        sanitized_input_text = sanitizer(request_data['user_text'])
        con.ping()

        output_list = reply_output(sanitized_input_text)

        return JsonResponse(output_list, status=status.HTTP_200_OK, safe=False)
