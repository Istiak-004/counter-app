from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect, reverse
from .models import Counter_app
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import counterForm

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect(reverse('login'))

        return render(request, 'register.html', { 'form': form })


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', { 'form':  AuthenticationForm })

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'login.html',
                    { 'form': form}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'login.html',
                    { 'form': form }
                )
            login(request, user)

            return redirect('counter')

@login_required
def CounterView(request):
    form = counterForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'counter.html',{'form':form})
