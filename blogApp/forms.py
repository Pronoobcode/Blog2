from django.forms import ModelForm
from .models import Post, User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2', 'bio', 'avatar')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['created_by', 'participants']
