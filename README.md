# Aquifr Open-Source Crowdfunding Platform

To run on your local machine, make sure you have a Postgres server
running with the following database configurations:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aquifr_db',
        'USER': 'super_user',
        'PASSWORD': 'P1949Mc0x#4z',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

In general, you'll need to follow the following steps:

1. Install Postgres
2. Create a database called `aquifr_db`
3. Add a user called `super_user` with password `P1949Mc0x#4z`
4. Run `python manage.py migrate`

Of course, you can set up your own database settings, but be sure to
change the corresponding lines in `aquifer/settings.py`. In production,
you are encouraged to create a file next to `settings.py` called
`production_settings.py`, which overrides important, private settings.

Don't forget that Postgres needs to be running on your local machine
before running `python manage.py runserver`

