from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse 
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
	context = {
		"title":"Hello World!",
		"content":"Welcome to the home page"
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"About page",
		"content":"Welcome to the about page"

	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Contact_page",
		"content":"Welcome to the contact page",
		"form": contact_form

	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))

	return render(request, "contact/view.html", context)	


# def login_page(request):
# 	form = LoginForm(request.POST or None)
# 	context = {
# 		"form": form
# 	}
# 	print("User logged in")
# 	print(request.user.is_authenticated())
# 	if form.is_valid():
# 		print(form.cleaned_data)
# 		username = form.cleaned_data.get("username")
# 		password = form.cleaned_data.get("password")
# 		user = authenticate(request, username=username, password=password)
# 		print(user)
# 		print(request.user.is_authenticated())
# 		# context['form'] = LoginForm()

# 		if user is not None:
# 			print(request.user.is_authenticated())

# 			login(request, user)
# 			# print("user is logggeed")
# 			# context['form'] = LoginForm()
# 			return redirect("/login")
# 		else:
# 			print("Error")
# 		# context['form'] = LoginForm()

# 	return render(request, "auth/login.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)

def register_page(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)

	return render(request, "auth/register.html", {})




def home_page_old(request):
	html_ = """
	<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

	    <title>Hello, world!</title>
	  </head>
	  <body>
	  	<div class="text-center">
	    	<h1>Hello, world!</h1>
	    </div>	
	    	
	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
	  </body>
	</html>
	"""


	return HttpResponse(html_)