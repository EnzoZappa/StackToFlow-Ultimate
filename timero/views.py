from django.shortcuts import render
from django.http import JsonResponse

def timer_view(request):
    return render(request, 'timer.html')
# tempo/views.py

def cronometro_view(request):
    return render(request, 'cronometro.html')

# Timer: Variáveis globais para armazenar o tempo restante
timer_start_time = 0
timer_duration = 0

def timer_home(request):
    global timer_duration
    if request.method == "POST":
        # Configura o timer com a duração informada
        timer_duration = int(request.POST['duration'])
        return render(request, 'tempo/home.html', {'timer_time': timer_duration})

    # Caso o método seja GET, apenas exibe o timer
    return render(request, 'tempo/home.html', {'timer_time': timer_duration})

def start_timer(request):
        if request.method == "POST":
            duration = int(request.POST.get('duration', 0))  # Obtenha a duração enviada pelo formulário
            return JsonResponse({'message': 'Timer iniciado!', 'duration': duration})
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def stop_timer(request):
    global timer_start_time
    global timer_duration
    elapsed_time = time.time() - timer_start_time
    remaining_time = timer_duration - int(elapsed_time)
    return JsonResponse({'remaining_time': remaining_time})

def reset_timer(request):
    global timer_start_time
    global timer_duration
    timer_start_time = 0
    timer_duration = 0
    return JsonResponse({'message': 'Timer resetado!'})



