from django.shortcuts import render
from .models import About
from .forms import CollaborateForm  # Import the CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()  # Initialize a blank form

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},  # Pass the form to the template
    )
