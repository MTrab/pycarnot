"""Test file for the library."""

from os import environ

from pycarnot import Carnot

API_KEY = environ["API_KEY"]
EMAIL = environ["EMAIL"]

carnot = Carnot(EMAIL, API_KEY, "DK1")
carnot.update()

print(carnot)
