import requests
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required




def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        api_url = 'http://127.0.0.1:8000/api/register/' 

        data = {
            'username': username,
            'email': email,
            'password': password,
        }

        response = requests.post(api_url, json=data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        
        if response.status_code == 201:
            return render(request, 'signup.html', {'success': 'User created successfully. You can now login.'})
        else:

            try:
                error_message = response.json()  # Try to parse JSON
            except ValueError:
                error_message = 'An error occurred. Please try again.'
            
            # If the error message exists in the response, return it
            if 'detail' in error_message:
                error_message = error_message['detail']
            
            return render(request, 'signup.html', {'error': f'Failed to create user: {error_message}'})
    return render(request, 'signup.html')



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password') 
       
       
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print(f"User: {user.username}, is_superuser: {user.is_superuser}")

            if user.is_superuser:
                return redirect('admin_dashboard') 
            else:
                return redirect('user_dashboard') 
        else:       
            print(f"Authentication failed for username: {username}")   
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html') 




@login_required
def admin_dashboard(request):
    print(f"Logged in user: {request.user}")
    
    if request.user.is_authenticated:  # Ensure the user is authenticated
        #print(f"User is the superuser: {request.user.is_superuser}")
        
        if request.user.is_superuser:
            messages.success(request, "Successfully logged in as superuser.")
            users = User.objects.all()  
            return render(request, 'admin_dashboard.html', {'users': users})
        else:
            return render(request, 'admin_dashboard.html', {'message': 'You do not have superuser privileges.'})
    else:
        return render(request, 'admin_dashboard.html', {'message': 'You need to log in first.'})   



@login_required
def user_dashboard(request):
    return render(request, 'usersdashboard/user_dashboard.html')


def LogoutPage(request):
        logout(request)
        return redirect('')


def add_user(request):
    if request.method == 'POST':
        #getting the form data fields...
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            User.objects.create(username=username, email=email, password=password)
            return render(request, 'add_user.html', {'success': 'User added sucessfully!'})
        except Exception as e:
            return render(request, 'add_user.html', {'error':f'Error:{str(e)}'})
        #getting back our empty form after adding the user
    return render(request, 'add_user.html')   
