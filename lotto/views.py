from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello, world!</h1>')
def index(request):
    sample_str = 'This is python variable'
    lottos = GuessNumbers.objects.all()
    return render(request,'lotto/default.html',{'pass_str':sample_str,'lottos':lottos})
def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            # urls.py의 name='index'
            return redirect('index')
    else:
        form = PostForm
        return render(request, 'lotto/form.html',{'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request,"lotto/detail.html",{"lotto1":lotto})
