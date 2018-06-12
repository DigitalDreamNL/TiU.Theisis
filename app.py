from flask import Flask
from flask_micron import *
import methods
import config

app = Flask(__name__)
micron = Micron(app)


@micron.method()
def create(inhabitant):
    return methods.create.execute(config.adapter, inhabitant)


@micron.method()
def find_all():
    return methods.find_all.execute(config.adapter)


@micron.method()
def find_by_id(id):
    return methods.find_by_id.execute(config.adapter, id)


@micron.method()
def find_by_name(name):
    return methods.find_by_name.execute(config.adapter, name)


@micron.method()
def delete(id):
    return methods.delete.execute(config.adapter, id)


@micron.method()
def update(inhabitant):
    return methods.update.execute(config.adapter, inhabitant)
