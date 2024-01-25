from django.urls import path
from .views import get_user_data

urlpatterns = [
    # Rate Limiting with Django Ratelimit
    path('user-data/', get_user_data, name='get_user_data'),

    # # API Key Authentication with Django REST Framework
    # path('api/user-data/', get_user_data, name='api_get_user_data'),

    # # Token Bucket Algorithm with Django Ratelimit
    # path('token-bucket/user-data/', get_user_data, name='token_bucket_get_user_data'),

    # # Quotas and Monitoring with Django Ratelimit
    # path('quota/user-data/', get_user_data, name='quota_get_user_data'),
]
