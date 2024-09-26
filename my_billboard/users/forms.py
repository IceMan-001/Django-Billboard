from django import forms
from django.contrib.auth import get_user_model

# Получение текущей модели пользователя
User = get_user_model()


# Создание формы регистрации пользователя
class UserRegistrationForm(forms.ModelForm):
    # Создание дополнительного поля пароля для повторного ввода при регистрации
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)  # widget=forms.PasswordInput - скрытый ввод

    # def __init__(self, *args, **kwargs):
    #     author = kwargs.pop('author', None)
    #     super(UserRegistrationForm, self).__init__(*args, **kwargs)
    #     if author:
    #         self.fields['author'].initial = author
    #         self.fields['author'].disabled = True

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')  # Если пароли не совпадают - генерируем исключение
        return cleaned_data['password2']

    class Meta:
        model = User  # Установка связи между model и User
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'phone', 'city')


class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
    new_password_1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    new_password_2 = forms.CharField(label="Повторите новый пароль", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password_1 = cleaned_data['new_password_1']
        new_password_2 = cleaned_data['new_password_2']
        old_password = cleaned_data['old_password']

        if new_password_1 and new_password_2 and new_password_1 != new_password_2:
            raise forms.ValidationError('Пароли не совпадают')

        if new_password_1 and new_password_2 and new_password_1 == new_password_2 and new_password_1 == old_password:
            raise forms.ValidationError("Пароли совпадают с текущим")

        return cleaned_data
