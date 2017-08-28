from django.shortcuts import render


def home_view(request):
    if request.user.is_authenticated():
        context = {
            'Имя': 'Автор1'
        }
    else:
        context = {
            'Имя': 'Автор2'
        }
    return render(request, 'home.html', context)