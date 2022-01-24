# Epic Events: Develop a secured back-end architecture using Django ORM

## Summary

| #                 | Feature                                     |
|-------------------|---------------------------------------------|
|[1](#feature-one)  | app uses Django and PostgreSQL              |
|[2](#feature-two)  | adds connexion page for users               |
|[3](#feature-three)| adds connexion page for users               |



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

==> **Check if the version of your interpreter is Python 3.9.2**

#### Database configuration

First: if not already done: install PostgreSQL on your machine: link => [download PostgreSQL](https://www.postgresql.org/download/)  
Same with pgAdmin4: link => [download pgAdmin4](https://www.pgadmin.org/download/)  

Then: create a database with the settings of your choice.  

In the root folder, rename the file ```.env.template``` to ```.env```  
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

| Comment                                    | Folder             | Instruction                                                       |
|--------------------------------------------|--------------------|-------------------------------------------------------------------|
| change to root directory                   | chose folder       | ```cd epicevents```                                               |
| run the server                             | root               | ```python manage.py runserver```                                  |

Then, in your web browser navigate to http://127.0.0.1:8000/

#### Tests for feature 1 / App uses Django and PostgreSQL

Tests checks these below conditions:

| Item                         | version        | color code in the cli |
|------------------------------|----------------|-----------------------|
| Python                       | 3              | blue                  |
| Django                       | 3.0+           | blue                  |
| PostgreSQL                   | 12.0+          | blue                  |

#### Run the tests

In a Command Line Interface (be sure to be in the same folder as the one containing the file manage.py).  

| Comment                                    | Folder             | Instruction                                                  |
|--------------------------------------------|--------------------|--------------------------------------------------------------|
| run tests                                  | root               | ```python manage.py test```                                  |
| run tests with verbose option and colors   | root               | ```python manage.py test -v 2```                             |

## #Feature two 
### Adds a connexion page for users

#### Migrations

A custom user model have been created. 
In order to save the changes to the database type:

| Comment                                    | Folder             | Instruction                                                  |
|--------------------------------------------|--------------------|--------------------------------------------------------------|
| prepare the migration files                | root               | ```python manage.py makemigrations users```                  |
| migrate to the database                    | root               | ```python manage.py migrate```                               |


#### Access to admin login page

First: in the CLI, create a super user, type: ```python manage.py createsuperuser```

In your web browser navigate to http://127.0.0.1:8000/admin/

You can access the admin page with the credentials you have entered for the superuser.  

On the admin page you can create users.  
There is three roles available for the users: management, sales or support.  
Only the users with a management role will be able to access to the admin page.  

You can try to create users for management, sales and support the try to login to the admin site.  
You will see that only the users with a management role can access the admin site.  

#### Additional Tests for Feature 2 / Adds a connexion page for users

Tests checks these below conditions:

| Item                                | color code in the cli | 
|-------------------------------------|-----------------------|
| create user                         | none/white            |
| create superuser                    | none/white            |
| admin page is configured            | magenta               |
| admin page is accessible            | magenta               |
| only managers can access admin page | magenta               |

#### Run the tests

In the Command Line Interface:

| Comment                                    | Folder             | Instruction                                                  |
|--------------------------------------------|--------------------|--------------------------------------------------------------|
| run tests                                  | root               | ```python manage.py test```                                  |
| run tests with verbose option and colors   | root               | ```python manage.py test -v 2```                             |


## #Feature three
### Application handles models


| Models handled by the application   
|-------------------------------------|
| Account                             |
| Contract                            |
| Event                               |
| Status                              |

To populate the Status table, in the CLI: change on the root folder and type:  

```python manage.py loaddata status/fixtures/status.json```
