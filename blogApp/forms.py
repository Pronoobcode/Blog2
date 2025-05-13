from django.forms import ModelForm
from .models import Post, User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('fullname', 'username', 'email', 'bio', 'avatar', 'password1', 'password2')

class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('fullname', 'username', 'email', 'bio', 'avatar')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('created_by', 'participants')
