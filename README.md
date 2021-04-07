# SauceCon 2021 Workshop - Build an API and API Testing Framework from Scratch in 120 Minutes

Hello! If you are reading this you likely are interested in or attending my [SauceCon 2021 Workshop](https://saucecon.com/workshops/) called "Build an API and API Testing Framework from Scratch in 120 Minutes". This is part of the workshop "API Testing and Monitoring". If you are not attending my workshop or not interested in API building and testing, then I hope you enjoy this repository nonetheless. 

The structure of this repository contains

- A simple [Flask](https://flask.palletsprojects.com/en/1.1.x/) application for creating a "Sauce Log", a database for a list of hot sauces and their descriptions, and
- A fairly simple API test framework written using [pytest](https://pytest.org) and [requests](https://docs.python-requests.org/en/master/).

The workshop shall walk through the API app and test framework.

## Before You Start

This is a Python project, so you will need Python 3.7+ installed on your machine. A good IDE such as PyCharm or VS Code is recommeded.

## The Layout of the Workshop

The workshop at SauceCon - which [you should totally check out](https://www.saucecon.com) - will walk through developing this Flask app and in turn developing an API test framework for it. This is done using some tags. Here's what each tag will show:

- *v1-starting* Creating an initial app with a single endpoint
- *v2-post-get* Creating two endpoints that allow POST and GET requests
- *v3-flask-restful* Adding in Flask-Restful, a library for writing REST APIs
- *v4-add-db* Implementing a SQL database to maintain app state and data
- *t1-entries-test* Writing our first test
- *t2-entry-tests* Writing some more complex tests
- *t3-api-wrapper* Looking for patterns and making a lightweight test framework
- *t4-api-utilities* From good to great


## Installing And Setting up the Project

Please clone this repo since there are some tags that are used for the workshop. You can also download the ZIP file of this repo to work with the final product. 

### Virtual Environment

To install the product, first create a Python [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) by running this in the directory you just cloned:

```
python -m venv venv
```

then activate the virtual environment with

```
source venv/bin/activate 
```

on Mac/Linux, or

```
.\venv\bin\Activate.psl
```

on Windows 10.

Your terminal should have `(venv)` at the start of it once the virtual environment is activated. You can also use PyCharm to handle virtual environments. 

### Installing Dependencies

To install dependencies, run

```
pip install -r requirements.txt
```

You should be ready to go! 

## Starting the Flask App

If you like skipping ahead, you can start the app running

```
gunicorn --bind 0.0.0.0:5000 main:app
```

which will start the app locally at `http://localhost:5000`. You can check that this is up and running by executing

```
http://localhost:5000/sauce_logs
```

in a browser window or using curl. You should see a nice welcome message. 

## Running the API Tests

Once you have the app up and running, you can run the tests by executing

```
pytest
```

All tests should pass. If they do not, check that the app is running on port 5000.