# Epic Events: Develop a secured back-end architecture using Django ORM

## Summary

| #               | Feature                                     |
|-----------------|---------------------------------------------|
|[1](#feature-one)| app uses Django and PostgreSQL              |
|[2](#feature-two)| adds connexion page for users               |



## #Feature one 
### app uses Django and PostgreSQL

app uses:

- Python 3
- Django (version 3.0+)
- PostgreSQL database(version 12.0+)

#### Installation

In a Command Line Interface:

| Comment                                    | Folder                | Instruction                                                             |
|--------------------------------------------|-----------------------|-------------------------------------------------------------------------|
| clone the repository                       | folder of your choice | ```git clone https://github.com/RafaRemote/dapy_p12_epic_events.git```  |
| change directory to the cloned repo        | same as previously    | ```cd dapy_p12_epic_events```                                           |
| create a virtual environment               | root                  | ```python -m venv env```                                                |
| activate the virtual environment           | root                  | ```source env/bin/activate```                                           |
| upgrade pip                                | root                  | ```pip install --upgrade pip```                                         |
| install the dependencies                   | root                  | ```pip install -r requirements.txt```                                   |

==> Check if the version of your interpreter is Python 3.9.2

#### Run the application

| Comment                                    | Folder             | Instruction                                                       |
|--------------------------------------------|--------------------|-------------------------------------------------------------------|
| change to root directory                   | chose folder       | ```cd epicevents```                                               |
| run the server                             | root               | ```python manage.py runserver```                                  |

Then, in your web browser navigate to http://127.0.0.1:8000/

#### Tests

Tests checks these below conditions:

| Item                         | version        | 
|------------------------------|----------------|
| Python                       | 3              |
| Django                       | 3.0+           |
| PostgreSQL                   | 12.0+          |

#### Run the tests

In the Command Line Interface:

| Comment                                    | Folder             | Instruction                                                  |
|--------------------------------------------|--------------------|--------------------------------------------------------------|
| run tests                                  | root               | ```python manage.py test```                                  |
| run tests with verbose option              | root               | ```python manage.py test -v 2```                             |

## #Feature two 
### adds a connexion page for users

#### 