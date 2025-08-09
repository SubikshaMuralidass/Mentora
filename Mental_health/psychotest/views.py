# views.py

from django.shortcuts import render, redirect
from .models import Question, TestResult
from textblob import TextBlob

def take_test(request):
    questions = Question.objects.all()
    return render(request, 'psychotest/take_test.html', {'questions': questions})

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def submit_test(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith("q"):
                question_id = int(key[1:])
                question = Question.objects.get(id=question_id)

                # Get selected option's actual text
                if value == 'A':
                    selected_text = question.option_a
                elif value == 'B':
                    selected_text = question.option_b
                elif value == 'C':
                    selected_text = question.option_c
                elif value == 'D':
                    selected_text = question.option_d
                else:
                    selected_text = ""

                sentiment = get_sentiment(selected_text)

                # Save to DB
                TestResult.objects.create(
                    question=question,
                    selected_option_text=selected_text,
                    sentiment=sentiment
                )
        return redirect('dashboard_insights')  # Or some success page
    
