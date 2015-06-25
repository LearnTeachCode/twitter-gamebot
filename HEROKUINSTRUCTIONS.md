# Python + Heroku = :heart:

Python is a philosophy of elegance that spawned a community which speaks a common-enough programming language aimed at tying imagination into practicality.
Heroku is a Platform as a Service (PaaS) host for deploying applications.

## Prerequisites
* [Heroku toolbelt](https://toolbelt.heroku.com/)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python](https://www.python.org/)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Enviornment setup instructions

_Start by making a project directory and a virtual environment._

```python
mkdir application
cd application
virtualenv --python=pythonX.X env
source env/bin/activate
```

This will create a _virtual python environment_ for Python X.X (_pick a version_) in a directory named env. python --version will show you that the version which you requested is not your _system default python_! :heart:

_Install any required python libraries into your virtual enviornment_

```python
pip install xxx
```

## Create you application

```python
application-name-xxxx.py

code code code 


```

## Deployment

_create a heroku application_

```python
heroku create application-name-xxxx
```

_You'll see an app-name and a git-address_
_connect your Heroku app into your git repository by adding the Heroku git repo as a remote_

```python
git init
heroku git::remote -a application-name-xxxx
```

## Heroku-izing your Python application

_you'll need the following files_

```python
requirements.txt
runtime.txt
Procfile
.gitignore
```

#### requirements.txt
_run this any time you update your libraries_

```python
pip freeze > requirements.txt
```

#### runtime.txt
This file tells Heroku what version of python to run your application. You should set it to the version you're using in your virtual environment.

```python
python-2.7.10
```

#### Procfile
This file tells Heroku about the processes needed for your app.  You'll need to consult the Heroku documentation in order to decide which process best fits your need.

```python
worker: python application-name-xxxx.py
```

#### .gitignore

```python
__pycache__/
env/
*.pyc
```

## Environment variables

heroku config:set VAR1=value1 VAR2=value2

Accessing in code:

```python
import os
os.environ['VAR1'] _gets value1_
os.environ['VAR2'] _gets value2_
```

## Push to github

```python
git add .
git commit -m ":thumbsup:"
git push origin master
```

## Push to Heroku

```python
git add .
git commit -m ":thumbsup:"
git push heroku master
```

#First deployment

log in to Heroku, go to your application dashboard, and increase the number of dynos allocated to your application to 1

## Viewing output and logs

_from the application directory_

```python
heroku logs
```