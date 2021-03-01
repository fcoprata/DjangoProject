from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(requests,nome,idade):
    return HttpResponse(f'<h1>Hello {nome}  de {idade}</h1>')
def soma(requests,n1,n2):
    return HttpResponse(f'soma de {n1}+{n2}={n1+n2}')
def sub(requests,n1,n2):
    return HttpResponse(f'subtração de {n1}-{n2}={n1-n2}')
def mult(requests,n1,n2):
    return HttpResponse(f'multiplicação de {n1}x{n2}={n1*n2}')
def div(requests,n1,n2):
    return HttpResponse(f'divisão de {n1}/{n2}={n1/n2}')
