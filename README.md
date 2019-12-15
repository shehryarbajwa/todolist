# TodoList

## Tech Stack
The tech stack includes:

SQLAlchemy ORM to be the ORM library of choice
PostgreSQL is the database for backend
Python3 and Flask as the server language and server framework
HTML, CSS, and Javascript with Bootstrap 4 for the website's frontend

## Overall:

Models are located in models.py.
Controllers are located in app.py.
The web frontend is located in templates/, which builds static assets deployed to the web server at static/.

## Instructions

## Installing Dependencies
Python 3.7

Follow instructions to install the latest version of python for the platform in the python docs

## Virtual Enviornment

Use this code to download the pip package manager
- python3 -m pip install --user --upgrade pip

Then install:
- python3 -m pip install --user virtualenv

To create a virtual env:
- python3 -m venv env

To activate a virtual env:
- source env/bin/activate

This code is written in Python but run in a virtual environment. By using a virtual environment we minimize the risk of having dependencies that might be deprecated

## PIP Dependencies
Once the virtual environment setup is up and running, install dependencies by naviging to the /backend directory and running:

pip install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.

## Key Dependencies
- Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- SQLAlchemy and Flask-SQLAlchemy are libraries to handle the postgres database.

## Running the server

Create a virtual environment in python using 

From within the ./src directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```
To run the server, execute:

```bash
flask run --reload
```

The --reload flag will detect file changes and restart the server automatically.

## After setup

- Remember to comment out line 15 on app.py

db_drop_and_create_all()

This should be run only at setup and removed once setup. That way we don't reinitialize the database twice