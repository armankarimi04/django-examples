1. install wagtail
```
> pip install wagtail
```

2. generate new wagtail project
```
> wagtail start mysite mysite
```

3. install dependencies
```
> cd <projectFolder: e.g. mysite>
> pip install -r requirements.txt
```

4. initialize database (default is sqlite)
(current command line position must be on the same level as manage.py)
```
> python manage.py migrate
```

5. create a superuser
```
> python manage.py createsuperuser
admin, admin@admin.com, 123, bypass password validation yes
```

6. start server
```
> python manage.py runserver
```
---------------------------------------------

- extend the HomePage model
- make migrations, migrate
(now in wagtail admin, Home page can be edited)
(we did some editing)
(the template of this page is home/templates/home/home_page.html)

- naming convention used for wagtail templates:
model: BlogPage
template name: blog_page.html
