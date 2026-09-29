import pandas as pd

database = []

def write_csv():
with open("database", "w") as db:
    for item in database:
        db.write(f"{item}\n")

def read_csv():
with open("database", "r") as db:
    for item in database:
        content = database.read()
        print(content)

