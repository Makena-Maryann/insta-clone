# Insta-clone

#### A clone of Instagram web app using Django. 

#### By **Maryann Makena**

## Setup/Installation Requirements

- To run the app, install `Python3`
- Then use these commands:
     1. `git clone https://github.com/Makena-Maryann/insta-clone.git`
     2. `cd insta-clone`
     3. `python -m venv virtual` to create a virtual environment named `virtual`
     4. `source virtual/bin/activate` to activate the virtual environment
     5. `psql` then `CREATE DATABASE instagram` to create a postgres database
     6. `pip install -r requirements.txt` to install dependencies
     7. `python3 manage.py makemigrations posts` then `python3 manage.py migrate` to create database migrations
     8. `python3 manage.py runserver` to run the app
     9. `python3 manage.py test posts` to run the tests

## User stories
As a user I would like to:
  1. Sign in to the application to start using.
  2. Upload my pictures to the app.
  3. See my profile with all my pictures.
  4. Follow other users and see their pictures on my timeline.
  5. Like a picture and leave a comment on it.

## Known Bugs

No known bugs.

## Technologies Used

Django
Python3
Bootstrap4
HTML
CSS
Heroku

## Support and contact details

Incase of any issues drop me an email at maryann.makena00@gmail.com

### License

MIT License

Copyright (c) 2020 Makena-Maryann

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.