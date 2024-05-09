**Documentation**: [django-base-site.readthedocs.org](http://django-base-site.readthedocs.org/)  
**Source Code**: [github.com/epicserve/django-base-site](https://github.com/epicserve/django-base-site/)

## ✨ Features

### 🧑‍💻 Best Practices

* [Environs](https://github.com/sloria/environs) - Used for managing environment variables
* [Docker](https://www.docker.com/) - Docker Compose for development and a multi-stage Dockerfile for production ready

### 📦️ Django Packages

* [Django 5](https://www.djangoproject.com/) - Latest version of Django

[custom_user_model]: https://docs.djangoproject.com/en/stable/topics/auth/customizing/#substituting-a-custom-user-model

### 🔧 Python Testing Tools

* [Pytest](https://docs.pytest.org/) - The most popular Python test runner in the Python community
* [Pytest Django](https://pytest-django.readthedocs.io/en/latest/index.html) - A Django plugin for Pytest
* [Pytest-cov](https://pytest-cov.readthedocs.io) - Adds code coverage to tests

### 🩺 Code Quality, Formatting, and Linting Tools

* [Ruff](https://github.com/charliermarsh/ruff) - Python formatting and linting. Lighting fast because it's written in Rust! Replaces Black and other tools.
* [Mypy](http://mypy-lang.org/) - Python Type checking
* [dj Lint](https://djlint.com/) - Automatic Django HTML template formatting and linting
* [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar) - A toolbar for debugging and
  optimizing Django queries
* [Stylelint](https://stylelint.io/) - Automatic Sass formatting and linting
* [Eslint](https://eslint.org/) - Automatic Javascript formatting and linting

### 💄Frontend

* [Bootstrap 5](https://getbootstrap.com/) - A popular UI framework
* [Vite](https://vitejs.dev/) - A fast frontend build tool


## Installation

### Requirements

Before proceeding make sure you have installed [Docker](https://docs.docker.com/engine/installation/) and
[Just](https://github.com/casey/just#installation). Docker with Docker Compose is used for local development and Just is
used common project commands.

### Quickstart Install Script

Copy and past the following into your terminal to run the install script:

```bash
bash <(curl -s https://raw.githubusercontent.com/epicserve/django-base-site/main/scripts/start_new_project)
```

Running the script mostly does the same thing as manual method. The exception is that the install script has
questions to customize your new project setup.

**Note:** When starting the Django runserver it will take several seconds before the CSS styles take effect. This is
because Vite is running in dev mode which takes a few seconds to take effect.

Example output:

    $ cd ~/Sites
    $ bash <(curl -s https://raw.githubusercontent.com/epicserve/django-base-site/main/scripts/start_new_project)
    
    What is the project name slug [example]?
    What directory do you want your project in [/Users/brento/Sites/example]?

    Done.

    To start Docker Compose run:
    $ cd /Users/brento/Sites/example
    $ just start

### Manual Installation

    $ curl -LOk https://github.com/epicserve/django-base-site/archive/main.zip && unzip main
    $ mv django-base-site-main example
    $ cd example
    $ export SECRET_KEY=$(python -c "import random; print(''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789%^&*(-_=+)') for i in range(50)))")
    $ cat > .env <<EOF
    DEBUG=on
    SECRET_KEY='$SECRET_KEY'
    DATABASE_URL=postgres://postgres:@db:5432/postgres
    INTERNAL_IPS=127.0.0.1,0.0.0.0
    EOF
    $ just remove_extra_files
    $ find ./public -name ".keep" | xargs rm -rf
    $ just start

## Usage

The Django Base Site comes with Just recipes for all the most common commands and tasks that an engineer will use during
development. To see the full list of commands run `just` in the root of the project directory. The following is an
abbreviated list of the most common commands.

```
build_assets                 # Build frontend assets
clean                        # Remove build files, python cache files and test coverage data
collectstatic                # Run Django's collectstatic management command
format                       # Format all code
lint                         # Lint everything
upgrade_python_requirements  # Run pip-compile make the requirement files
open_coverage                # Run the django test runner with coverage
start                        # Start docker-compose
start_with_docs              # Start docker-compose with docs
stop                         # Stop all docker-compose services
test                         # Run the Django test runner without coverage
```

## Deploying to Production

The Django base site is designed to be production ready because it comes with a production
ready [multi-stage Dockerfile](https://github.com/epicserve/django-base-site/blob/main/config/docker/Dockerfile).
You can also read a [blog post](https://epicserve.com/django/2022/12/30/using-flyio-with-the-django-base-site.html)
about using it with fly.io. If you want to blog about using the Django Base Site with other PaaS providers, please let
me know, and I can link to the post here.
## Tech Stack
