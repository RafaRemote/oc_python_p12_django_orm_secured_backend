# Openclassrooms Path: Python Developer
# Project n.12: Develop a secured back-end architecture using Django ORM
## API built on top of a Djano App for a CRM Software(Epic-Events)

## Quality Assurance Branch

Coverage feature added.

#### Installation

In a Command Line Interface:

_the root folder is the directory 'epicevents' containing the manage.py file_

| Comment                                    | Folder                | Instruction                                                             |
|--------------------------------------------|-----------------------|-------------------------------------------------------------------------|
| install the dependencies                   | root                  | ```pip install -r requirements.txt```                                   |

It will install coverage.py

## Test the coverage

| Comment                                           | Folder                       | Instruction                                          |
|---------------------------------------------------|------------------------------|------------------------------------------------------|
| first instruction                                 | folder containing manage.py  | ``` coverage run --source='.' manage.py test  ```    |
| checks the coverage, will show a table in the CLI | folder containing manage.py  | ``` coverage report ```                              |
