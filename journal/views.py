from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignupForm,JournalForm
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='userlogin')
def dashboard(request):
    getname = Profile.objects.get(user__username = request.user.username)
    journal = Journal.objects.select_related('user').filter(user= request.user).order_by('-id')
    count = journal.count()

    context = {
        'getname':getname,
        'journal':journal,
        'count':count
    }
    return render(request, 'dashboard.html',context)

@login_required(login_url='userlogin')
def journal(request):
    journal = Journal.objects.filter(user__username = request.user.username)

    if request.method == 'POST':
        date = request.POST['date']
        pair = request.POST['pair']
        time_open = request.POST['time_open']
        time_close = request.POST['time_close']
        duration = request.POST ['duration']
        session = request.POST ['session']
        longorshort = request.POST ['longorshort']
        entry = request.POST ['entry']
        stop_loss = request.POST ['stop_loss']
        outcome = request.POST ['outcome']
        rr = request.POST ['rr']
        note = request.POST['note']

        jot = Journal()
        jot.user = request.user
        jot.date = date
        jot.pair = pair
        jot.time_open = time_open
        jot.time_close = time_close
        jot.duration = duration
        jot.session = session
        jot.longorshort = longorshort
        jot.entry = entry
        jot.stop_loss = stop_loss
        jot.outcome =outcome
        jot.rr = rr
        jot.note = note
        jot.save()
        return redirect ('dashboard')


    context = {
        'journals':journal
    }
    return render(request, 'journal.html',context)

def userlogin(request):
    if request.method == "POST":
        name = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username = name,password = passw)
        if user:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('dashboard')
        else:
            messages.warning(request,'Username/password incorrect')
            return redirect('userlogin')
    return render(request, 'userlogin.html')



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            newprofile = Profile(user=newuser)
            newprofile.first_name = newuser.first_name
            newprofile.last_name = newuser.last_name
            newprofile.email = newuser.email
            newprofile.save()
            login(request, newuser)
            messages.success(request, 'Signup successful!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def learnforex(request):
    return render(request, 'learnforex.html')

def signout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='userlogin')
def profile(request):
    profile = Profile.objects.get(user__username = request.user.username)

    context = {
        'profile':profile
    }
    return render(request, 'profile.html', context)

@login_required(login_url='userlogin')
def update(request, journal_id):
    journal = get_object_or_404(Journal,id=journal_id, user=request.user)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the list of journals or any other desired page
    else:
        form = JournalForm(instance=journal)

        context = {
            'form':form,
            'journal':journal
        }
    return render(request,'journal_update.html',context )

