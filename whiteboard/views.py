from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # O usuário precisa estar logado para acessar
def whiteboard_view(request):
    return render(request, 'whiteboard.html')
