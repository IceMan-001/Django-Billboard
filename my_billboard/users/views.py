from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from my_billboard.settings import LOGIN_REDIRECT_URL
from .forms import UserRegistrationForm, CustomPasswordChangeForm
from .models import CustomUser

User = get_user_model()


def register(request):
    # если нажали кнопку регистрации (метод POST)
    if request.method == 'POST':
        # создаем объект с данными из запроса
        user_form = UserRegistrationForm(request.POST)
        # Валидация формы (правильность введенных данных)
        if user_form.is_valid():
            # Создание объекта с полями формы (без сохранения в БД)
            new_user = user_form.save(commit=False)
            # Хеширование пароля пользователя
            new_user.set_password(user_form.cleaned_data['password'])  # Хеширование пароля
            # Сохранение пользователя в БД
            new_user.save()  # по умолчанию commit=True
            context = {'title': 'Успешная регистрация', 'new_user': new_user}
            return render(request, template_name='users/register_done.html', context=context)

    # Если метод GET - отрисовка страницы регистрации
    user_form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'register_form': user_form
    }
    return render(request, template_name='users/register.html', context=context)


def log_in(request):
    # Создание формы аутентификации
    form = AuthenticationForm(request, request.POST)
    # Проверка формы
    if form.is_valid():
        # Получения логина и пароля из формы
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # Аунтификация пользователя (проверка наличия пользователя и пароля)
        user = authenticate(username=username, password=password)
        if user is not None:
            # Авторизация пользователя (проверка прав доступа)
            login(request, user)
            # Получение дальнейшего маршрута после авторизации (next - путь, откуда пришел пользователь)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)


@login_required
def log_out(request):
    logout(request)
    return redirect('board:index')


@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        raise PermissionDenied()

    context = {
        'user': user,
        'title': 'Информация о профиле'
    }

    return render(request, template_name='users/profile.html', context=context)


@login_required
def user_edit(request, pk):
    post = get_object_or_404(CustomUser, pk=pk)  # получить объект по ключу
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return user_detail(request, pk=pk)

    else:
        form = UserRegistrationForm(instance=post)
    context = {
            'form': form,
            'title': 'Редактировать данные пользователя'
        }
    return render(request, template_name='users/user_edit.html', context=context)


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.POST)

        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password_1']

            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('board:index')

            else:
                form.add_error('old_password', 'Старый пароль неверный')
                return redirect('users:change_password')

        return redirect('users:change_password')

    else:
        form = CustomPasswordChangeForm()
        context = {'title': 'Сменить пароль', 'form': form}
        return render(request, template_name='users/change_password.html', context=context)

