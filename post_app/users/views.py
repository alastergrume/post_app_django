from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.


def sign_in(request):
    """
    Функция аутентификации пользователей
    """

    # Вывод формы представления через шаблон
    if request.method == 'GET':
        # Сохраняем поля формы в переменную, создаем объект класса
        form = LoginForm()
        # отправляем представление в шаблон
        return render(request, 'users/login.html', {'forms': form})

    # Проверка пользователя, после нажатия кнопки 'Login'. Перехватываем POST из формы
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Привет {username.title()}. Добро пожаловать!')
                # Если пользователь такой есть, то мы перемещаем его на страницу с постами
                # Пока нет логики регистрации пользователей, работает только superuser
                return redirect('post-create')

        # Если такого пользователя нет, то перенаправляется заново на ту же самую форму
        messages.error(request, 'invalid username/password')
        return render(request, 'users/login.html', {'forms': form})


def sing_out(request):
    """
    Функция для выхода из аккаунта
    :return: Возврат на страницу login
    """
    logout(request)
    messages.success(request, "Вы вышли из аккаунта")
    return redirect('login')



