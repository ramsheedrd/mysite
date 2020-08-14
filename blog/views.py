from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Authors
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('login', permanent=False)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:     
        return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index', permanent=False)