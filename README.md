# TiU.Theisis

API Layer for an application that allows for dynamic addition of attributes. Both PostgreSQL (SQL database) and MongoDB (NoSQL database) are supported through specific Data Adapter Interfaces.

This project has been developed as part of my thesis for the Master Information Management program at Tilburg University.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Python modules

This project requires the following modules:

* [PyGreSQL](http://www.pygresql.org/) (PostgreSQL interface)
* [PyMongo](https://api.mongodb.com/python/current/) (MongoDB interface)
* [Flask](http://flask.pocoo.org/) (Python microframework)
* [Flask Micron](https://github.com/mmakaay/flask_micron) (API framework built on top of Flask)
* SetupTools

All modules, except for Flask Micron, can be installed using pip package manager:

```
pip install pygresql
pip install pymongo
pip install flask
pip install setuptools
```

Flask Micron must be cloned manually and installed using the following command (requires SetupTools):

```
python setup.py install 
```

#### Databases

The Data Adapter Interfaces support the following databases:

* In-memory database (for development)
* [PostgreSQL](https://www.postgresql.org/) (SQL database)
* [MongoDB](https://www.mongodb.com/) (NoSQL database)

### Installing

To run the application, configure the desired Data Adapter Interface in `config.py` by uncommenting the line
and adding configuration parameters.

Then, run the application using the following command:

```
python.exe -m flask run
```

#### Example request

Create a record in the database by sending a POST request with a JSON object to the `/create` endpoint.

Example input:

```
{
    "FirstName": "Robert",
    "LastName": "Martin",
    "DateOfBirth": "1952-09-17",
    "ShelterId": "14" 
}
```

Example output (is input with newly assigned Id):

```
{
    "Id": "5b1d4dd15768a23ab4ba1fd7"
    "FirstName": "Robert",
    "LastName": "Martin",
    "DateOfBirth": "1952-09-17",
    "ShelterId": "14" 
}
```

## Acknowledgments

* Special thanks to Maurice Makaay [@mmakaay](https://github.com/mmakaay) without whom there would be no TiU.Theisis API Layer.