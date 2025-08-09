from django.shortcuts import render
from django.shortcuts import render
from chatbot.models import ChatConversation
from textblob import TextBlob
from collections import Counter
import datetime
from django.utils.timezone import localtime
from psychotest.models import TestResult
'''
#from .models import TestResult

def dashboard(request):
    results = TestResult.objects.all().order_by('-timestamp')
    latest_result = results.first()
    return render(request, 'insights.html', {
        'latest_result': latest_result,
    })




def dashboard_insights(request):
    chats = ChatConversation.objects.filter(sender="user").order_by('timestamp')

    # Analyze sentiments
    sentiment_counts = Counter()
    mood_data = []
    for chat in chats:
        mood = analyze_sentiment(chat.message)
        sentiment_counts[mood] += 1
        mood_data.append({'message': chat.message, 'sentiment': mood, 'time': chat.timestamp})

    #latest_result = TestResult.objects.filter(user=request.user).order_by('-timestamp').first()

    context = {
        #'latest_result': latest_result,
        'sentiment_counts': dict(sentiment_counts),
        'mood_data': mood_data,
    }
    return render(request, 'dashboard/insights.html', context)

____________
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"



def dashboard_view(request):
    chats = ChatConversation.objects.filter(sender='user').order_by('timestamp')

    sentiments = []
    timestamps = []

    for chat in chats:
        sentiment = get_sentiment(chat.message)  # Assuming you use TextBlob
        sentiments.append(sentiment)
        timestamps.append(localtime(chat.timestamp).strftime('%b %d, %H:%M'))

    sentiment_scores = [1 if s == 'Positive' else (-1 if s == 'Negative' else 0) for s in sentiments]

    return render(request, 'chatbot/insights.html', {
        'sentiments': sentiments,
        'timestamps': timestamps,
        'sentiment_scores': sentiment_scores
    })


'''
from psychotest.models import TestResult

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

def dashboard_insights(request):
    chats = ChatConversation.objects.filter(sender="user").order_by('timestamp')

    # Analyze sentiments
    sentiment_counts = Counter()
    mood_data = []
    for chat in chats:
        mood = analyze_sentiment(chat.message)
        sentiment_counts[mood] += 1
        mood_data.append({'message': chat.message, 'sentiment': mood, 'time': chat.timestamp})

    # ✅ Get latest test result (since no user field is available)
    latest_result = TestResult.objects.order_by('-timestamp').first()

    context = {
        'latest_result': latest_result,
        'sentiment_counts': dict(sentiment_counts),
        'mood_data': mood_data,
    }
    return render(request, 'dashboard/insights.html', context)
