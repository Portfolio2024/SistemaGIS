from django.shortcuts import render

def index(request):
  title = 'Dashboard'
  return render(request, 'index.html', {'title': title})


  
