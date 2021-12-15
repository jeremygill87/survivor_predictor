import csv

with open('SurvivorData.csv') as survivors:
    survivors_reader = csv.DictReader(survivors, delimiter=',')
    survivor_list = [survivor['Place'] for survivor in survivors_reader]