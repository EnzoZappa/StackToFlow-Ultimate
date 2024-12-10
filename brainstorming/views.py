from django.shortcuts import render
from django.http import JsonResponse
from .models import Brainstorm
from .utils import optimize_prompt, run_final

def brainstorming_view(request):
    if request.method == "POST":
        user_prompt = request.POST.get("prompt", "")
        if not user_prompt:
            return JsonResponse({"error": "Prompt is required"}, status=400)

        # Generate optimized prompt
        optimized_prompt = optimize_prompt(user_prompt)

        # Get final brainstorming output
        final_output = run_final(optimized_prompt)

        return JsonResponse({
            "optimized_prompt": optimized_prompt,
            "final_output": final_output
        })
    return JsonResponse({"error": "Invalid request method"}, status=405)