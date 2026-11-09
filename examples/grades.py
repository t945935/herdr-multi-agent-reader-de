"""Gemeinsamer Vertrag; die Rangfolge verwendet ungerundete Gesamtpunktzahlen."""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"Deutsch", "Geschichte", "Mathematik"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("Die Noten müssen genau Deutsch, Geschichte und Mathematik enthalten")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Noten müssen numerisch und dürfen nicht boolesch sein")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("Noten müssen endlich und zwischen 0 und 100 liegen")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("Der Durchschnitt muss numerisch sein")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("Der Durchschnitt muss zwischen 0 und 100 liegen")
    return "Bestanden" if average >= 60 else "Nicht bestanden"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("Schülerinnen und Schüler müssen als Liste angegeben werden")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("Jeder Schülerdatensatz muss ein Objekt sein")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Der Name ist erforderlich")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
