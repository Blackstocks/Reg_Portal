# Reg_Portal
Transformed competition evaluation with an innovative judging portal leveraging HTML, CSS, JavaScript, Django


#Setting up the environment:
Open the project folder in VS Code 
Check the version of python and Django. If nothing appear then run the command
          python -m pip install django
          python -m django --version
Now activate the virtual environment
          ./bin/activate(Windows)
          source ./bin/activate(Linux/MacOs)
Change the directory to reg_portal by:
          cd reg_portal
Now install certain Module
          python -m pip install Pillow
Now you are in the Django project directory. You can run the following to start server:
python manage.py runserver

File Structure:
.reg_portal
├── ead
├── lsm
├── empresario
├── landingPage
|   └── landingPage app folder
├── reg_portal
|   └── main project folder
└── media
   └── profiles
       └── uploaded profile images are stored here

reg_portal is the main project folder containing the settings.py, main urls.py
landingPage folder is the app folder handles the templates of main reg_portal. It also contains the model CustomUser which is an extension of abstract user of django and it is being used as the authentication model
Every initiative has its own app, ead, lsm and empresario

Way of doing stuff:
The working or default brach in the github is ead-dash.
All the forms are made in form.py and then passed then to the templates
All the static css files are named as “app_name.css” in order to avoid clashes. The class names are generic and while styling access the class by using the whole structure for example, “.main .card .profile h4” in order to avoid issues.
There is a main template.html in every app templates and every other extends it for the dashboard part and the same for login and register as well.
Decorators have been used in various apps to restrict the views to authenticated user.
All the urls are named as “app_url” for example “empresario_dashboard”.
Every app has its model named as “APPUser” for example EADUser that maps to the CustomUser by one to one maping. In the case of empresario we also have a questionnaire that extends and a notice model.
For empresario there is a questionnaire submitted boolean value in the EmpresarioUser model that is used to know weather the user has submitted it or not. If not the questionnaire is shown in the dashboard.
Every CustomUser has three boolean values for now namely ead, lsm and empresario and when a user registers depending on the page he is registering lets say lsm then lsm value will be true.
In case of empresario the user username will be his primary email.
The custom user has username, email and name. And ead, lsm and empresario.
All the styling is done by following responsive grid view.
As of now the dashboard of empresario has the working and presentable code and that needs to be done in ead and lsm.
The otp hasn’t been setup yet but it can be done, and its stuff are assigned in lower part of settings.py.
The template folder in every app folder has the following structure and while accessing then to render in view, it goes as render(request, ‘appname/file.html’)
appname
└── templates
   └── appname
       └── file.html
