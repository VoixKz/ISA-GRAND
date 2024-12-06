from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .integrationai import getQuestions, processPost, generatePdfCV
from .cv_create import fill_pdf
from authApp.models import CustomUser
import os
from django.conf import settings
from datetime import datetime

def cv_form(request):
    context = dict()
    context['questions'] = getQuestions()
    return render(request, 'cv/cv_form.html', context)

def process_interest_form(request):
    if request.method == "POST":
        data_ready = processPost(request.POST)
        
        # Получение данных пользователя из базы данных
        user = CustomUser.objects.get(email=request.user.email)
        user_data = {
            "text_name": user.personaluser.full_name,
            "text_email": user.email,
            "text_phone": user.personaluser.phone_number,
            "textarea_edu": user.personaluser.education,
            "textarea_exp": user.personaluser.experience,
        }
        
        # Генерация текста для CV с помощью AI
        cv_text = generatePdfCV(data_ready)
        
        # Заполнение PDF шаблона
        pdf_data = {
            **user_data,
            "textarea_profile": cv_text,
        }
        
        # Генерация имени файла
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_pdf_filename = f"CV-{user.email}-{current_time}.pdf"
        output_pdf_path = os.path.join(settings.MEDIA_ROOT, output_pdf_filename)
        
        input_pdf_path = os.path.join(settings.BASE_DIR, 'cv', 'static', 'cv', 'media', 'cv_form.pdf')
        fill_pdf(input_pdf_path, output_pdf_path, pdf_data)
        
        # Возвращение PDF файла в ответе
        return FileResponse(open(output_pdf_path, 'rb'), content_type='application/pdf', filename=output_pdf_filename)
    
    return HttpResponse("403 Invalid", content_type="text/plain")