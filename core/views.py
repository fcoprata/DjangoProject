from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(requests,nome,idade):
    return HttpResponse(f'<h1>Hello {nome}  de {idade}</h1>')