<<<<<<< HEAD
# Pitch-Perfect

 By [Lewis Mutuma](https://mutumamutuma.github.io/Portfolio/)
=======
# Pitch

# Author

by abdirahman-mahat
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b

## Overview

Pitch It is a web application that is meant for users to add pitches on different categories and one can get likes or comments.

## Description

The Pitch It web application is meant for users to post pitches on any of the 7 different categories. These categories are:

<<<<<<< HEAD
    1. Interview Pitch
    2. Business
    3. Maths Pitch
    4. Pick-up lines
    5. Science and Tech

=======
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
A user can select any of the categories from the a select field given in the app

Other users can give feedback to the pitch posts by commenting, liking or disliking the pitch. 

## Specifications

<<<<<<< HEAD
Get the specs [here](https://github.com/MutumaMutuma/Pitch/blob/master/specs.md)
=======

Get the specs [here](https://github.com/abdirahman-mahat/pitch/blob/master/specs.md)
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b

## Set-up and Installation

### Prerequiites

    - Python 3.6
    - Ubuntu software

### Create a Virtual Environment

Run the following commands in the same terminal:

```sudo apt-get install python3.6-venv```

```python3.6 -m venv virtual```

```source virtual/bin/activate```

### Install dependancies

Install dependancies that will create an environment for the app to run

```pip3 install -r requirements```

Install [Postgres](https://www.postgresql.org/download/)

### Prepare environment variables

```export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchperfect'```

```export SECRET_KEY='Your secret key'```

### Run Database Migrations

```python manage.py db init```

```python manage.py db migrate -m "initial migration"```

```python manage.py db upgrade```


### Running the app in development

In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

<<<<<<< HEAD
SQLAlchemy errors, automatic sign out has a short time span
=======
SQLAlchemy errors, automatic sign out has a short time span, deployment to heroku
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details

<<<<<<< HEAD
Contact me on lewismutuma1000@gmail.com for any comments, reviews or advice.
=======
Contact me on abdirahmanmahat3@gmail.com for any comments, reviews or advice.
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b

### License

    **MIT LICENSE** 
<<<<<<< HEAD
&copy; Copyright **Lewis Mutuma**
=======
&copy; Copyright **abdirahman mahat**
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
