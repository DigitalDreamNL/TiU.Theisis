import re
from flask_micron import *


def execute(inhabitant):
    _checkLastName(inhabitant)
    _checkDateOfBirth(inhabitant)


class InvalidLastName(MicronClientError):
    """Invalid LastName; the LastName cannot be empty"""


def _checkLastName(inhabitant):
    if inhabitant['LastName'] is None:
        raise InvalidLastName()


class InvalidDateOfBirth(MicronClientError):
    """Invalid DateOfBirth; the DateOfBirth must use format YYYY-MM-DD"""


def _checkDateOfBirth(inhabitant):
    date = inhabitant['DateOfBirth']
    dateFormat = re.compile(r"^\d\d\d\d-\d\d-\d\d$")
    if date is None or dateFormat.match(date):
        return
    raise InvalidDateOfBirth()
