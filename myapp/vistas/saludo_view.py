from django.shortcuts import render

class Saludo_view:

    def saludo(request):
        return render(request, 'saludo.html')