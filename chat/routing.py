from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/monkord/(?P<chatId>[^/]+)/(?P<userId>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]