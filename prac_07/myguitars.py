import csv
from guitar import Guitar
from collections import namedtuple

def main():
    guitars = []
    in_file = open('languages.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        