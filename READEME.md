# Django API Security and Optimization

This Django project demonstrates strategies for securing and optimizing your API, including rate limiting, API key authentication, token bucket algorithm, and usage quotas.

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/Kashif1Naqvi/django-api-security.git
  ```

create envoirement variable on Linux/MAC

```python -m venv env_name```

Active the env variable
``` source  env_name/bin/activate```

Install the required packages:

```pip install -r requirements.txt```

Run migrations:

```python manage.py migrate```


```Usage```

1. Rate Limiting with Django Ratelimit
Access user data while enforcing rate limits:

```curl http://localhost:8000/user-data/```

2.  API Key Authentication with Django REST Framework
    Access user data with API key authentication:

3.  Token Bucket Algorithm with Django Ratelimit
    Access user data with token bucket rate limiting:

4.  Quotas and Monitoring with Django Ratelimit
    Access user data with usage quotas:


```Configuration```

Adjust rate limits, API keys, and other settings in the project's `settings.py` file. Customize these features according to your application's requirements.

```Contributing```

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and improvements are highly appreciated!




