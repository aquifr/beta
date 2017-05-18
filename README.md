# Aquifr Open-Source Crowdfunding Platform

## Getting Started (back-end development)

Using a virtual environment is preferred to avoid potential conflicts with other python/django installations. The following steps assume you're running OSX and have homebrew installed. Installing virtualenv wrapper is optional, but does streamline the process of creating more virtualenvs. 

-   Install Python3: `brew install python3`
-   Install virtualenv: `brew install pyenv-virtualenv` 
-   Install pip: `curl https://bootstrap.pypa.io/get-pip.py | python3`
-   Install virtualenvwrapper: `pip install virtualenvwrapper`
    -   The following will have to be added to your bash source file, and sets where virtual environments are stored, the location of project directories, and the location of the installed script.
        ```
        export WORKON_HOME=$HOME/.virtualenvs
        export PROJECT_HOME=$HOME/Devel
        source /usr/local/bin/virtualenvwrapper.sh
        ```
    -   For more information, refer to virtualenvwrapper [documentation](https://virtualenvwrapper.readthedocs.io/en/latest). 
-   Install postgres: `brew install postgresql`

Once the you have the above installed, we can create a virtual environment for your Aquifr install. `mkvirtualenv aquifr` will create a virtual environment and activate it. Note the change in terminal. To exit the virtualenv, use the command `deactivate`. To load the virtualenv, use the command `workon aquifr`.

With the virtualenv loaded, we can get python dependencies with pip. In the app directory, run `pip install -r requirements.txt`.



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

