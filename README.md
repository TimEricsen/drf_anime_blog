# API blog, using DRF
## Local use
1. Open folder as project.
2. Agree to a request to automatically add a virtual environment with all dependencies.
3. Create admin user for use

```python manage.py createsuperuser```

4. Do all the steps of creating.
5. After that, make migrations of your app to create tables in your DB.

```python manage.py makemigrations AnimeApp```

6. Then, make migrate step.

```python manage.py migrate```

7. And run your local server.

```python manage.py runserver```

You can see all the links available in the API and follow them.
Or use the special documentation for API (e.g. SwaggerUI)

You have to add all the objects by yourself (genres, studios, anime etc.)
