from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .task import send_email_task

@api_view(['POST'])
def send_email_view(request):
    subject = request.data.get('subject')
    message = request.data.get('message')
    recipient = request.data.get('recipient')

    if not subject or not message or not recipient:
        return JsonResponse({'status': 'error', 'message': 'Missing fields'}, status=400)

    try:
        send_email_task.apply_async((subject, message, [recipient]), countdown=30)  
        print('hellll')
    except Exception as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse({'status': 'success', 'message': 'Email is being sent!'})
