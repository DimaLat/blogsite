from django import forms

from .models import Post

# class PostForm(forms.Form):
#     title = form.CharField()
#     description = forms.CharField()
#     image = forms.ImageField()
#     slug = forms.CharField()



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','image','slug']
