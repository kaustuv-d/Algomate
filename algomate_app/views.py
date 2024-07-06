from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}
history = []

def generate_response(request):
    if request.method == "POST":
        prompt = request.POST.get('prompt')
        history.append(prompt)
        final_prompt = "\n".join(history)
        data = {
            "model": "Algomate",
            "prompt": final_prompt,
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            actual_response = response_data['response']
            return JsonResponse({'response': actual_response})
        else:
            return JsonResponse({'error': response.text}, status=500)
    return render(request, 'index.html')
