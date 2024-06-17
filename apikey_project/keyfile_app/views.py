# from django.shortcuts import render, redirect
#
# from .forms import ApiKeyForm
#
#
# def save_api_key(request):
#     if request.method == 'POST':
#         form = ApiKeyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = ApiKeyForm()
#     return render(request, 'keyfile_app/api_key_form.html', {'form': form})
#
#
# def success(request):
#     return render(request, 'keyfile_app/success.html')
#
#
# def handle_uploaded_file(f):
#     # Пример обработки файла
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


# from django.shortcuts import render, redirect
# from .forms import ApiKeyForm
#
#
# def save_api_key(request):
#     if request.method == 'POST':
#         form = ApiKeyForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save()
#             return redirect('success')
#     else:
#         form = ApiKeyForm()
#     return render(request, 'keyfile_app/api_key_form.html', {'form': form})
#
# def success(request):
#     # Получаем последний сохраненный ключ и файл
#     last_entry = ApiKey.objects.latest('id')
#     return render(request, 'keyfile_app/success.html', {'entry': last_entry})


from django.shortcuts import render

from .forms import ApiKeyForm
from .models import ApiKey  # Импортируем модель ApiKey


def save_api_key(request):
    if request.method == 'POST':
        form = ApiKeyForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # Получаем последний сохраненный API ключ и файл
            last_entry = ApiKey.objects.latest('id')
            result = process_key_and_file(last_entry.key, last_entry.file.path)
            return render(request, 'keyfile_app/result.html', {'result': result})
    else:
        form = ApiKeyForm()
    return render(request, 'keyfile_app/api_key_form.html', {'form': form})


from openai import OpenAI


def process_key_and_file(api_key, file):
    client = OpenAI(api_key=api_key)
    with open(file, 'rb') as audio_file:
        try:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                # language="uk"
            )
            return transcription.text
        except Exception as e:
            return str(e)

def success(request):
    # Получаем последний сохраненный ключ и файл
    last_entry = ApiKey.objects.latest('id')
    return render(request, 'keyfile_app/success.html', {'entry': last_entry})
