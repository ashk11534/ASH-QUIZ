from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, UpdateUserForm

from django.contrib.auth.models import User

from base_app.models import Exam

from django.contrib.sites.shortcuts import get_current_site

from django.template.loader import render_to_string

from .token_generator import user_tokenizer_generate

from django.utils.encoding import force_bytes, force_str

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.is_active = False

            user.save()

            current_site = get_current_site(request)

            subject = 'Account verification email'

            message = render_to_string('account/registration/email-verification.html', {

                'user': user,

                'domain': current_site.domain,

                'uid': urlsafe_base64_encode(force_bytes(user.pk)),

                'token': user_tokenizer_generate.make_token(user)

            })

            user.email_user(subject=subject, message=message)

            return redirect('email-verification-sent')
        
    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)


def email_verification(request, uidb64, token):

    unique_id = force_str(urlsafe_base64_decode(uidb64))

    user = User.objects.get(pk=unique_id)

    if user and user_tokenizer_generate.check_token(user, token):

        user.is_active = True

        user.save()

        return redirect('email-verification-success')

    else:

        return redirect('email-verification-failed')


def email_verification_sent(request):

    return render(request, 'account/registration/email-verification-sent.html')

def email_verification_success(request):

    return render(request, 'account/registration/email-verification-success.html')

def email_verification_failed(request):

    return render(request, 'account/registration/email-verification-failed.html')


def my_login(request):
    
    if request.user.is_authenticated:

        return redirect('home')

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')

            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect('dashboard')

    context = {'form': form}

    return render(request, 'account/my-login.html', context=context)


@login_required(login_url='my-login')
def dashboard(request):

    exam_participations = Exam.objects.filter(participants__id = request.user.id)

    context = {'exam_participations': exam_participations}

    return render(request, 'account/dashboard.html', context = context)


@login_required(login_url='my-login')
def delete_exam(request, exam_id):

    exam = Exam.objects.get(id = exam_id)

    exam.participants.remove(request.user)

    return redirect('dashboard')


@login_required(login_url='my-login')
def user_logout(request):

    logout(request)

    messages.success(request, 'Logout success')

    return redirect('home')

@login_required(login_url='my-login')
def profile_management(request):

    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():

            user_form.save()

            messages.info(request, 'Account updated')

            return redirect('dashboard')

    context = {'user_form': user_form}

    return render(request, 'account/profile-management.html', context=context)


@login_required(login_url='my-login')
def delete_account(request):

    user = User.objects.get(id = request.user.id)

    if request.method == 'POST':

        user.delete()

        messages.error(request, 'Account deleted')

        return redirect('home')

    return render(request, 'account/delete-account.html')