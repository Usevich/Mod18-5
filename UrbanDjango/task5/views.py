from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
users = ["admin", "User2", "User3"]

def sign_up_by_html(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        info = {}

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append('username')
            return render(request, 'fifth_task/registration_page.html',
                          {'message': f'Приветствуем:{username}'})
        return render(request, 'fifth_task/registration_page.html', info)
    return render(request, 'fifth_task/registration_page.html', {'users': users})
def sign_up_by_django(request):
    form = UserRegister()
    info = {'form': form}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print('ОК')
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append('username')
                return render(request, 'fifth_task/registration_page.html',
                              {'message': f'Приветствуем:{username}'})
                info['form'] = form
        return render(request, 'fifth_task/registration_page.html', info)
    return render(request, 'fifth_task/registration_page.html', info)


