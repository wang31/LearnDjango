from django.shortcuts import render
from django.shortcuts import render_to_response
from models import posts

# Create your views here.

def home(request):
    post = posts.objects.all()[:10]
    return render_to_response('index.html', {'posts' : post})
