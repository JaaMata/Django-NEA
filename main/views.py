from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import LoginForm, StudentForm, StudentSearchForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class SignUp(View):
    form = UserCreationForm
    template_name = 'forms/user_creation_form.html'

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid() and form.clean():
            username = form['username'].value()
            password = form['password1'].value()
            user = User(username=username, password=password)
            user.save()

            first_name = form['first_name'].value()
            last_name = form['last_name'].value()
            teacher = Teacher(account=user, first_name=first_name, last_name=last_name)
            teacher.save()
            login(request, user)
            return redirect('home')
        else:
            context = {'form' : self.form, 'form' : form}
            return render(request, self.template_name, context)

class LoginView(View):
    form = LoginForm
    template_name = 'forms/login.html'

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {
                    'errors': "The password or username are not correct",
                    'form': form}
                return render(request, self.template_name, context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateStudentView(View):
    form = StudentForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return render(request, 'forms/create_student.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.student_id = Student.generate_id()
            obj.email = Student.email_gen(obj)
            obj.save()

            return redirect('home')

        context = {'form': form}
        return render(request, 'forms/create_student.html', context)

class StudentSearchView(View):
        form = StudentSearchForm
