from django.shortcuts import render

def infraestructura(request):
  title = 'Infraestructura Eléctrica'
  return render(request, 'infraestructura.html', {'title': title})
