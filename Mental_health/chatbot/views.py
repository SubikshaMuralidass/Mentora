from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ChatConversation
import json
import requests
from django.shortcuts import render

def chat_page(request):
    chat_history = ChatConversation.objects.all().order_by('timestamp')
    return render(request, 'chatbot/chat.html', {'chat_history': chat_history})

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")

        # Save user message
        ChatConversation.objects.create(sender="user", message=user_message)

        # Send to Rasa
        rasa_response = requests.post("http://localhost:5005/webhooks/rest/webhook", json={
            "sender": "user",
            "message": user_message
        })

        try:
            bot_reply = rasa_response.json()[0]["text"]
        except (IndexError, KeyError):
            bot_reply = "Sorry, I couldn't understand that."

        # Save bot reply
        ChatConversation.objects.create(sender="bot", message=bot_reply)

        return JsonResponse({"success": True, "bot_response": bot_reply})
    return JsonResponse({"success": False, "error": "Invalid request"})
