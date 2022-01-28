# Openclassrooms Path: Python Developer
# Project n.12: Develop a secured back-end architecture using Django ORM
## CRM Software Epic-Events 

## Summary

The 6 first features have been developed according to the technical requirements presented in the [kanban](https://www.notion.so/5a4642c14eef48c78c9e1b98a8e0a3fc?v=12d25b7081ba436a9e06f0e99cdcae25).

| #                 | Title                                                        |
|-------------------|--------------------------------------------------------------|
|[1](#feature-one)  | Feature one: app uses Django and PostgreSQL                  |
|[2](#feature-two)  | Feature two: adds connexion page for users                   |
|[3](#feature-three)| Feature three: adds models Account, Contract, Event, Status  |
|[4](#feature-four) | Feature four: adds two django groups                         |
|[5](#feature-five) | Feature five: (soon)                                         |
|[6](#feature-six)  | Feature six: (soon)                                          |
|[7](#tests)        | Tests: tests for all the implemented features                |
|[8](#optimization) | Optimization: propositions                                   |


### Feature one: app uses Django and PostgreSQL

app uses:

- Python 3
- Django (version 3.0+)
- PostgreSQL database(version 12.0+)

#### Installation


In a Command Line Interface:

_the root folder is the directory 'epicevents' containing the manage.py file_

| Comment                                    | Folder                | Instruction                                                             |
|--------------------------------------------|-----------------------|-------------------------------------------------------------------------|
| clone the repository                       | folder of your choice | ```git clone https://github.com/RafaRemote/dapy_p12_epic_events.git```  |
| change directory to the cloned repo        | same as previously    | ```cd dapy_p12_epic_events```                                           |
| create a virtual environment               | root                  | ```python -m venv env```                                                |
| activate the virtual environment           | root                  | ```source env/bin/activate```                                           |
| upgrade pip                                | root                  | ```pip install --upgrade pip```                                         |
| install the dependencies                   | root                  | ```pip install -r requirements.txt```                                   |

==> **Check if the version of your interpreter is Python 3.9.2**

#### Database configuration

First: if not already done: install PostgreSQL on your machine: link => [download PostgreSQL](https://www.postgresql.org/download/)  
Same with pgAdmin4: link => [download pgAdmin4](https://www.pgadmin.org/download/)  

Then: create a database with the settings of your choice.  

In the root folder, rename the file ```.template``` to ```.env```  
Assign the values of your database settings freshly created to the variables below.  
**do not use quotes or double quotes** Correct example: ```DB_NAME=database```    

| Variables expecting values assignment |
|---------------------------------------|
| DB_NAME                               |
| DB_USER                               |
| DB_PASSWORD                           |
| DB_HOST                               |
| DB_PORT                               |

#### Run the application

_the root folder is the directory 'epicevents' containing the manage.py file_

| Comment                                    | Folder             | Instruction                                                       |
|--------------------------------------------|--------------------|-------------------------------------------------------------------|
| change to root directory                   | chosen folder      | ```cd epicevents```                                               |
| run the server                             | root               | ```python manage.py runserver```                                  |

Then, in your web browser navigate to http://127.0.0.1:8000/


### Feature two: connexion page for users

### Migrations

You can let the server run in the first terminal and open a second terminal.  
A custom user model have been created.  
In order to save the changes to the database type:  

| Comment                                    | Folder             | Instruction                                                  |
|--------------------------------------------|--------------------|--------------------------------------------------------------|
| prepare the migration files                | root               | ```python manage.py makemigrations```                        |
| migrate to the database                    | root               | ```python manage.py migrate```                               |


### Access to admin login page


First: in the CLI, create a super user, type: ```python manage.py createsuperuser```  
You'll need to provide a username and a password.  

Then in your web browser navigate to http://127.0.0.1:8000/admin/  

You can access the admin page with the credentials you have entered for the superuser.  

On the admin page you can create users.  
There is three roles available for the users:  
- management
- sales
- support

Only the users with a management role can access to the admin page.  

You can try to create users for management, sales and support then try to login to the admin site.  
You will see that only the users with a management role can access the admin site.  

### Feature three: application handles new models

There is four new apps in this project.  
Four new main models are handled by the application, they have the same name as the apps.  
On the admin main page you will the presence of theses four new models.  

| Models handled by the application   |
|-------------------------------------|
| Account                             |
| Contract                            |
| Event                               |
| Status                              |

#### Migrations

In the CLI:

| Comment                                    | Folder             | Instruction to type                                                    |
|--------------------------------------------|--------------------|------------------------------------------------------------------------|
| prepare the migration files                | root               | ```python manage.py makemigrations account contract event status```    |
| migrate to the database                    | root               | ```python manage.py migrate```                                         |

You will need to populate the database in order to have statuses to use.  
You have two options:  

- option 1: create the statuses via the admin page. Status suggested: "planning", "live", "cancelled", "terminated". (you can add how many statuses you want)
- option 2: in the root folder (_the folder named 'epicevents' containing the file 'load_statuses.py' and 'manage.py'), type : ```python load_statuses.py```, it will create the above suggested statuses.


#### Usage

In the admin site, providing that you are a superuser you can now:
- Create, Read, Update or Delete an Account,
- Create, Read, Update or Delete a Contract,
- Read, Update an Event,
- Create a Status.

The cannot:
- Create an Event. Event is automatically created when a contract is signed.  
- Delete an Event. Event is deleted when the linked contract it deleted.  
- Delete a status. Event has always a status linked to them.

## Feature four: application handles new groups

There is three teams:

- management,
- sales,
- support.

CRM users from management team are the admins. They are the only ones to use the django admin website.  

The two other teams represent two different groups. The table below show what they can respectively do.


**GROUP SALES**

| Action           | Object    | Notes                                         |
|------------------|-----------|-----------------------------------------------|
| CREATE           | Account   |                                               |
| READ UPDATE      | Account   | the ones they are assigned to                 |
| READ UPDATE      | Contract  | the ones of the clients they are assigned to  |
| CREATE           | Event     |                                               |


**GROUP SUPPORT**

| Action           | Object    | Notes                                           |
|------------------|-----------|-------------------------------------------------|
| READ UPDATE      | Event     | the ones they are assigned to                   |
| READ             | Account   | the ones that they are assigned to their events |


### Feature five: soon  

### Feature six: soon


### Tests

In the tables, you will find what are the purposes of the tests.

#### Tests for feature 1 / App uses Django and PostgreSQL

| Item                         | version        | color code in the cli           |
|------------------------------|----------------|---------------------------------|
| Python                       | 3              | blue                            |
| Django                       | 3.0+           | blue                            |
| PostgreSQL                   | 12.0+          | blue                            |

#### Tests for Feature 2 / Adds a connexion page for users

| Item                                          | color code in the cli           | 
|-----------------------------------------------|---------------------------------|
| create user                                   | none/white                      |
| create superuser                              | none/white                      |
| admin page is configured                      | magenta                         |
| admin page is accessible                      | magenta                         |
| only managers can access admin page           | magenta                         |

#### Tests for Feature 3 / Adds model

| Model existence                               | color code in the cli           | 
|-----------------------------------------------|---------------------------------|
| Account                                       | yellow                          |
| Contract                                      | yellow                          |
| Event                                         | yellow                          |
| Status                                        | yellow                          |

#### Tests for Feature 4 / Adds django groups **NOT IMPLEMENTED YET**

| Groups Authorizationos                        | color code in the cli           | 
|-----------------------------------------------|---------------------------------|
| Sales                                         | cyan                            |
| Support                                       | cyan                            |

#### Run the tests

In the Command Line Interface:

| Comment                                    | Folder             | Instruction                      |
|--------------------------------------------|--------------------|----------------------------------|
| run tests                                  | root               | ```python manage.py test```      |
| run tests with verbose option and colors   | root               | ```python manage.py test -v 2``` |


### Optimization: soon