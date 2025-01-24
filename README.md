SCT211-0420/2023 Lincoln Muraguri
SCT211-0239/2023 Bryan Kweri                           
                                
                                Django Project Documentation
Project Overview
This Django project is a web application that helps users to select diseases and corresponding treatments. The user can enter personal details, select a disease, and get treatment information. The application also provides server-side validation to ensure the accuracy and integrity of the data provided.

Features
User Registration: Users can enter their name, email, and password.
Disease Selection: Users can select a disease from the list.
Treatment Display: Based on the disease selected, the treatment information is displayed.
Error Handling: The system handles validation errors for user input and displays appropriate messages.
Responsive Design: The project includes responsive CSS for compatibility with different devices.
Setup and Installation
Follow these steps to set up and run the project locally:

cd your-django-project
1. Create a Virtual Environment
Ensure that you are working in a clean virtual environment to avoid dependency conflicts.
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
2. Install Project Dependencies
Install the required Python packages using pip:
3. Set Up Static Files
Make sure that the static files are correctly served by Django. Add the following to your settings.py:

4. Database Setup
Make sure to set up the database. For the development environment, you can use the default SQLite database.

Apply database migrations:
python manage.py migrate

6. Run the Server
Start the Django development server by running:
python manage.py runserver


                        How the Project Works
    Model Structure
User: Represents the user who inputs personal details like name, email, and password.
Disease: Represents different diseases. Each disease can have multiple associated treatments.
Treatment: Represents the treatment related to a specific disease.
View Logic
The validate_form view handles form submissions. It extracts data from the POST request, validates the input, and either displays an error or saves the user data along with the selected disease and treatment.
If the form submission is successful, the user is redirected to a success page showing their details.
Template Structure
index.html: Displays the form for user input (name, email, password, and disease selection).
success.html: Displays the user's information after successful submission (name, email, disease, and treatment).
error.html: Displays an error message in case of validation issues.
Common Issues and Troubleshooting
Static Files Not Loading:
Make sure {% load static %} is included at the top of your template.
Check if the static files are correctly configured in settings.py under STATIC_URL and STATICFILES_DIRS.
Database Migration Issues:
If you're facing issues with migrations:
Run python manage.py migrate to ensure the database schema is up to date.
CSRF Token Error:
If you're getting a CSRF token error:
Ensure that {% csrf_token %} is included inside the form tag in your HTML templates.
                                Conclusion
This Django project helps users input their details, select a disease, and view the related treatment. By following the steps above, you should be able to run the project locally and contribute further to its development.

