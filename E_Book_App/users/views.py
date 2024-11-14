from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from .forms import AppUserForm, LogoutUserForm, EditUserForm, DeleteUserForm
from .models import AppUser, Profile


class RegisterUserView(CreateView):
    form_class = AppUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form = super().form_valid(form)
        login(self.request, self.object)
        return form


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

    form = LogoutUserForm()
    context = {'form': form}
    return render(request, 'users/logout.html', context=context)


def profile_page(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/profile-page.html', context=context)


@login_required
def profile_edit_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile-page')
    else:
        form = EditUserForm(instance=profile)

    context = {'form': form}
    return render(request, 'users/profile-edit.html', context=context)


@login_required
def profile_delete_view(request):
    user = request.user
    form = DeleteUserForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user_profile = user.profile
        user.delete()
        logout(request)
        return redirect('index')

    context = {'form': form}

    return render(request, 'users/profile-delete.html', context=context)
