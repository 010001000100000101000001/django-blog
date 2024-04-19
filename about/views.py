from django.shortcuts import render
from django.contrib import messages  # Import messages framework
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.

    **Template**
    :template:`about/about.html`
    """
    # Check if the request method is POST
    if request.method == "POST":
        # Populate the CollaborateForm with the POST data
        collaborate_form = CollaborateForm(request.POST)

        # Check if the form data is valid
        if collaborate_form.is_valid():
            # Save the form data to the database
            collaborate_form.save()

            # Add a success message using the messages framework
            messages.add_message(
                request, messages.SUCCESS,
                "Request received! I will respond within 2 working days."
            )

    # Retrieve the latest About object
    about = About.objects.order_by('-updated_on').first()

    # Initialize a blank CollaborateForm
    collaborate_form = CollaborateForm()

    """
    Render the about.html template, passing the
    about and collaborate_form objects
    """
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
