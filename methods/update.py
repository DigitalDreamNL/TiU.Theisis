from methods import validators
from copy import copy


def execute(adapter, inhabitant):
    inhabitant = copy(inhabitant)
    validators.inhabitant.execute(inhabitant)
    return adapter.update(inhabitant)
