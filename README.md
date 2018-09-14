# Pitch-Perfect

 By [Lewis Mutuma](https://mutumamutuma.github.io/Portfolio/)

## Overview

Pitch It is a web application that is meant for users to add pitches on different categories and one can get likes or comments.

## Description

The Pitch It web application is meant for users to post pitches on any of the 7 different categories. These categories are:

    1. Interview Pitch
    2. Business
    3. Maths Pitch
    4. Pick-up lines
    5. Science and Tech

A user can select any of the categories from the a select field given in the app

Other users can give feedback to the pitch posts by commenting, liking or disliking the pitch. 

## Specifications

Get the specs [here](https://github.com/MutumaMutuma/PitchPerfect/blob/master/specs.md)

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

SQLAlchemy errors, automatic sign out has a short time span

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details

Contact me on lewismutuma1000@gmail.com for any comments, reviews or advice.

### License

    **MIT LICENSE** 
&copy; Copyright **Lewis Mutuma**