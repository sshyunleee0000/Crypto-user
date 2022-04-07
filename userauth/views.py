from django.shortcuts import render
from userauth.models import User
from django.shortcuts import redirect
import hashlib
import os


def home(request):
    return render(request, "home.html")

def login_check(request):
    user_id = request.GET['user_id']
    user_pw = request.GET['user_pw']

    # Calling up saved membership via ID
    use = User.objects.filter(user_id=user_id).values()
    print(use)

    if len(use) == 1:
        # Call the random number used to encrypt the member's password
        salt = use[0]['salt']
        salt = salt.encode()
        # Encrypt in the same way as when signing up
        hash = hashlib.pbkdf2_hmac('sha256', user_pw.encode(), salt, 1000)
        user_pw = use[0]['user_pw'].replace("\\\\", "\\")
        # Compare the encrypted entered password with the stored
        if user_pw == str(hash):
            context = {
            "use": use
            }
            return render(request, "afterlogin.html", context)
        else:
            return render(request, 'home.html', {'Login_error': True})
    else:
        return render(request, 'home.html', {'Login_error': True})

    return render(request, "afterlogin.html")

def logout(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")

def signup_check(request):
    user_id = request.GET['user_id']
    user_pw = request.GET['user_pw']
    user_pw_re = request.GET['user_pw_re']
    # Duplicate ID check
    check = 0
    use = User.objects.values('user_id')
    print(use)
    count = User.objects.count()
    for i in range(count):
        if user_id == use[i]['user_id']:
            check = 1
            break    
    if check == 1:
        return render(request, 'signup.html', {'ID_error': True})
    elif user_pw != user_pw_re:
        return render(request, 'signup.html', {'Signup_error': True})
    else:
        # Generating salt to perform pbkdf2
        salt = os.urandom(16)
        # Encrypt the password
        hash = hashlib.pbkdf2_hmac('sha256', user_pw.encode(), str(salt).encode(), 1000)
        if user_id != "":
            use = User.objects.create(user_id=user_id, user_pw=hash, salt=salt)
            return redirect('/')
        else:
            return redirect('/signup')


    

