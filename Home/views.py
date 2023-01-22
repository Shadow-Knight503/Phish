from django.shortcuts import render
from .models import UserCreds
from .forms import UserForm


# Create your views here.
def home(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            form = user_form.save(commit=False)
            form.save()
            print("Submitted")

    ctx = {
        'form': user_form,
    }
    return render(request, "Home.html", ctx)


def List(request):
    users = UserCreds.objects.all()
    ctx = {
        "Users": users,
    }
    return render(request, "List.html", ctx)
