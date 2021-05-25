# Order sample application
## Setup

The first thing to do is to clone the repository:

    $ git clone https://github.com/nmeowt/learn_django
    $ cd learn_django

Create a virtual environment to install dependencies in and activate it:
On MacOS:

    $ python3 -m venv venv
    $ . venv/bin/activate
On Windows

    $ py -3 -m venv venv
    $ venv\Scripts\activate

Then install the dependencies:

    (venv)$ 	pip install -r requirements.txt

Note the  `(venv)`  in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by  `venv`.

Once  `pip`  has finished downloading the dependencies:

    (venv)$ cd project
    (venv)$ python3 manage.py runserver
