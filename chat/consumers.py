import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import User, Profile, Chat, Message
from django.utils import timezone
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['chatId']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print("connected")

    async def disconnect(self, close_code):
        # Leave room group
        print("disconnected")

    async def receive(self, text_data):
        text = text_data
        
        user = await sync_to_async(User.objects.get)(id=self.scope['url_route']['kwargs']['userId'])
        profile = await sync_to_async(Profile.objects.get)(user=user)
        chat = await sync_to_async(Chat.objects.get)(id=self.scope['url_route']['kwargs']['chatId'])

        message = await sync_to_async(Message.objects.create)(writer=profile, date=timezone.now())
        message.text = text.replace('\n', '<br>')
        message.chat = chat
        await sync_to_async(message.save)()

        # Send the received message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'id': message.id,
                    'text': message.text,
                    'writer': {
                        'name': message.writer.name,
                        'pfp': message.writer.pfp.url
                    },
                    'date': message.date.strftime('%Y-%m-%d %H:%M:%S')
                }
            }
        )

    async def chat_message(self, event):
        # Send the received message to the WebSocket
        await self.send(text_data=json.dumps(event['message']))