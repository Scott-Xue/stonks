"""Reads the given csv file into a list of strings containing the names of the securities."""

import csv
import os


def load(file):
    assert os.path.isfile(file)
    with open(file) as f:
        reader = csv.reader(f)
        return next(reader)

