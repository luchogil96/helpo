[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

# helpo

## About
A [Django 1.11](https://www.djangoproject.com/) project boilerplate/template with lots of state of the art libraries and tools like:
- [React](https://facebook.github.io/react/), for building interactive UIs
- [django-js-reverse](https://github.com/ierror/django-js-reverse), for generating URLs on JS
- [Bootstrap 4](https://v4-alpha.getbootstrap.com/), for responsive styling
- [Webpack](https://webpack.js.org/), for bundling static assets
- [Celery](http://www.celeryproject.org/), for background worker tasks
- [WhiteNoise](http://whitenoise.evans.io/en/stable/) with [brotlipy](https://github.com/python-hyper/brotlipy), for efficient static files serving
- [prospector](https://prospector.landscape.io/en/master/) and [ESLint](https://eslint.org/) with [pre-commit](http://pre-commit.com/) for automated quality assurance (does not replace proper testing!)

For continuous integration, a [CircleCI](https://circleci.com/) configuration `circle.yml` is included.

Also, includes a Heroku `app.json` and a working Django `production.py` settings, enabling easy deployments with ['Deploy to Heroku' button](https://devcenter.heroku.com/articles/heroku-button). Those Heroku plugins are included in `app.json`:
- PostgreSQL, for DB
- Redis, for Celery
- Sendgrid, for e-mail sending
- Papertrail, for logs and platform errors alerts (must set them manually)
- Opbeat, for performance monitoring

This is a good starting point for modern Python/JavaScript web projects.

## Project bootstrap [![CircleCI](https://circleci.com/gh/Jumpi96/helpo.png?circle-token=:circle-token)](https://circleci.com/gh/Jumpi96/helpo.png?circle-token=:circle-token)
- [ ] Open the command line and go to the directory you want to start your project in.
- [ ] Start your project using:
```
django-admin startproject theprojectname --extension py,yml,json --name Procfile,README.md,.env.example --template=https://github.com/vintasoftware/django-react-boilerplate/archive/boilerplate-release.zip
```
- [ ] Above: don't forget the `--extension` and `--name` params! (also don't forget to change `theprojectname` to your project's name).
- [ ] Navigate to the project's directory through your command line.
- [ ] Install pipenv if not installed yet: `pip install pipenv` (maybe you'll have to run this command as an OS superuser).
- [ ] Make sure you have Python 3.6 installed.
- [ ] `pipenv install --dev`
- [ ] Activate the newly created virtualenv with `pipenv shell`
- [ ] `npm update --save`
- [ ] `npm update --save-dev`
- [ ] Check for outdated npm dependencies with `npm outdated` and update them.
- [ ] Change the first line of README to the name of the project.
- [ ] Add an email address to the `ADMINS` settings variable in `helpo/helpo/settings/base.py`
- [ ] Change the `SERVER_EMAIL` to the email address used to send e-mails.

After completing ALL of the above, remove this `Project bootstrap` section from the project README. Then follow `Running` below.

## Running
### Setup
- On project root, do the following:
- Create a copy of ``helpo/settings/local.py.example``:  
  `cp helpo/settings/local.py.example helpo/settings/local.py` (remembering you should replace `helpo` with your project's name!).
- Create a copy of ``.env.example``:  
  `cp .env.example .env`
- Create the migrations for `users` app (do this, then remove this line from the README):  
  `python manage.py makemigrations`
- If you get an "there's no module named Django" error, install it through `pip install django<2` and try the step above again.
- Run the migrations:  
  `python manage.py migrate`

### Tools
- Setup [editorconfig](http://editorconfig.org/), [prospector](https://prospector.landscape.io/en/master/) and [ESLint](http://eslint.org/) in the text editor you will use to develop.

### Running the project
- Open a command line window and go to the project's directory.
- `pipenv install --dev`
- `npm install`
- `npm run start`
- Open another command line window and go to the project's directory.
- `pipenv shell`
- `python manage.py runserver`

## Contributing
### How to test `django-admin startproject`
If you made changes to this boilerplate and want to test them, commit your changes and use `git archive -o boilerplate.zip HEAD` to create the template zip. Then, do a `cd ..` and a `django-admin startproject theprojectname --extension py,yml,json --name Procfile,README.md,.env.example --template=django-react-boilerplate/boilerplate.zip` to test the project bootstrap.

### How to test Heroku deployment
Push your changes to a branch and visit `https://dashboard.heroku.com/new?template=https://github.com/fill-org-or-user/fill-project-repo-name/tree/fill-branch` (replace all `fill-*`).

### How to add a 'Deploy to Heroku' button
Read [this](https://devcenter.heroku.com/articles/heroku-button#adding-the-heroku-button).

P.S. if you want to deploy in a different way please check the `app.json` file for what needs to be configured.

Copyright (c) 2018 Vinta Serviços e Soluções Tecnológicas Ltda.
[MIT License](LICENSE.txt)