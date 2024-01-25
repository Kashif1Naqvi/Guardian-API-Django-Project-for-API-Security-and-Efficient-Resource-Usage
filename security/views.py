from django.shortcuts import render
from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from django.views.decorators.http import require_GET


#Rate Limiting with ratelimit liberary
"""
Request block after 2 request per minit
key base on User to do that
"""
@ratelimit(key='user', rate='2/m', block=True)
@require_GET
def get_user_data(request):
    user_id = {'user_id': 10, 'username': "kashif"}
    return JsonResponse(user_id)