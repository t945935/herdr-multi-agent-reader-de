"""Kleiner Vertrag für eine Entwicklungs- und Review-Übung."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Erwartet wird eine Zahl, bool ist ausgeschlossen")
    if not isfinite(value):
        raise ValueError("Erwartet wird eine endliche Zahl")
    return value


def add(a, b):
    return _number(a) + _number(b)


def subtract(a, b):
    return _number(a) - _number(b)


def multiply(a, b):
    return _number(a) * _number(b)


def divide(a, b):
    a, b = _number(a), _number(b)
    if b == 0:
        raise ZeroDivisionError("Division durch null ist nicht möglich")
    return a / b
