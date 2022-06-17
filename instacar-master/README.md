# INSTACAR

## Technology Stack:
### Backend
* #### Django(Python3)
###### Django is used here because of it's powerful underlying code that makes it very convenient to use and focus on logic rather than boilerplate code and also because of Python's ease of use.

### Frontend
* #### HTML/CSS
* #### JavaScript
* #### Bootstrap
  ###### It is a frontend framework which makes it is easier to design elements in HTML without worrying much about CSS(Bootstrap uses it's own CSS, JS, jQuery). Easy to use and saves a lot of time when creating basic/minimal frontend

### Database
* #### SQLite
  ###### It is used(which comes bundled with Django). This is only used for development purpose and a more powerful datatbase should be used in production.

### Deployment
* #### Docker
  ###### Docker is undoubtedly one of the easiest ways to deploy a project. It's ease of use is the main reason and also the fact that if it runs on my machine, it will probably run on any other machine with docker installed.

## How to Use?
* Create a python3 virtual environment, navigate to project directory on terminal and install dependencies(listed in requirements.txt file) using the command
  `pip install requirements.txt` <br>
  RUN `python manage.py makemigrations` and `python manage.py migrate` <br>to create tables in database. <br>
  To run server, use command `python manage.py runserver`

* If Docker is installed, navigate to project directory on terminal,<br> RUN `docker-compose up`.

* Open a browser and navigate to <b>localhost:8000</b> to use the website.

* For now, source is fixed at Bengaluru and it's distance from certain cities is stored in the db. One can add more cities and their distances using the admin panel provided by Django by accessing <b>localhost:8000/admin</b>

## Security Features
* Cross site scripting (XSS) protection
* Cross site request forgery (CSRF) protection
* SQL injection protection

###### These security features are already provided by Django, so that makes a website safe from the most common vulnerabilities.
