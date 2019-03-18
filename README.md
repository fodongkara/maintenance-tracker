# Maintenance Tracker

[![Coverage Status](https://coveralls.io/repos/github/3Nakajugo/maintenance-tracker/badge.svg?branch=ft-codeclimate-164393081)](https://coveralls.io/github/3Nakajugo/maintenance-tracker?branch=ft-codeclimate-164393081)
[![Build Status](https://travis-ci.org/fodongkara/maintenance-tracker.svg?branch=develop)](https://travis-ci.org/fodongkara/maintenance-tracker)
[![Maintainability](https://api.codeclimate.com/v1/badges/ba3df7af94b1e38f81d5/maintainability)](https://codeclimate.com/github/3Nakajugo/maintenance-tracker/maintainability)
=======
## Introduction

Maintenance Tracker App is an application that provides users with the ability to reach out to the operations or repairs department regarding issues that need reapairs or maintenance. users make requests and they are able to track the status of their request


## Features

- Users can create an account and login.
- The users should beable to make maintenance or repair requests.
- An admin should be able to approve or reject a repair or maintenance request and provide comments
- The admin should be able to mark a request as resolved once its done
- The admin should be able to view all maintenance and repair requests on the application
- The admin should be able to filter requests
- The user can view all their requests


## Technologies

- [Python 3.6](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
- [Git](https://git-scm.com/) - Git is a distributed version-control system for tracking changes in source code during software development.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) - A tool to create isolated Python environments.
- [Django 2.1.7](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Postgresql](https://www.postgresql.org/) - PostgreSQL, often simply Postgres, is an open source object-relational database management system


## Setup
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Ensure you have the following softwares to run this application.

### Local deployment.
Open your Console, Terminal or Command Prompt, navigate to the directory that you want to work from and folllow the steps below.

1. Clone this repository by running
> `git clone https://github.com/fodongkara/maintenance-tracker.git`
2. Navigate into the project folder
> `cd maintenance-tracker`.
3. Create  Virtual Environment by running
> `mkvirtualenv Tracker`.
4. Set that folder to become the project directory of the virtual environment
> `setprojectdir .`.
5. Run the virtual environment
> `workon Tracker`.
6. Install required depenencies by running
> `pip install -r requirements.txt`
7. Launch / Run the development server.
> `python manage.py runserver`


## Testing
To get the full test report and coverage of the application, run the following commands.

1. To get the test coverage run.
> `coverage run manage.py test -v 2`
2. To get the test report run.
> `coverage html`


## Contributers
> [Edna Nakajugo](https://github.com/3Nakajugo) || 
> [Kenneth Sanya](https://github.com/sanya-kenneth) || 
> [Nelson Adralia](https://github.com/nadralia) || 
> [Lamech Lwasampijja](https://github.com/llwasampijja) || 
> [James Francis Kisuule](https://github.com/engjames) || 
> [James Mudidi](https://github.com/JamesMudidi)


## Acknowledgements
> [Frank Odongkara](https://github.com/fodongkara)