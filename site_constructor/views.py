from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import login, logout


from .models import LanguagesList
from .forms import RegistrationForm, SiteProfileForm, LoginForm
from users.models import ProfileUser


# class HomeLanduages(View):
#     model = LanguagesList
#     template_name = 'site_constructor/index.html'
#     context_object_name = 'languages'

def index(request):
    languages = LanguagesList.objects.all()
    return render(request, 'site_constructor/index.html', {'languages': languages})


# class SignInView(View):
#     model = ProfileUser
#     template_name = 'site_constructor/sign_in.html'

def mentors(request):
    data = []
    return render(request, 'site_constructor/mentors.html', {'data': data})


class SearchView(View):
    template_name = 'site_constructor/index.html'

    def post(self, request):
        search = request.POST["search"]
        languages = LanguagesList.objects.filter(language_name=search).all()
        return render(request, self.template_name, {'languages': languages})
        # return HttpResponse(str(request.POST), content_type='text/plain')


class SiteProfileView(View):
    template_name = 'site_constructor/site_profile.html'

    def get(self, request):
        language_info = LanguagesList.objects.all()
        user_id = request.user.id
        user_info = ProfileUser.objects.get(id=user_id)
        profile_form = SiteProfileForm()
        return render(request, self.template_name,
                      {'profile_form': profile_form,
                       'user_info': user_info,
                       "language_info": language_info})

    def post(self, request):
        form = SiteProfileForm(request.POST, request.FILES)
        user_id = request.user.id
        data = request.POST
        about_you = data['about_you']
        if form.is_valid():
            # language_list = data['language_list']
            user = ProfileUser.objects.get(id=user_id)
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.phone_number = form.cleaned_data.get('phone_number')
            user.user_photo = form.cleaned_data.get('user_photo')
            user.about_you = about_you
            # user.about_you = form.cleaned_data.get('about_you')
            user.linked_in = form.cleaned_data.get('linked_in')
            user.save()
            return redirect("site_profile")
        else:
            return HttpResponse("Error!", content_type="text/plain")


class RegistrationView(View):
    template_name = 'site_constructor/registration.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'reg_form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        data = request.POST
        first_name = data["first_name"]
        user_name = data["user_name"]
        email = data["email"]
        types = data['types']
        password = data["password"]
        password_retype = data["password_retype"]

        if form.is_valid():
            if ProfileUser.objects.filter(username=user_name).exists() is False and password == password_retype:
                profile = ProfileUser.objects.create(username=user_name, email=email, first_name=first_name, types=types)
                profile.set_password(password)
                profile.save()
                return HttpResponse("Exelent! Please, confirm your e-mail!", content_type="text/plain")
            elif ProfileUser.objects.filter(username=user_name).exists() is True:
                return HttpResponse("Username exists. Please, take other!", content_type="text/plain")
        return HttpResponse("Error!", content_type="text/plain")


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = LoginForm()
    return render(request, 'site_constructor/sign_in.html', {'login_form': form})


def user_logout(request):
    logout(request)
    return redirect('home_page')
