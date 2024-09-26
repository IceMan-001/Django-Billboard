from django import forms
from .models import Post


# class PostForm(forms.Form):
#     author = forms.CharField(max_length=50, label='Автор')
#     title = forms.CharField(max_length=200, label='Заголовок')
#     text = forms.CharField(label='Текст объявления', widget=forms.Textarea)

# второй способ создания форм более простой
class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if author:
            self.fields['author'].initial = author
            self.fields['author'].disabled = True

        self.fields['author'].widget.attrs['placeholder'] = 'Укажите автора'
        self.fields['title'].widget.attrs['placeholder'] = 'Укажите заголовок'
        self.fields['text'].widget.attrs['placeholder'] = 'Текст объявления'
        self.fields['image'].widget.attrs['placeholder'] = 'Фотография'
        self.fields['url_adders'].widget.attrs['placeholder'] = 'Укажите email'

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'image', 'url_adders']  # так правильнее всего
        # второй способ не надо так делать
        # fields = '__all__'
        # exclude = ['created_at'] или так

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['author'].widget.attrs['placeholder'] = 'Укажите автора'
    #     self.fields['title'].widget.attrs['placeholder'] = 'Укажите заголовок'
    #     self.fields['text'].widget.attrs['placeholder'] = 'Текст объявления'
    #     self.fields['image'].widget.attrs['placeholder'] = 'Фотография'
    #     self.fields['url_adders'].widget.attrs['placeholder'] = 'Укажите email'

# class DeleteNewForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = []
