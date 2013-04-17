Django Project Template
========================

This is the template that I use to create a new django project for development in a windows environment.

* admin is enabled by default

* settings file with appropriate substitution with {{ project_name }} variable, where needed. {{ secret_key }} variable is also substituted.

* A fixtures folder with intial date to create a superuser without prompting for any input while syncing db is  added. Put this folder in one of the installed apps.

* urls file has the code to enable serving static and media files in the development server.

* By default the database is set to in-project sqlite3 db file method

* media, static, templates folders created

* 404, 500, base templates created inside the templates folder

* cmd files created for common tasks like syncing, running server, creating app, launching shell

* gtignore file is created to ignore local settings, db file etc,.

To create project with this template

```
git clone https://github.com/affenity/django-project-template.git
python django-admin.py startproject --template=django-project-template <project_name>
```

