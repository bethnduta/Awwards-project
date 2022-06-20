## Author
Beth Nduta
### AWWARDS-LIKE PROJECT
![image](https://user-images.githubusercontent.com/85553801/173741821-942a2c3a-58c4-4491-aa95-226d5794d312.png)

## DESCRIPTION OF THE PROJECT
As a user you can:
* view posted projects and their details
* post a project to be rated/reviewed
* Rate/review other user's projects
* search for projects
* View projects overall score
* View your profile page

## TECHNOLOGIES USED
* PYTHON3.10.4
* DJANGO, MVC Framework
* HTML, CSS, BOOTSTRAP
* JAVASCRIPT
* POSTGRESQL
* HEROKU

## SETUP/INSTALLATION REQUIREMENTS
To access the code:
* clone the repo https://github.com/bethnduta/Awwards-project.git
* activate virtual environment using python3.10.4 as default handler python3 -m venv env && source env\bin\activate
* Install dependencies Install dependencies that will create an environment for the app to run pip install -r requirements.txt
* Create the database --psql
* CREATE DATABASE awwards
* env file Create .env file and paste the following filling where necessary: SECRET_KEY = <'secret_key>' DBNAME = 'awwards' USER = '' PASSWORD = '' DEBUG = True
* Run initial migration
* python 3.10.4 manage.py runmigrations awwards
* python 3.10.4 manage.py migrate
* Run the app python 3.10.4 manage.py runserver -open terminal on localhost:8000

## CURRENT BUGS
* There are no known bugs as of now. Incase you find one feel free to solve the bug and push the changes

## SUPPORT AND CONTACT DETAILS
Incase you want to contribute to the project fork the repository and make changes. Incase you wish to brainstorm any idea concerning the project kindly keep in touch with me through my;
* email[bethnduta05@gmail.com]
* slack[bethnduta]

## LICENSE
MIT Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## ACKNOWLEDGEMENTS
I acknowledge Maryann Mwikali as my technical mentor while learning Django framework
