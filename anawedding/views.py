from django.shortcuts import render
from . import responses

def get_response(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = responses.get_responses(message)
        if response is None:
            response = "I'm sorry, I didn't understand your message. Could you please rephrase it?"
        
        return render(request, 'anawedding/chatbot.html', context={'response': response})
    else:
        return render(request, 'anawedding/index.html')

