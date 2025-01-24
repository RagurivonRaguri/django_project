from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User,Treatment, Disease
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from django.contrib.auth.hashers import make_password

# Create your views here.
#opening page viw
def opening(request):
    template_one = loader.get_template('index.html')
    return HttpResponse(template_one.render())

@csrf_exempt
def validate_form(request):
    if request.method == "POST":
        # Extract personal details from the form
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        
        # Extract the selected disease name from the form
        disease_name = request.POST.get("disease", "").strip()

        # Server-side validation for personal details
        if not name:
            return render(request, "index.html", {"error": "Name is required."})
        if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email):
            return render(request, "index.html", {"error": "Invalid email address."})
        if len(password) < 6:
            return render(request, "index.html", {"error": "Password must be at least 6 characters long."})
        
        # Server-side validation for the disease name
        try:
            disease = Disease.objects.get(name=disease_name)
        except Disease.DoesNotExist:
            return render(request, "index.html", {"error": "Invalid disease selected."})

        # Fetch the related treatment (you can customize logic here)
        treatment = disease.treatments.first()  # Fetch the first treatment related to the disease
        if not treatment:
            return render(request, "index.html", {"error": "No treatment found for the selected disease."})

        # Hash the password before saving the user
        hashed_password = make_password(password)

        # Save the user to the database
        try:
            user = User(name=name, email=email, password=hashed_password, disease=disease, treatment=treatment)
            user.save()

            # Return success response with user details
            return render(request, "success.html", {
                "name": user.name,
                "email": user.email,
                "disease": disease.name,
                "treatment": treatment,
            })
        except Exception as e:
            # Handle errors and return error.html template
            return render(request, "error.html", {"error": str(e)})

    # Handle GET request: Show the form
    return render(request, "index.html")



#view to show the success page
def success(request):
    template_two = loader.get_template('success.html')
    return HttpResponse(template_two.render())


def error(request):
    template_three = loader.get_template('error.html')
    return HttpResponse(template_three.render())