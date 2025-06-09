import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

@csrf_exempt
def chat_page(request):
    return render(request, 'index.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message", "")

        try:
            response = model.generate_content(user_input)
            reply = response.text
        except Exception as e:
            reply = f"⚠️ Model error: {str(e)}"

        return JsonResponse({"reply": reply})
    
    return JsonResponse({"reply": "Invalid request method."})
