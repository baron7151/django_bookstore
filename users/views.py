from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm #  参照するフォームのクラスを指定
    success_url = reverse_lazy('login') #  送信されるとsuccess_urlにリダイレクトされる
    template_name = 'signup.html' #  表示するテンプレートのファイル名
