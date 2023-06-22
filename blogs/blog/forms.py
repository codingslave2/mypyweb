from django import forms
from blog.models import Post

# Post 폼 생성
class PostForm(forms.ModelForm):
    class Meta:
        model = Post # Post 객체 생성
        fields = ('title', 'content', 'photo')
        