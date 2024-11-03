"""
ASGI config for devsearch project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
# Below lines ar done in get_asgi_application() command so If we use get_asgi_application below(inside the application object) then we can use this command to get the app set up so that daphne asgi run command don't give us any error.
# import django
# django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')
# Implementing get_asgi_application before any other application import ensures that the asgi application is built first. So the daphne -b 0.0.0.0 -p 8000 devsearch.asgi:application command works. 
django_asgi_app=get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing


application = ProtocolTypeRouter({
    "http":django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
