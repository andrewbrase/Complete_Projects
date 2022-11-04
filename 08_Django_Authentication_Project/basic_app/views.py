from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):

    return render(request, 'basic_app/index.html')

def register(request):

    # assume at first they are not registered
    registered=False

    # if the request is POST, grab the forms and assign them to variables
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # hashing the password
            user.set_password(user.password)
            # saving the hashed password to the database
            user.save()

            profile = profile_form.save(commit=False)
            # this sets up the 1 to 1 relationship 
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    # there was no request yet
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', 
    {'registered':registered,
     'user_form':user_form,
     'profile_form':profile_form
    })