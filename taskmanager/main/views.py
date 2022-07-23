from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Task
from .forms import TaskForm
from .models import Article
def index(request):
    tasks = Task.objects.order_by("-id")
    return render(request, "main/index.html", {"title": "Главная страница сайта", "task": tasks} )


def about(request):
    return render(request, "main/about.html")


def Max(request):
    return render(request, "main/Max Verstappen.html")


def create(request):
    error=""
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error= "Форма была неверной"
    form = TaskForm()
    context={
        "form": form,
        "error": error
    }
    return render(request, "main/create.html", context)


def test(request):
    Articles=Article.objects.order_by("-pubdate")
    return render(request, "main/test.html",{"article":Articles})




def article_page(request, slug):
    article_correct = Article.objects.get(slug=slug)
    return render(request, "main/article_page.html",{"article_correct": article_correct})

