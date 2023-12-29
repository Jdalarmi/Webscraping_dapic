from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .scraping import scraping

@api_view(['GET'])
def api(request):
    if request.method == 'GET':
        print('teste')
        dados = scraping()
        return Response(dados)
