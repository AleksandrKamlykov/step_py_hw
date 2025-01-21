from django.shortcuts import render, redirect
from .forms import RegistrForm

def index(request):
    return render(request, 'users/index.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            full_name = form.cleaned_data['full_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            avatar = form.cleaned_data['avatar']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Save the data to the database or perform other actions

            # Redirect to the info page with the form data
            return redirect('info', full_name=full_name, date_of_birth=date_of_birth, avatar=avatar, email=email)

    else:
        form = RegistrForm()

    return render(request, 'users/registration.html', {'form': form})


def info(request, full_name, date_of_birth, avatar, email):
    context = {
        'full_name': full_name,
        'date_of_birth': date_of_birth,
        'avatar': avatar,
        'email': email,
    }
    return render(request, 'users/info.html', context)